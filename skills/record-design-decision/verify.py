#!/usr/bin/env python3
"""Verify a DAS portable bundle or one independently installed skill (Python 3.9+)."""

import argparse
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import posixpath
import re
import urllib.parse


SKILLS = (
    "assess-design-reuse", "audit-design-surface", "audit-design-system",
    "design-router", "develop-visual-direction", "evolve-design-system",
    "explore-design-directions", "frame-design-task", "maintain-design-knowledge",
    "prototype-design-directions", "publish-design-system-canon",
    "reconstruct-design-context", "record-design-decision",
    "validate-design-contract", "verify-design-implementation", "write-design-contract",
)
REFERENCES = (
    "audit-exploration-templates", "authority-and-status", "contract-review-templates",
    "design-knowledge-index", "design-lab-protocol", "design-system-craft",
    "engineering-integration",
    "packet-projections", "product-profile-and-tools", "quality-checklists",
    "task-context-templates", "visual-craft",
)
SOURCES = tuple(sorted(
    ["skills/" + name + "/SKILL.md" for name in SKILLS]
    + ["references/" + name + ".md" for name in REFERENCES]
))
CODEX_TARGET_ID = "codex-20261017"
CODEX_TARGET_RECORD = {
    "client": "codex",
    "id": "codex-20261017",
    "qualification": {
        "claudeQualification": "not conferred",
        "effort": "ultra",
        "model": "gpt-6-astra",
        "packagingInstallationQualification": "not implied; requires separate artifact evidence",
        "route": "native explicit named-skill chat",
        "scope": "bounded Fieldnote, BorrowDesk, source-conflict control, E02, E04 plus unchanged E07 chain evidence"
    },
    "schema": "das-client-target-v1",
    "selectedSourceMapSHA256": "4f8262ea079cc09b69d8a18a22303600f8fa5cd22f728852155adc7b772385d9",
    "sourceDigest": "dbbc3101c90a4a852fecaf3ae2c3a8f68cdf3b9ba6a38c148a06ea2797580e34",
    "sourceMapAlgorithm": "sorted path + NUL + sourceSHA256 + LF"
}
CODEX_RC_TARGET_ID = "codex-20261028-rc1"
CODEX_RC_TARGET_RECORD = {
    "client": "codex",
    "id": CODEX_RC_TARGET_ID,
    "qualification": {
        "claudeQualification": "not conferred",
        "effort": "ultra",
        "model": "gpt-6-astra",
        "packagingInstallationQualification": "no native installation or invocation of this artifact observed",
        "releaseQualified": False,
        "route": "native explicit named-skill CLI 0.163.0",
        "scope": "One prospective seven-source BorrowDesk sample: C1-C4 PASS; full non-effective handoff. No inherited historical-case qualification or reliability claim."
    },
    "schema": "das-client-target-v1",
    "selectedSourceMapSHA256": "2084692186f80c00ae9d297d3bbd8dfcda627dcdf39a71bcd1ad92edbd020eca",
    "sourceDigest": "4b3cf50c212aac87f2f788c762d5b1866f336c73c765213f140444c6b2ecd86b",
    "sourceMapAlgorithm": "sorted path + NUL + sourceSHA256 + LF"
}
CODEX_STABLE_TARGET_ID = "codex-0.1.0"
CODEX_STABLE_TARGET_RECORD = {
    "client": "codex",
    "id": CODEX_STABLE_TARGET_ID,
    "qualification": {
        "claudeQualification": "not conferred",
        "effort": "ultra",
        "model": "gpt-6-astra",
        "packagingInstallationQualification": "source behavior and RC1 local routes have separate evidence; verify the final published artifact and its public routes",
        "route": "native explicit named-skill CLI 0.163.0",
        "scope": "Exact RC1 sources: seven-source BorrowDesk, fresh Fieldnote and both E07 phases assessed C1-C4 PASS. E07 includes actual exact approval, local canon publication/readback, separate contract effectivity and current handoff. Scoped samples do not establish reliability, every-skill or all-model correctness."
    },
    "schema": "das-client-target-v1",
    "selectedSourceMapSHA256": "2084692186f80c00ae9d297d3bbd8dfcda627dcdf39a71bcd1ad92edbd020eca",
    "sourceDigest": "4b3cf50c212aac87f2f788c762d5b1866f336c73c765213f140444c6b2ecd86b",
    "sourceMapAlgorithm": "sorted path + NUL + sourceSHA256 + LF"
}
CODEX_TARGETS = {CODEX_TARGET_ID: CODEX_TARGET_RECORD,
                 CODEX_RC_TARGET_ID: CODEX_RC_TARGET_RECORD,
                 CODEX_STABLE_TARGET_ID: CODEX_STABLE_TARGET_RECORD}
TARGET_SUFFIXES = {CODEX_TARGET_ID: "-codex", CODEX_RC_TARGET_ID: "-codex-rc1",
                   CODEX_STABLE_TARGET_ID: ""}
CLAUDE_PLUGIN_FILES = {".claude-plugin/plugin.json", ".claude-plugin/marketplace.json"}
CODEX_PLUGIN_FILES = {".codex-plugin/plugin.json", ".agents/plugins/marketplace.json"}
STABLE_EXCLUDED_FILES = CLAUDE_PLUGIN_FILES | {"docs/claude-code.md", "docs/claude-desktop.md"}
STABLE_EXTRA_FILES = ("docs/release-notes.md", "assets/plugin-icon.svg",
                      "assets/social-preview.png")


def repository_files(names, target):
    """Select only the documented consumer files for this artifact profile."""
    if target == CODEX_STABLE_TARGET_ID:
        return tuple(name for name in names if name not in STABLE_EXCLUDED_FILES) + STABLE_EXTRA_FILES
    return tuple(name for name in names if not target or name not in CLAUDE_PLUGIN_FILES)

LINK = re.compile(r'\]\(([^\s)]+)(?:\s+"[^"\n]*")?\)')


def sha256(data):
    return hashlib.sha256(data).hexdigest()


def plain_path(path):
    raw = Path(path)
    raw = raw if raw.is_absolute() else Path.cwd() / raw
    if any(part.is_symlink() for part in (raw, *raw.parents)):
        raise ValueError("Symlink paths are not accepted: " + str(raw))
    return Path(os.path.abspath(raw))


def relative_name(name):
    path = PurePosixPath(name)
    if not isinstance(name, str) or "\\" in name or path.is_absolute() or not path.parts:
        raise ValueError("Invalid manifest path: " + repr(name))
    if str(path) != name or any(part in (".", "..") for part in path.parts):
        raise ValueError("Invalid manifest path: " + name)
    return name


def walk_files(root, checkout=False):
    result = set()
    for directory, dirs, files in os.walk(root, followlinks=False):
        for name in dirs + files:
            path = Path(directory) / name
            if path.is_symlink():
                raise ValueError("Symlink in package: " + str(path))
            if not (path.is_dir() or path.is_file()):
                raise ValueError("Non-regular package entry: " + str(path))
            if name == ".git":
                if not checkout or Path(directory) != root:
                    raise ValueError("Git metadata is not package payload: " + str(path))
                if name in dirs:
                    dirs.remove(name)
                else:
                    files.remove(name)
        result.update((Path(directory) / name).relative_to(root).as_posix() for name in files)
    return result


def source_digest(records):
    return sha256("".join(
        record["sourcePath"] + "\t" + record["sourceSHA256"] + "\n"
        for record in sorted(records, key=lambda item: item["sourcePath"])
    ).encode("utf-8"))


def validate_source_target(target, digest):
    if target is not None and target not in CODEX_TARGETS:
        raise ValueError("Unknown client target: " + str(target))
    pinned = {record["sourceDigest"] for record in CODEX_TARGETS.values()}
    if ((target is None and digest in pinned)
            or (target is not None and digest != CODEX_TARGETS[target]["sourceDigest"])):
        raise ValueError("Pinned Codex source digest differs or its target label is missing")


def target_from_record(record):
    target = record.get("id") if isinstance(record, dict) else None
    if target not in CODEX_TARGETS or record != CODEX_TARGETS[target]:
        raise ValueError("Codex TARGET.json differs from the fixed target record")
    return target


def check_target(root, manifest):
    target = manifest.get("clientTarget")
    validate_source_target(target, manifest.get("sourceDigest"))
    path = root / "TARGET.json"
    if target is None:
        if path.exists() or path.is_symlink():
            raise ValueError("Target metadata requires an explicit client target")
    elif (not path.is_file() or target_from_record(
            json.loads(plain_path(path).read_text(encoding="utf-8"))) != target):
        raise ValueError("Codex TARGET.json differs from the fixed target record")
    return target


def artifact_label(version, target):
    if target is not None and target not in CODEX_TARGETS:
        raise ValueError("Unknown client target: " + str(target))
    return "design-agent-skills-" + version + (TARGET_SUFFIXES[target] if target else "")


def path_mapping(entry):
    return {
        source: ("SKILL.md" if source == "skills/" + entry + "/SKILL.md"
                 else "related/" + source.split("/")[1] + ".md"
                 if source.startswith("skills/") else source)
        for source in SOURCES
    }


def transform(data, source_path, destinations):
    """Change only local Markdown link path bytes, preserving labels and fragments."""
    text = data.decode("utf-8")
    current = destinations[source_path]

    def replace(match):
        target = match.group(1)
        parts = urllib.parse.urlsplit(target)
        if parts.scheme or parts.netloc or not parts.path:
            return match.group(0)
        source_target = posixpath.normpath(posixpath.join(
            posixpath.dirname(source_path), urllib.parse.unquote(parts.path)))
        if source_target not in destinations:
            raise ValueError("Local link leaves source allowlist: " + source_path + " -> " + target)
        mapped = posixpath.relpath(destinations[source_target], posixpath.dirname(current) or ".")
        suffix = target[len(parts.path):]
        start, end = match.span(1)
        relative_start = start - match.start()
        relative_end = end - match.start()
        return match.group(0)[:relative_start] + mapped + suffix + match.group(0)[relative_end:]

    return LINK.sub(replace, text).encode("utf-8")


def check_links(root, names):
    links = anchors = 0
    for name in sorted(names):
        if not name.endswith(".md"):
            continue
        text = (root / name).read_text(encoding="utf-8")
        targets = [match.group(1) for match in LINK.finditer(text)]
        targets += re.findall(r'<img\b[^>]*?\bsrc=["\']([^"\']+)["\']', text, re.I)
        for target in targets:
            parts = urllib.parse.urlsplit(target)
            if parts.scheme or parts.netloc:
                continue
            if parts.path.startswith("/"):
                raise ValueError("Absolute local link: " + name + " -> " + target)
            destination = posixpath.normpath(posixpath.join(
                posixpath.dirname(name), urllib.parse.unquote(parts.path))) if parts.path else name
            if destination not in names:
                raise ValueError("Broken local link: " + name + " -> " + target)
            links += 1
            if parts.fragment:
                headings = re.findall(r"^#{1,6}\s+(.+?)\s*#*$",
                                      (root / destination).read_text(encoding="utf-8"), re.M)
                slugs = set()
                occurrences = {}
                for heading in headings:
                    slug = re.sub(r"[^\w\- ]", "", heading.lower()).replace(" ", "-")
                    count = occurrences.get(slug, 0)
                    occurrences[slug] = count + 1
                    slugs.add(slug if not count else slug + "-" + str(count))
                if urllib.parse.unquote(parts.fragment) not in slugs:
                    raise ValueError("Broken local anchor: " + name + " -> " + target)
                anchors += 1
    return links, anchors


def check_plugins(root, names, version, target=None):
    all_paths = CLAUDE_PLUGIN_FILES | CODEX_PLUGIN_FILES
    if target in CODEX_TARGETS:
        if CLAUDE_PLUGIN_FILES.intersection(names):
            raise ValueError("Claude plugin metadata is forbidden in the Codex artifact")
        paths = CODEX_PLUGIN_FILES
    else:
        paths = all_paths
    # Source-only fixtures have no consumer documents or native plugin claims.
    if not paths.intersection(names) and "README.md" not in names:
        return
    if not paths.intersection(names) and target is None:
        return
    if not paths.issubset(names):
        raise ValueError("Incomplete plugin metadata")
    if target == CODEX_STABLE_TARGET_ID:
        if STABLE_EXCLUDED_FILES.intersection(names):
            raise ValueError("Other-client files are forbidden in the stable Codex artifact")
        if not set(STABLE_EXTRA_FILES).issubset(names):
            raise ValueError("Stable release documents or media are missing")
    plugin_paths = [".codex-plugin/plugin.json"]
    if target is None:
        plugin_paths.append(".claude-plugin/plugin.json")
    for name in plugin_paths:
        plugin = json.loads((root / name).read_text(encoding="utf-8"))
        if plugin.get("name") != "design-agent-skills" or plugin.get("version") != version:
            raise ValueError("Plugin identity/version differs from package: " + name)
        if plugin.get("license") != "MIT":
            raise ValueError("Plugin license differs from package: " + name)
    codex = json.loads((root / ".codex-plugin/plugin.json").read_text(encoding="utf-8"))
    if codex.get("skills") != "./skills/":
        raise ValueError("Codex plugin must point to the installed skills directory")
    if target == CODEX_STABLE_TARGET_ID:
        interface = codex.get("interface", {})
        for field in ("logo", "composerIcon"):
            path = interface.get(field) if isinstance(interface, dict) else None
            if not isinstance(path, str) or not path.startswith("./") or path[2:] not in names:
                raise ValueError("Stable plugin media must resolve inside the package: " + field)
            if not 0 < (root / path[2:]).stat().st_size <= 5 * 1024 * 1024:
                raise ValueError("Stable plugin media must be nonempty and at most 5 MiB: " + field)
    if target is None:
        claude = json.loads((root / ".claude-plugin/marketplace.json").read_text(encoding="utf-8"))
        if (claude.get("name") != "design-agent-skills" or len(claude.get("plugins", [])) != 1
                or claude["plugins"][0].get("name") != "design-agent-skills"
                or claude["plugins"][0].get("source") != "./"):
            raise ValueError("Claude marketplace must resolve this repository's plugin")
    catalog = json.loads((root / ".agents/plugins/marketplace.json").read_text(encoding="utf-8"))
    entries = catalog.get("plugins", [])
    if (catalog.get("name") != "design-agent-skills" or len(entries) != 1
            or entries[0].get("name") != "design-agent-skills"
            or entries[0].get("source") != {"source": "local", "path": "./"}):
        raise ValueError("Codex marketplace must resolve this repository's plugin")


def check(root, source_root=None, checkout=False):
    root = plain_path(root)
    manifest = json.loads((root / "MANIFEST.json").read_text(encoding="utf-8"))
    if manifest.get("schema") != "das-portable-v1":
        raise ValueError("Unsupported manifest schema")
    target = check_target(root, manifest)
    records = manifest["files"]
    expected = {relative_name(record["path"]): record for record in records}
    if len(records) != len(expected) or "MANIFEST.json" in expected:
        raise ValueError("Duplicate or recursive manifest file record")
    actual = walk_files(root, checkout=checkout)
    if actual != set(expected) | {"MANIFEST.json"}:
        raise ValueError("Unexpected/missing files: " + repr(sorted(actual ^ (set(expected) | {"MANIFEST.json"}))))
    for name, record in expected.items():
        data = (root / name).read_bytes()
        if len(data) != record["bytes"] or sha256(data) != record["sha256"]:
            raise ValueError("Changed payload: " + name)
    if (root / "VERSION").read_text(encoding="utf-8") != manifest["version"] + "\n":
        raise ValueError("VERSION does not match manifest")

    kind = manifest["kind"]
    if kind == "skill":
        entry = manifest["entrypoint"]
        if entry not in SKILLS:
            raise ValueError("Unknown entrypoint")
        mapping = path_mapping(entry)
        source_records = manifest["sources"]
        sources = {record["sourcePath"]: record for record in source_records}
        if len(source_records) != 28 or set(sources) != set(SOURCES):
            raise ValueError("Expected exact 28-source closure")
        layout = set(mapping.values()) | {"verify.py", "VERSION"}
        if "LICENSE" in expected:
            layout.add("LICENSE")
        if target:
            layout.add("TARGET.json")
        if set(expected) != layout:
            raise ValueError("Unexpected skill closure layout")
        if manifest["sourceDigest"] != source_digest(source_records):
            raise ValueError("Source digest mismatch")
        inverse = {value: key for key, value in mapping.items()}
        for source, destination in mapping.items():
            record = sources[source]
            if record["exportPath"] != destination:
                raise ValueError("Incorrect export mapping: " + source)
            exported = (root / destination).read_bytes()
            restored = transform(exported, destination, inverse)
            if sha256(exported) != record["exportSHA256"] or sha256(restored) != record["sourceSHA256"]:
                raise ValueError("Source/export reproduction failed: " + source)
            if source_root is not None:
                original = plain_path(plain_path(source_root) / source).read_bytes()
                if restored != original:
                    raise ValueError("Inverse transform differs from canonical input: " + source)
            if source.startswith("skills/"):
                match = re.match(rb"---\nname: ([^\n]+)\ndescription: ([^\n]+)\n---", exported)
                if not match or match[1].decode("utf-8") != source.split("/")[1]:
                    raise ValueError("Invalid skill frontmatter: " + destination)
        links, anchors = check_links(root, actual)
        return {"status": "pass", "kind": kind, "version": manifest["version"],
                "entrypoint": entry, "sourceDigest": manifest["sourceDigest"],
                "files": len(actual), "sources": 28, "localLinks": links,
                "anchors": anchors, "inverseReproductions": 28,
                "canonicalCompared": source_root is not None, "clientTarget": target}
    if (kind != "bundle" or manifest["entrypoints"] != list(SKILLS)
            or manifest["sourceFiles"] != list(SOURCES)):
        raise ValueError("Unknown bundle kind or entrypoints")
    discovered = sorted(name for name in actual if name.endswith("/SKILL.md"))
    if discovered != sorted("skills/" + entry + "/SKILL.md" for entry in SKILLS):
        raise ValueError("Expected exactly 16 discoverable SKILL.md files")
    check_plugins(root, actual, manifest["version"], target)
    results = [check(root / "skills" / entry, source_root) for entry in SKILLS]
    if any(result["clientTarget"] != target for result in results):
        raise ValueError("Mixed client targets in bundle")
    if target and any((root / "skills" / entry / "TARGET.json").read_bytes()
                      != (root / "TARGET.json").read_bytes() for entry in SKILLS):
        raise ValueError("Mixed target records in bundle")
    if "LICENSE" in actual:
        license_bytes = (root / "LICENSE").read_bytes()
        for entry in SKILLS:
            license_path = root / "skills" / entry / "LICENSE"
            if not license_path.is_file() or license_path.read_bytes() != license_bytes:
                raise ValueError("Licensed bundle requires the same LICENSE in every skill: " + entry)
    if any(result["sourceDigest"] != manifest["sourceDigest"] for result in results):
        raise ValueError("Mixed source closures in bundle")
    if any(result["version"] != manifest["version"] for result in results):
        raise ValueError("Mixed versions in bundle")
    shared = {name for name in actual if name.startswith("references/")}
    if shared:
        if shared != {"references/" + name + ".md" for name in REFERENCES}:
            raise ValueError("Unexpected shared reference layout")
        first_skill = json.loads((root / "skills" / SKILLS[0] / "MANIFEST.json").read_text(encoding="utf-8"))
        source_hashes = {record["sourcePath"]: record["sourceSHA256"] for record in first_skill["sources"]}
        if any(sha256((root / name).read_bytes()) != source_hashes[name] for name in shared):
            raise ValueError("Shared references differ from installed skill sources")
    links, anchors = check_links(root, actual)
    return {"status": "pass", "kind": kind, "version": manifest["version"],
            "files": len(actual), "skills": 16, "sourcesPerSkill": 28,
            "sourceDigest": manifest["sourceDigest"], "localLinks": links,
            "anchors": anchors, "inverseReproductions": 448,
            "canonicalCompared": source_root is not None, "clientTarget": target}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).parent)
    parser.add_argument("--source-root", type=Path,
                        help="Optionally compare inverse-transformed bytes with the original source corpus")
    parser.add_argument("--checkout", action="store_true",
                        help="Ignore only the root .git directory or regular file; verify all package payload normally")
    args = parser.parse_args()
    try:
        result = check(args.root, args.source_root, checkout=args.checkout)
    except (OSError, ValueError, KeyError, TypeError) as error:
        parser.exit(1, "Verification failed: " + str(error) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
