#!/usr/bin/env python3
"""Check, synchronize and package the two client editions; Python 3.9+."""

import argparse
import hashlib
import json
import os
from pathlib import Path
import runpy
import shutil
import tempfile


CLIENTS = ("codex", "claude")
ROOT_FILES = (
    "README.md", "INSTALL.md", "VERSION", "LICENSE", "CHANGELOG.md",
    "CONTRIBUTING.md", "AGENTS.md", "CLAUDE.md", "SUPPORT.md", "SECURITY.md",
    ".gitignore", ".agents/plugins/marketplace.json", ".claude-plugin/marketplace.json",
    "docs/skills.md", "docs/update.md", "scripts/manage.py", "tests/test_repository.py",
    ".github/workflows/validate.yml", ".github/ISSUE_TEMPLATE/bug_report.yml",
    ".github/ISSUE_TEMPLATE/feature_request.yml", ".github/PULL_REQUEST_TEMPLATE.md",
    ".github/VULNERABILITY_REPORT.yml", "assets/design-agent-skills-hero.svg",
    "assets/plugin-icon.svg", "assets/social-preview.png",
)


def json_bytes(value):
    return (json.dumps(value, indent=2, sort_keys=True, ensure_ascii=False) + "\n").encode("utf-8")


def sha256(data):
    return hashlib.sha256(data).hexdigest()


def plain_root(root):
    root = Path(root).absolute()
    if any(path.is_symlink() for path in (root, *root.parents)):
        raise ValueError("Symlink repository path is not accepted")
    return root


def inventory(root, strict=False):
    names = set()
    for directory, dirs, files in os.walk(root, followlinks=False):
        for name in list(dirs) + files:
            path = Path(directory) / name
            metadata = (Path(directory) == root and name in (".git", ".idea", ".vscode"))
            if strict and metadata:
                raise ValueError("Working-copy metadata is not allowed in a strict package: " + name)
            if not strict and (metadata or name in ("__pycache__", ".DS_Store")):
                if name in dirs:
                    dirs.remove(name)
                continue
            if path.is_symlink() or not (path.is_file() or path.is_dir()):
                raise ValueError("Non-regular repository entry: " + str(path))
            if path.is_file():
                names.add(path.relative_to(root).as_posix())
    return names


def expected_payload(root):
    root = plain_root(root)
    # Native clients resolve their own entrypoint from the same repository root.
    codex = json.loads((root / ".agents/plugins/marketplace.json").read_text())
    claude = json.loads((root / ".claude-plugin/marketplace.json").read_text())
    if (codex.get("name") != "design-agent-skills" or len(codex.get("plugins", [])) != 1
            or codex["plugins"][0].get("name") != "design-agent-skills"
            or codex["plugins"][0].get("source") != {"source": "local", "path": "./packages/codex"}):
        raise ValueError("Codex marketplace must select packages/codex")
    if (claude.get("name") != "design-agent-skills" or len(claude.get("plugins", [])) != 1
            or claude["plugins"][0].get("name") != "design-agent-skills"
            or claude["plugins"][0].get("source") != "./packages/claude"):
        raise ValueError("Claude marketplace must select packages/claude")
    payload = {name: (root / name).read_bytes() for name in ROOT_FILES}
    version = payload["VERSION"].decode("utf-8").rstrip("\n")
    packages = {}
    for client in CLIENTS:
        package = root / "packages" / client
        manage = runpy.run_path(str(package / "scripts/manage.py"))
        api = manage["verifier"](package)
        generated = manage["expected_payload"](package)
        result = manage["validate_payload"](generated, api)
        if result["version"] != version or result["clientTarget"] != client + "-" + version:
            raise ValueError("Client package/version mismatch: " + client)
        payload.update({"packages/" + client + "/" + name: data for name, data in generated.items()})
        packages[client] = result
    # Reuse the client verifier's existing Markdown/anchor checker on a clean projection.
    with tempfile.TemporaryDirectory(prefix="das-repository-links-") as temporary:
        projection = Path(temporary).resolve()
        for name, data in payload.items():
            path = projection / name
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(data)
        api["check_links"](projection, set(payload))
    payload["MANIFEST.json"] = json_bytes({
        "schema": "das-repository-v1", "version": version,
        "packages": {client: {"path": "packages/" + client, "clientTarget": value["clientTarget"],
                                "sourceDigest": value["sourceDigest"]} for client, value in packages.items()},
        "files": [{"path": name, "bytes": len(data), "sha256": sha256(data)}
                  for name, data in sorted(payload.items())],
    })
    return payload, {"status": "pass", "version": version, "files": len(payload), "packages": packages}


def check_repository(root, strict=False):
    root = plain_root(root)
    inventory(root, strict=strict)  # Reject symlinks before opening any source file.
    payload, result = expected_payload(root)
    actual = inventory(root, strict=strict)
    if actual != set(payload):
        raise ValueError("Unexpected/missing repository files: " + repr(sorted(actual ^ set(payload))))
    changed = [name for name, data in payload.items() if (root / name).read_bytes() != data]
    if changed:
        raise ValueError("Stale generated files; run sync: " + repr(changed[:5]))
    return result


def sync(root):
    root = plain_root(root)
    actual = inventory(root)
    payload, result = expected_payload(root)
    if actual - set(payload):
        raise ValueError("Unexpected repository files: " + repr(sorted(actual - set(payload))))
    # All source pins, pointers and projections passed before the first write.
    for name, data in payload.items():
        path = root / name
        if not path.exists() or path.read_bytes() != data:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(data)
    return result


def build(root, output_dir):
    root = plain_root(root)
    result = check_repository(root)
    output_dir = plain_root(output_dir)
    if output_dir.exists() or output_dir == root or root in output_dir.parents:
        raise ValueError("Build into a new directory outside the repository")
    output_dir.mkdir(parents=True)
    packages = {}
    try:
        with tempfile.TemporaryDirectory(prefix="das-client-archives-") as temporary:
            for client in CLIENTS:
                package = root / "packages" / client
                manage = runpy.run_path(str(package / "scripts/manage.py"))
                built = manage["build"](package, Path(temporary).resolve() / client)
                for field in ("archive", "checksum"):
                    src = Path(built[field])
                    target = output_dir / src.name
                    shutil.copyfile(src, target)
                    built[field] = str(target)
                packages[client] = {key: value for key, value in built.items()
                                    if key not in ("tree", "excludedMetadata")}
        return {"version": result["version"], "packages": packages}
    except Exception:
        shutil.rmtree(output_dir)
        raise


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).absolute().parents[1])
    sub = parser.add_subparsers(dest="command", required=True)
    check = sub.add_parser("check")
    check.add_argument("--strict", action="store_true")
    sub.add_parser("sync")
    package = sub.add_parser("build")
    package.add_argument("--output-dir", required=True, type=Path)
    args = parser.parse_args()
    try:
        result = (check_repository(args.root, args.strict) if args.command == "check"
                  else sync(args.root) if args.command == "sync" else build(args.root, args.output_dir))
    except (OSError, ValueError, KeyError, TypeError) as error:
        parser.exit(1, "DAS maintenance failed: " + str(error) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
