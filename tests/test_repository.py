"""Public repository maintenance checks; run python3 -m unittest discover -s tests -v."""

from pathlib import Path
import json
import runpy
import tempfile
import unittest
import zipfile


ROOT = Path(__file__).absolute().parents[1]
MANAGE = runpy.run_path(str(ROOT / "scripts" / "manage.py"))
VERIFY = runpy.run_path(str(ROOT / "verify.py"))


class RepositoryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        MANAGE["check_repository"](ROOT)
        cls.original = MANAGE["expected_payload"](ROOT)

    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory(prefix="das-public-test-")
        self.addCleanup(self.temporary.cleanup)
        self.area = Path(self.temporary.name).resolve()
        self.root = self.area / "repository"
        MANAGE["write_payload"](self.root, self.original)
        self.target = json.loads((self.root / "MANIFEST.json").read_text()).get("clientTarget")

    def test_source_round_trip_and_exact_entrypoints(self):
        result = MANAGE["check_repository"](self.root, strict=True)
        self.assertEqual(result["skills"], 16)
        self.assertEqual(result["inverseReproductions"], 448)
        self.assertEqual(len(list(self.root.rglob("SKILL.md"))), 16)
        for entry in VERIFY["SKILLS"]:
            for reference in VERIFY["REFERENCES"]:
                name = "references/" + reference + ".md"
                mapping = VERIFY["path_mapping"](entry)
                inverse = {export: source for source, export in mapping.items()}
                portable = (self.root / "skills" / entry / name).read_bytes()
                restored = VERIFY["transform"](portable, name, inverse)
                self.assertEqual(restored, (self.root / name).read_bytes())

    def test_reference_edit_requires_sync_and_updates_every_skill(self):
        reference = "references/" + VERIFY["REFERENCES"][0] + ".md"
        source = self.root / reference
        source.write_bytes(source.read_bytes() + b"\nMaintainer fixture reference.\n")
        manifest_before = (self.root / "MANIFEST.json").read_bytes()
        if self.target:
            with self.assertRaisesRegex(ValueError, "Pinned Codex source digest"):
                MANAGE["sync"](self.root)
            self.assertEqual((self.root / "MANIFEST.json").read_bytes(), manifest_before)
            return
        with self.assertRaisesRegex(ValueError, "Stale generated files"):
            MANAGE["check_repository"](self.root)
        self.assertEqual((self.root / "MANIFEST.json").read_bytes(), manifest_before)
        MANAGE["sync"](self.root)
        MANAGE["check_repository"](self.root)
        for entry in VERIFY["SKILLS"]:
            mapping = VERIFY["path_mapping"](entry)
            expected = VERIFY["transform"](source.read_bytes(), reference, mapping)
            self.assertEqual((self.root / "skills" / entry / reference).read_bytes(), expected)

    def test_skill_edit_propagates_without_rewriting_its_entrypoint(self):
        entry = "design-router"
        path = self.root / "skills" / entry / "SKILL.md"
        edited = path.read_bytes() + b"\nMaintainer fixture instruction.\n"
        path.write_bytes(edited)
        if self.target:
            manifest_before = (self.root / "MANIFEST.json").read_bytes()
            with self.assertRaisesRegex(ValueError, "Pinned Codex source digest"):
                MANAGE["sync"](self.root)
            self.assertEqual(path.read_bytes(), edited)
            self.assertEqual((self.root / "MANIFEST.json").read_bytes(), manifest_before)
            return
        with self.assertRaisesRegex(ValueError, "Stale generated files"):
            MANAGE["check_repository"](self.root)
        MANAGE["sync"](self.root)
        self.assertEqual(path.read_bytes(), edited)
        inverse = {export: source for source, export in VERIFY["path_mapping"](entry).items()}
        original = VERIFY["transform"](edited, "SKILL.md", inverse)
        for other in VERIFY["SKILLS"]:
            mapping = VERIFY["path_mapping"](other)
            source = "skills/" + entry + "/SKILL.md"
            expected = VERIFY["transform"](original, source, mapping)
            self.assertEqual((self.root / "skills" / other / mapping[source]).read_bytes(), expected)
        MANAGE["check_repository"](self.root)

    def test_build_is_self_contained_deterministic_and_excludes_metadata(self):
        metadata = {".idea/workspace.xml": b"local IDE state", ".git/config": b"private git configuration",
                    ".DS_Store": b"local OS state", "tests/__pycache__/unused.pyc": b"cached bytecode"}
        MANAGE["write_payload"](self.root, metadata)
        result = MANAGE["check_repository"](self.root)
        self.assertIn(".idea", result["excludedMetadata"])
        with self.assertRaisesRegex(ValueError, "Unexpected/missing files"):
            MANAGE["check_repository"](self.root, strict=True)
        one = MANAGE["build"](self.root, self.area / "release-one")
        two = MANAGE["build"](self.root, self.area / "release-two")
        self.assertEqual(Path(one["archive"]).read_bytes(), Path(two["archive"]).read_bytes())
        self.assertEqual(one["archiveSHA256"], two["archiveSHA256"])
        label = VERIFY["artifact_label"](one["version"], self.target)
        with zipfile.ZipFile(one["archive"]) as archive:
            expected = {label + "/" + name for name in self.original}
            self.assertEqual(set(archive.namelist()), expected)
            self.assertEqual(sum(name.endswith("/SKILL.md") for name in archive.namelist()), 16)
            self.assertFalse(any(".idea" in name or ".git/" in name for name in archive.namelist()))
            archive.extractall(self.area / "extracted")
        extracted = self.area / "extracted" / label
        self.assertEqual(VERIFY["check"](extracted)["status"], "pass")
        # This second build has only the extracted public files as its input.
        extracted_manage = runpy.run_path(str(extracted / "scripts/manage.py"))
        three = extracted_manage["build"](extracted, self.area / "release-three")
        self.assertEqual(Path(one["archive"]).read_bytes(), Path(three["archive"]).read_bytes())
        for name, data in metadata.items():
            self.assertEqual((self.root / name).read_bytes(), data)

    def test_unlisted_files_are_rejected_instead_of_silently_exported(self):
        (self.root / "private-notes.txt").write_text("Not a release input", encoding="utf-8")
        for operation in (lambda: MANAGE["check_repository"](self.root),
                          lambda: MANAGE["sync"](self.root),
                          lambda: MANAGE["build"](self.root, self.area / "release")):
            with self.assertRaisesRegex(ValueError, "Unexpected"):
                operation()
        self.assertFalse((self.area / "release").exists())

    def test_build_rejects_stale_generated_files_and_in_repository_output(self):
        with self.assertRaisesRegex(ValueError, "outside the repository"):
            MANAGE["build"](self.root, self.root / "dist")
        reference = self.root / "references" / (VERIFY["REFERENCES"][0] + ".md")
        reference.write_bytes(reference.read_bytes() + b"\nUnsynced edit.\n")
        expected = "Pinned Codex source digest" if self.target else "Stale generated files"
        with self.assertRaisesRegex(ValueError, expected):
            MANAGE["build"](self.root, self.area / "release")
        self.assertFalse((self.area / "release").exists())

    def test_rebuild_does_not_overwrite_an_existing_output(self):
        output = self.area / "release"
        first = MANAGE["build"](self.root, output)
        archive = Path(first["archive"]).read_bytes()
        with self.assertRaises(FileExistsError):
            MANAGE["build"](self.root, output)
        self.assertEqual(Path(first["archive"]).read_bytes(), archive)

    def test_version_bump_updates_advertised_plugins_and_standalone_skills(self):
        version_file = self.root / "VERSION"
        current = version_file.read_text(encoding="utf-8").strip()
        major, minor, patch = map(int, current.split("+", 1)[0].split("-", 1)[0].split("."))
        next_version = "{}.{}.{}".format(major, minor, patch + 1)
        version_file.write_text(next_version + "\n", encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "Stale generated files"):
            MANAGE["check_repository"](self.root)
        MANAGE["sync"](self.root)
        result = MANAGE["check_repository"](self.root)
        self.assertEqual(result["version"], next_version)
        for name in (".claude-plugin/plugin.json", ".codex-plugin/plugin.json"):
            if self.target and name in VERIFY["CLAUDE_PLUGIN_FILES"]:
                self.assertFalse((self.root / name).exists())
                continue
            self.assertEqual(json.loads((self.root / name).read_text())["version"], next_version)
        for entry in VERIFY["SKILLS"]:
            self.assertEqual((self.root / "skills" / entry / "VERSION").read_text(), next_version + "\n")

    def test_edition_provenance_and_no_claude_metadata_leak(self):
        manifest = json.loads((self.root / "MANIFEST.json").read_text())
        if self.target:
            self.assertIn(self.target, VERIFY["CODEX_TARGETS"])
            target = (self.root / "TARGET.json").read_bytes()
            self.assertEqual(json.loads(target), VERIFY["CODEX_TARGETS"][self.target])
            for name in VERIFY["CLAUDE_PLUGIN_FILES"]:
                self.assertFalse((self.root / name).exists())
            for entry in VERIFY["SKILLS"]:
                skill = self.root / "skills" / entry
                self.assertEqual((skill / "TARGET.json").read_bytes(), target)
                self.assertEqual(VERIFY["check"](skill)["clientTarget"], self.target)
            if self.target == VERIFY["CODEX_STABLE_TARGET_ID"]:
                for name in VERIFY["STABLE_EXTRA_FILES"]:
                    self.assertTrue((self.root / name).is_file(), name)
                for name in VERIFY["STABLE_EXCLUDED_FILES"]:
                    self.assertFalse((self.root / name).exists(), name)
        else:
            self.assertNotIn("clientTarget", manifest)
            self.assertFalse((self.root / "TARGET.json").exists())
            for name in VERIFY["CLAUDE_PLUGIN_FILES"] | VERIFY["CODEX_PLUGIN_FILES"]:
                self.assertTrue((self.root / name).is_file())

    def test_wrong_plugin_skill_path_fails_before_sync_writes(self):
        path = self.root / ".codex-plugin/plugin.json"
        plugin = json.loads(path.read_text())
        plugin["skills"] = "./private-skills/"
        path.write_text(json.dumps(plugin), encoding="utf-8")
        previous = (self.root / "MANIFEST.json").read_bytes()
        with self.assertRaisesRegex(ValueError, "installed skills directory"):
            MANAGE["sync"](self.root)
        self.assertEqual((self.root / "MANIFEST.json").read_bytes(), previous)

    def test_readme_html_image_must_resolve_to_package_asset(self):
        path = self.root / "README.md"
        path.write_text(path.read_text() + '\n<img src="assets/missing.svg" alt="Missing">\n', encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "Broken local link"):
            MANAGE["sync"](self.root)

    def test_broken_local_links_fail_before_sync_writes(self):
        reference = self.root / "references" / (VERIFY["REFERENCES"][0] + ".md")
        reference.write_bytes(reference.read_bytes() + b"\n[Missing](not-a-reference.md).\n")
        previous = (self.root / "MANIFEST.json").read_bytes()
        expected = "Pinned Codex source digest" if self.target else "allowlist"
        with self.assertRaisesRegex(ValueError, expected):
            MANAGE["sync"](self.root)
        self.assertEqual((self.root / "MANIFEST.json").read_bytes(), previous)


if __name__ == "__main__":
    unittest.main()
