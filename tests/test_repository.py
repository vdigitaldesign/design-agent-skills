import json
from pathlib import Path
import runpy
import shutil
import subprocess
import sys
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
API = runpy.run_path(str(ROOT / "scripts/manage.py"))


class RepositoryTests(unittest.TestCase):
    def test_both_complete_client_packages_and_native_sources(self):
        result = API["check_repository"](ROOT)
        self.assertEqual(result["packages"]["codex"]["sourcesPerSkill"], 28)
        self.assertEqual(result["packages"]["claude"]["sourcesPerSkill"], 31)
        self.assertEqual({v["version"] for v in result["packages"].values()}, {result["version"]})

    def test_wrong_native_client_source_cannot_be_synced(self):
        with tempfile.TemporaryDirectory(prefix="das-wrong-client-") as temporary:
            root = Path(temporary).resolve() / "repository"
            shutil.copytree(ROOT, root, ignore=shutil.ignore_patterns(".git", "__pycache__"))
            path = root / ".claude-plugin/marketplace.json"
            data = json.loads(path.read_text())
            data["plugins"][0]["source"] = "./packages/codex"
            path.write_text(json.dumps(data))
            with self.assertRaisesRegex(ValueError, "Claude marketplace"):
                API["sync"](root)

    def test_client_maintenance_suites(self):
        for client in API["CLIENTS"]:
            result = subprocess.run([sys.executable, "-B", "-m", "unittest", "discover", "-s", "tests", "-v"],
                                    cwd=ROOT / "packages" / client, capture_output=True, text=True)
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)


if __name__ == "__main__":
    unittest.main()
