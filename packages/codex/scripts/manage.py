#!/usr/bin/env python3
"""Maintain and build DAS from this public repository; Python 3.9+ standard library."""

import argparse
import json
import os
from pathlib import Path
import re
import runpy
import shutil
import tempfile
import zipfile


REPOSITORY_FILES = (
    "README.md", "INSTALL.md", "LICENSE", "CHANGELOG.md", "CONTRIBUTING.md", "AGENTS.md", "CLAUDE.md",
    "SUPPORT.md", "SECURITY.md", ".github/VULNERABILITY_REPORT.yml",
    "docs/codex.md", "docs/claude-code.md", "docs/claude-desktop.md", "docs/getting-started.md",
    "docs/skills.md", "docs/advanced-installation.md", "docs/how-das-works.md",
    "scripts/manage.py", "tests/test_repository.py", ".github/workflows/validate.yml",
    ".github/ISSUE_TEMPLATE/bug_report.yml", ".github/ISSUE_TEMPLATE/feature_request.yml",
    ".github/PULL_REQUEST_TEMPLATE.md",
    ".gitignore", "VERSION", "verify.py",
    "assets/design-agent-skills-hero.svg", ".claude-plugin/plugin.json", ".claude-plugin/marketplace.json",
    ".codex-plugin/plugin.json", ".agents/plugins/marketplace.json",
)
ROOT_METADATA = {".git", ".idea", ".vscode", "dist"}
ZIP_DATE = (2026, 10, 13, 0, 0, 0)


def json_bytes(value):
    return (json.dumps(value, indent=2, sort_keys=True, ensure_ascii=False) + "\n").encode("utf-8")


def verifier(root):
    return runpy.run_path(str(root / "verify.py"))


def read_file(root, name, api):
    path = api["plain_path"](root / name)
    if not path.is_file():
        raise ValueError("Missing regular source file: " + name)
    return path.read_bytes()


def expected_payload(root):
    """Derive every generated file from the editable files in this repository."""
    root = Path(root).absolute()
    api = verifier(root)
    root = api["plain_path"](root)
    target = None
    if (root / "MANIFEST.json").is_file():
        target = api["check_target"](root, json.loads(read_file(root, "MANIFEST.json", api)))
    elif (root / "TARGET.json").is_file():
        target = api["target_from_record"](json.loads(read_file(root, "TARGET.json", api)))
    names = api["repository_files"](REPOSITORY_FILES, target)
    payload = {name: read_file(root, name, api) for name in names}
    if target:
        payload["TARGET.json"] = read_file(root, "TARGET.json", api)
    version = payload["VERSION"].decode("utf-8").rstrip("\n")
    if (not re.fullmatch(r"\d+\.\d+\.\d+(?:-[0-9A-Za-z.-]+)?(?:\+[0-9A-Za-z.-]+)?", version)
            or payload["VERSION"] != (version + "\n").encode("utf-8")):
        raise ValueError("VERSION must contain one version followed by a newline")
    # Keep the advertised plugin versions for this artifact tied to VERSION.
    for name in (".claude-plugin/plugin.json", ".codex-plugin/plugin.json"):
        if name not in payload:
            continue
        metadata = json.loads(payload[name])
        if metadata.get("version") != version:
            metadata["version"] = version
            payload[name] = json_bytes(metadata)
    originals = {}
    for name in api["SOURCES"]:
        data = read_file(root, name, api)
        if name.startswith("skills/"):
            entry = name.split("/")[1]
            inverse = {export: source for source, export in api["path_mapping"](entry).items()}
            originals[name] = api["transform"](data, "SKILL.md", inverse)
        else:
            originals[name] = data
            payload[name] = data
    digest = api["source_digest"]([
        {"sourcePath": name, "sourceSHA256": api["sha256"](data)}
        for name, data in sorted(originals.items())
    ])

    # Check recovered editable sources before sync writes; old manifests cannot bless drift.
    api["validate_source_target"](target, digest)

    def file_records(files):
        return [{"path": name, "bytes": len(data), "sha256": api["sha256"](data)}
                for name, data in sorted(files.items())]

    for entry in api["SKILLS"]:
        mapping = api["path_mapping"](entry)
        files = {name: payload[name] for name in ("VERSION", "verify.py", "LICENSE")}
        if target:
            files["TARGET.json"] = payload["TARGET.json"]
        records = []
        for source, data in sorted(originals.items()):
            exported = api["transform"](data, source, mapping)
            files[mapping[source]] = exported
            records.append({"sourcePath": source, "sourceSHA256": api["sha256"](data),
                            "exportPath": mapping[source], "exportSHA256": api["sha256"](exported)})
        own_path = "skills/" + entry + "/SKILL.md"
        if files["SKILL.md"] != read_file(root, own_path, api):
            raise ValueError("Entrypoint links do not round-trip: " + own_path)
        files["MANIFEST.json"] = json_bytes({
            "schema": "das-portable-v1", "kind": "skill", "version": version,
            "entrypoint": entry, "sourceDigest": digest, "sources": records,
            **({"clientTarget": target} if target else {}),
            "files": file_records(files),
        })
        payload.update({"skills/" + entry + "/" + name: data for name, data in files.items()})
    payload["MANIFEST.json"] = json_bytes({
        "schema": "das-portable-v1", "kind": "bundle", "version": version,
        "entrypoints": list(api["SKILLS"]), "sourceDigest": digest,
        "sourceFiles": list(api["SOURCES"]), "files": file_records(payload),
        **({"clientTarget": target} if target else {}),
    })
    return payload


def inventory(root, strict=False):
    """Exclude named working-copy metadata, never arbitrary extra payload."""
    files, excluded = set(), []
    for directory, dirs, names in os.walk(root, followlinks=False):
        for name in list(dirs) + list(names):
            path = Path(directory) / name
            relative = path.relative_to(root).as_posix()
            ignored = (not strict and (
                (Path(directory) == root and name in ROOT_METADATA)
                or name == ".DS_Store" or name == "__pycache__"))
            if ignored:
                excluded.append(relative)
                if name in dirs:
                    dirs.remove(name)
                continue
            if path.is_symlink() or not (path.is_file() or path.is_dir()):
                raise ValueError("Non-regular repository entry: " + relative)
            if path.is_file():
                files.add(relative)
    return files, sorted(excluded)


def write_payload(root, payload):
    for name, data in sorted(payload.items()):
        path = root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(data)


def validate_payload(payload, api):
    # Strict package verification uses a clean projection. The working copy is not changed.
    with tempfile.TemporaryDirectory(prefix="das-verify-") as temporary:
        root = Path(temporary).resolve()
        write_payload(root, payload)
        return api["check"](root)


def checked_payload(root, strict=False):
    root = Path(root).absolute()
    payload = expected_payload(root)
    actual, excluded = inventory(root, strict=strict)
    if actual != set(payload):
        raise ValueError("Unexpected/missing files: " + repr(sorted(actual ^ set(payload))))
    changed = [name for name, data in sorted(payload.items()) if (root / name).read_bytes() != data]
    if changed:
        examples = ", ".join(changed[:5])
        raise ValueError("Stale generated files (" + str(len(changed))
                         + "); run python3 scripts/manage.py sync: " + examples)
    result = validate_payload(payload, verifier(root))
    result["excludedMetadata"] = excluded
    return payload, result


def check_repository(root, strict=False):
    return checked_payload(root, strict=strict)[1]


def sync(root):
    root = Path(root).absolute()
    payload = expected_payload(root)
    actual, excluded = inventory(root)
    unexpected = actual - set(payload)
    if unexpected:
        raise ValueError("Unexpected files: " + repr(sorted(unexpected)))
    result = validate_payload(payload, verifier(root))
    changed = {name: data for name, data in payload.items()
               if not (root / name).is_file() or (root / name).read_bytes() != data}
    write_payload(root, changed)
    result.update({"updatedFiles": len(changed), "excludedMetadata": excluded})
    return result


def build(root, output_dir):
    root = Path(root).absolute()
    payload, result = checked_payload(root)
    api = verifier(root)
    root, output_dir = api["plain_path"](root), api["plain_path"](output_dir)
    if output_dir == root or root in output_dir.parents:
        raise ValueError("Build outside the repository to keep generated SKILL.md copies out of discovery")
    if output_dir.exists():
        raise FileExistsError("Refusing to overwrite output directory: " + str(output_dir))
    label = api["artifact_label"](result["version"], result.get("clientTarget"))
    tree, archive = output_dir / label, output_dir / (label + ".zip")
    checksum = output_dir / (label + ".sha256")
    output_dir.mkdir(parents=True)
    try:
        write_payload(tree, payload)
        api["check"](tree)
        with archive.open("xb") as stream:
            with zipfile.ZipFile(stream, "w", compression=zipfile.ZIP_DEFLATED) as package:
                for name, data in sorted(payload.items()):
                    metadata = zipfile.ZipInfo(label + "/" + name, date_time=ZIP_DATE)
                    metadata.create_system = 3
                    metadata.compress_type = zipfile.ZIP_DEFLATED
                    metadata.external_attr = 0o100644 << 16
                    package.writestr(metadata, data, compresslevel=9)
        archive_hash = api["sha256"](archive.read_bytes())
        checksum.write_text(archive_hash + "  " + archive.name + "\n", encoding="ascii")
    except Exception:
        shutil.rmtree(output_dir)
        raise
    return {"version": result["version"], "sourceDigest": result["sourceDigest"],
            "clientTarget": result.get("clientTarget"),
            "tree": str(tree), "archive": str(archive), "archiveSHA256": archive_hash,
            "checksum": str(checksum), "excludedMetadata": result["excludedMetadata"]}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).absolute().parents[1])
    commands = parser.add_subparsers(dest="command", required=True)
    commands.add_parser("sync", help="Regenerate installed copies and manifests from editable sources")
    check = commands.add_parser("check", help="Check sources, generated copies, manifests, and local links")
    check.add_argument("--strict", action="store_true", help="Reject working-copy metadata as extra payload")
    package = commands.add_parser("build", help="Build a checked release into a new external directory")
    package.add_argument("--output-dir", type=Path, required=True)
    args = parser.parse_args()
    try:
        if args.command == "sync":
            result = sync(args.root)
        elif args.command == "check":
            result = check_repository(args.root, strict=args.strict)
        else:
            result = build(args.root, args.output_dir)
    except (OSError, ValueError, KeyError, TypeError) as error:
        parser.exit(1, "DAS maintenance failed: " + str(error) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
