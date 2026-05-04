import subprocess
import sys
import tempfile
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]

class InstallContractTest(unittest.TestCase):
    def run_cli(self, *args):
        return subprocess.run([sys.executable, "-m", "betavibe", *args], cwd=ROOT, text=True, capture_output=True, check=True)

    def test_install_agent_contract_writes_root_instruction_files(self):
        with tempfile.TemporaryDirectory() as td:
            project = Path(td) / "client-project"
            project.mkdir()
            self.run_cli("install-agent-contract", "--project", str(project), "--pack-path", "tools/betavibe")
            for rel in ["AGENTS.md", "CLAUDE.md", ".codex/AGENTS.md", ".claude/CLAUDE.md"]:
                text = (project / rel).read_text()
                self.assertIn("BETAVIBE_AGENT_CONTRACT_START", text)
                self.assertIn("resolve pre_spec", text)
                self.assertIn("should-capture", text)
                self.assertIn("tools/betavibe", text)
                self.assertIn("--registry ../../.betavibe/registry", text)
                self.assertIn("--cwd ../.. --repo ../..", text)

    def test_install_agent_contract_is_idempotent(self):
        with tempfile.TemporaryDirectory() as td:
            project = Path(td) / "client-project"
            project.mkdir()
            self.run_cli("install-agent-contract", "--project", str(project))
            first = (project / "AGENTS.md").read_text()
            self.run_cli("install-agent-contract", "--project", str(project))
            second = (project / "AGENTS.md").read_text()
            self.assertEqual(first, second)

    def test_full_install_adds_contract_skill_hooks_and_selftest_passes(self):
        with tempfile.TemporaryDirectory() as td:
            project = Path(td) / "client-project"
            project.mkdir()
            out = self.run_cli("--registry", str(project / "registry"), "install", "--project", str(project), "--pack-path", "tools/betavibe", "--self-test").stdout
            self.assertIn("Betavibe install self-test passed", out)
            for rel in [
                "AGENTS.md",
                "CLAUDE.md",
                ".codex/AGENTS.md",
                ".claude/CLAUDE.md",
                "skills/betavibe-insight/SKILL.md",
                ".claude/skills/betavibe-insight/SKILL.md",
                ".betavibe/hooks/pre_spec.sh",
                ".betavibe/hooks/pre_implement.sh",
                ".betavibe/hooks/should_capture.sh",
                ".betavibe/hooks/verify.sh",
                ".betavibe/hooks/learn.sh",
            ]:
                self.assertTrue((project / rel).exists(), rel)
            hook = (project / ".betavibe/hooks/pre_implement.sh").read_text()
            self.assertIn('--registry "$PROJECT_ROOT/.betavibe/registry"', hook)
            verify_hook = (project / ".betavibe/hooks/verify.sh").read_text()
            self.assertIn('verify --cwd "$PROJECT_ROOT" --repo "$PROJECT_ROOT"', verify_hook)
            learn_hook = (project / ".betavibe/hooks/learn.sh").read_text()
            self.assertIn('learn "$@"', learn_hook)

if __name__ == "__main__":
    unittest.main()
