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

    def test_install_agent_contract_is_idempotent(self):
        with tempfile.TemporaryDirectory() as td:
            project = Path(td) / "client-project"
            project.mkdir()
            self.run_cli("install-agent-contract", "--project", str(project))
            first = (project / "AGENTS.md").read_text()
            self.run_cli("install-agent-contract", "--project", str(project))
            second = (project / "AGENTS.md").read_text()
            self.assertEqual(first, second)

if __name__ == "__main__":
    unittest.main()
