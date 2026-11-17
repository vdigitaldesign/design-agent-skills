#!/usr/bin/env python3
"""Verify a DAS Claude package or one installed skill; Python 3.9+."""

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

CLAUDE_RELEASE_TARGET_ID = "claude-0.1.7"

CLAUDE_RELEASE_TARGET_RECORD = {
    "client": "claude",
    "id": CLAUDE_RELEASE_TARGET_ID,
    "schema": "das-client-target-v1",
    "selectedSourceMapSHA256": "b977729fbe959a4afde06928f5ac2b65434d52c7e5384342f5e97b97346c978c",
    "sourceDigest": "42a0c38897b8ab97e806724a1d42ae930092be7430a5417c4d6b62c03cf43388",
    "sourceMapAlgorithm": "SHA-256 of UTF-8 json.dumps(files, sort_keys=True, separators=(',', ':'))",
}

CLAUDE_PLUGIN_FILES = {".claude-plugin/plugin.json", ".claude-plugin/marketplace.json"}

CODEX_PLUGIN_FILES = {".codex-plugin/plugin.json", ".agents/plugins/marketplace.json"}

CLAUDE_RELEASE_EXTRA_FILES = ("assets/plugin-icon.svg", "assets/social-preview.png")

CLAUDE_RELEASE_REPOSITORY_FILES = {
    "README.md", "INSTALL.md", "LICENSE", "CHANGELOG.md", "CONTRIBUTING.md", "AGENTS.md",
    "SUPPORT.md", "SECURITY.md", "docs/claude-code.md", "docs/skills.md",
    "docs/how-das-works.md", "docs/advanced-installation.md", "scripts/manage.py",
    "tests/test_repository.py", ".gitignore", "VERSION", "verify.py",
    "assets/design-agent-skills-hero.svg",
} | CLAUDE_PLUGIN_FILES

LINK = re.compile(r'\]\(([^\s)]+)(?:\s+"[^"\n]*")?\)')

CLAUDE_TARGETS = {CLAUDE_RELEASE_TARGET_ID: CLAUDE_RELEASE_TARGET_RECORD}

CLIENT_TARGETS = CLAUDE_TARGETS

CODEX_TARGETS = {}

CODEX_STABLE_TARGET_IDS = set()

TARGET_SUFFIXES = {}

CLAUDE_SOURCES = ('references/audit-exploration-templates.md',
 'references/authority-and-status.md',
 'references/contract-review-templates.md',
 'references/design-knowledge-index.md',
 'references/design-lab-protocol.md',
 'references/design-system-craft.md',
 'references/engineering-integration.md',
 'references/executable-acceptance.md',
 'references/native-design-delivery.md',
 'references/packet-projections.md',
 'references/product-profile-and-tools.md',
 'references/quality-checklists.md',
 'references/task-context-templates.md',
 'references/visual-craft.md',
 'skills/assess-design-reuse/SKILL.md',
 'skills/audit-design-surface/SKILL.md',
 'skills/audit-design-system/SKILL.md',
 'skills/design-router/SKILL.md',
 'skills/develop-visual-direction/SKILL.md',
 'skills/evolve-design-system/SKILL.md',
 'skills/explore-design-directions/SKILL.md',
 'skills/frame-design-task/SKILL.md',
 'skills/maintain-design-knowledge/SKILL.md',
 'skills/prototype-design-directions/SKILL.md',
 'skills/publish-design-system-canon/SKILL.md',
 'skills/reconstruct-design-context/SKILL.md',
 'skills/record-design-decision/SKILL.md',
 'skills/validate-design-contract/SKILL.md',
 'skills/verify-design-implementation/SKILL.md',
 'skills/write-design-contract/SKILL.md',
 'skills/write-design-contract/references/source-version-reading.md')


def repository_files(names, target):
    """Select the public files carried by this Claude edition."""
    if target != CLAUDE_RELEASE_TARGET_ID:
        raise ValueError("Unknown client target: " + str(target))
    return tuple(name for name in names if name in CLAUDE_RELEASE_REPOSITORY_FILES) + CLAUDE_RELEASE_EXTRA_FILES


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
    if target is not None and target not in CLIENT_TARGETS:
        raise ValueError("Unknown client target: " + str(target))
    pinned = {record["sourceDigest"] for record in CLIENT_TARGETS.values()}
    if ((target is None and digest in pinned)
            or (target is not None and digest != CLIENT_TARGETS[target]["sourceDigest"])):
        client = "Claude" if target in CLAUDE_TARGETS else "Codex"
        raise ValueError("Pinned " + client + " source digest differs or its target label is missing")


def target_from_record(record):
    target = record.get("id") if isinstance(record, dict) else None
    if target not in CLIENT_TARGETS or record != CLIENT_TARGETS[target]:
        raise ValueError("TARGET.json differs from the fixed target record")
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
        raise ValueError("TARGET.json differs from the fixed target record")
    return target


def artifact_label(version, target):
    if target is not None and target not in CLIENT_TARGETS:
        raise ValueError("Unknown client target: " + str(target))
    if target == CLAUDE_RELEASE_TARGET_ID:
        return "design-agent-skills-claude-" + version
    return "design-agent-skills-" + version + (TARGET_SUFFIXES[target] if target else "")


def sources_for_target(target=None):
    if target is not None and target not in CLIENT_TARGETS:
        raise ValueError("Unknown client target: " + str(target))
    return CLAUDE_SOURCES if target in CLAUDE_TARGETS else SOURCES


def is_entrypoint(source):
    return source in {"skills/" + entry + "/SKILL.md" for entry in SKILLS}


def path_mapping(entry, target=None):
    if entry not in SKILLS:
        raise ValueError("Unknown entrypoint: " + str(entry))
    mapping = {}
    for source in sources_for_target(target):
        if source.startswith("skills/"):
            _, owner, local = source.split("/", 2)
            if owner == entry:
                destination = local
            elif is_entrypoint(source):
                destination = "related/" + owner + ".md"
            else:
                destination = "related/" + owner + "/" + local
        else:
            destination = source
        mapping[source] = destination
    if len(set(mapping.values())) != len(mapping):
        raise ValueError("Source export destination collision")
    return mapping


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
    if CODEX_PLUGIN_FILES.intersection(names):
        raise ValueError("Codex plugin metadata is forbidden in the Claude package")
    if not CLAUDE_PLUGIN_FILES.intersection(names) and "README.md" not in names:
        return
    required = {"README.md", "INSTALL.md", "CHANGELOG.md", "assets/design-agent-skills-hero.svg",
                *CLAUDE_RELEASE_EXTRA_FILES}
    if not required.issubset(names):
        raise ValueError("Claude release documents or media are missing")
    if not CLAUDE_PLUGIN_FILES.issubset(names):
        raise ValueError("Incomplete Claude plugin metadata")
    plugin = json.loads((root / ".claude-plugin/plugin.json").read_text(encoding="utf-8"))
    if plugin.get("name") != "design-agent-skills" or plugin.get("version") != version:
        raise ValueError("Claude plugin identity/version differs from package")
    if plugin.get("license") != "MIT":
        raise ValueError("Plugin license differs from package")
    if plugin.get("icon") != "./assets/plugin-icon.svg":
        raise ValueError("Claude release icon must point to the supplied DAS artwork")
    marketplace = json.loads((root / ".claude-plugin/marketplace.json").read_text(encoding="utf-8"))
    entries = marketplace.get("plugins", [])
    if (marketplace.get("name") != "design-agent-skills" or len(entries) != 1
            or entries[0].get("name") != "design-agent-skills" or entries[0].get("source") != "./"):
        raise ValueError("Claude marketplace must resolve this repository's plugin")


def check(root, source_root=None, checkout=False):
    root = plain_path(root)
    manifest = json.loads((root / "MANIFEST.json").read_text(encoding="utf-8"))
    if manifest.get("schema") != "das-portable-v1":
        raise ValueError("Unsupported manifest schema")
    target = check_target(root, manifest)
    source_paths = sources_for_target(target)
    source_count = len(source_paths)
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
        mapping = path_mapping(entry, target)
        source_records = manifest["sources"]
        sources = {record["sourcePath"]: record for record in source_records}
        if len(source_records) != source_count or set(sources) != set(source_paths):
            raise ValueError("Expected exact " + str(source_count) + "-source closure")
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
            if is_entrypoint(source):
                match = re.match(rb"---\nname: ([^\n]+)\ndescription: ([^\n]+)\n---", exported)
                if not match or match[1].decode("utf-8") != source.split("/")[1]:
                    raise ValueError("Invalid skill frontmatter: " + destination)
        links, anchors = check_links(root, actual)
        return {"status": "pass", "kind": kind, "version": manifest["version"],
                "entrypoint": entry, "sourceDigest": manifest["sourceDigest"],
                "files": len(actual), "sources": source_count, "localLinks": links,
                "anchors": anchors, "inverseReproductions": source_count,
                "canonicalCompared": source_root is not None, "clientTarget": target}
    if (kind != "bundle" or manifest["entrypoints"] != list(SKILLS)
            or manifest["sourceFiles"] != list(source_paths)):
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
        if shared != {name for name in source_paths if name.startswith("references/")}:
            raise ValueError("Unexpected shared reference layout")
        first_skill = json.loads((root / "skills" / SKILLS[0] / "MANIFEST.json").read_text(encoding="utf-8"))
        source_hashes = {record["sourcePath"]: record["sourceSHA256"] for record in first_skill["sources"]}
        if any(sha256((root / name).read_bytes()) != source_hashes[name] for name in shared):
            raise ValueError("Shared references differ from installed skill sources")
    links, anchors = check_links(root, actual)
    return {"status": "pass", "kind": kind, "version": manifest["version"],
            "files": len(actual), "skills": 16, "sourcesPerSkill": source_count,
            "sourceDigest": manifest["sourceDigest"], "localLinks": links,
            "anchors": anchors, "inverseReproductions": len(SKILLS) * source_count,
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
