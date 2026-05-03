from __future__ import annotations

from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from betavibe.registry import resolve_registry


class RegistryResolutionTests(unittest.TestCase):
    def test_default_prefers_nearest_project_betavibe_registry_from_vendored_pack(self):
        with tempfile.TemporaryDirectory() as td:
            project = Path(td) / "project"
            pack = project / "vendor" / "Betalpha-vibe-coding-partner"
            pack.mkdir(parents=True)
            (project / ".betavibe").mkdir()

            with patch("pathlib.Path.cwd", return_value=pack):
                self.assertEqual(resolve_registry(), project / ".betavibe" / "registry")

    def test_explicit_registry_still_wins(self):
        with tempfile.TemporaryDirectory() as td:
            explicit = Path(td) / "custom-registry"
            self.assertEqual(resolve_registry(explicit), explicit)

    def test_env_registry_wins_over_project_discovery(self):
        with tempfile.TemporaryDirectory() as td:
            project = Path(td) / "project"
            project.mkdir()
            (project / ".betavibe").mkdir()
            env_registry = Path(td) / "env-registry"
            with patch.dict("os.environ", {"BETAVIBE_REGISTRY": str(env_registry)}), patch("pathlib.Path.cwd", return_value=project):
                self.assertEqual(resolve_registry(), env_registry)


if __name__ == "__main__":
    unittest.main()
