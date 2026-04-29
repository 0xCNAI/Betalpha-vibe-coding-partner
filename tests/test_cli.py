import json
import subprocess
import sys
import tempfile
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]

class CliTest(unittest.TestCase):
    def run_cli(self, *args, cwd=ROOT):
        return subprocess.run([sys.executable, "-m", "betavibe", *args], cwd=cwd, text=True, capture_output=True, check=True)

    def test_capture_and_advise_token_search(self):
        with tempfile.TemporaryDirectory() as td:
            reg = Path(td) / "registry"
            self.run_cli("--registry", str(reg), "init")
            self.run_cli(
                "--registry", str(reg), "capture",
                "--type", "pitfall",
                "--title", "LINE OAuth token refresh silently kills webhook",
                "--summary", "LINE OAuth refresh token rotation caused webhook delivery to silently stop until explicit revalidation was added.",
                "--tags", "oauth,line-bot,webhook",
                "--tech", "node,line",
                "--symptom", "Webhook stopped receiving events after token rotation.",
                "--root-cause", "Refresh flow updated credentials without revalidating webhook delivery.",
                "--fix", "Add webhook self-test after token refresh.",
                "--prevention-signal", "Before deploying any LINE OAuth refresh flow, add or run webhook delivery self-test.",
                "--verify-trigger", "When LINE Messaging API auth behavior changes.",
            )
            out = self.run_cli("--registry", str(reg), "advise", "oauth line bot").stdout
            self.assertIn("LINE OAuth", out)
            self.assertIn("prevention_signal", out)

    def test_scan_git_creates_pending(self):
        with tempfile.TemporaryDirectory() as td:
            repo = Path(td) / "repo"
            reg = Path(td) / "registry"
            repo.mkdir()
            subprocess.run(["git", "init"], cwd=repo, check=True, capture_output=True)
            subprocess.run(["git", "config", "user.email", "t@example.com"], cwd=repo, check=True)
            subprocess.run(["git", "config", "user.name", "t"], cwd=repo, check=True)
            (repo / "auth_config.py").write_text("token='x'\n")
            subprocess.run(["git", "add", "."], cwd=repo, check=True)
            subprocess.run(["git", "commit", "-m", "fix auth token refresh regression"], cwd=repo, check=True, capture_output=True)
            out = self.run_cli("--registry", str(reg), "scan-git", str(repo)).stdout
            self.assertIn("wrote", out)
            pending = json.loads(self.run_cli("--registry", str(reg), "pending", "--json").stdout)
            self.assertTrue(pending)
            self.assertIn("auth", pending[0]["tags"])

    def test_dogfood_writes_report_and_pending_without_github_or_gbrain(self):
        with tempfile.TemporaryDirectory() as td:
            repo = Path(td) / "repo"
            reg = Path(td) / "registry"
            report = Path(td) / "dogfood.md"
            repo.mkdir()
            subprocess.run(["git", "init"], cwd=repo, check=True, capture_output=True)
            subprocess.run(["git", "config", "user.email", "t@example.com"], cwd=repo, check=True)
            subprocess.run(["git", "config", "user.name", "t"], cwd=repo, check=True)
            (repo / "schema_migration.py").write_text("print('v1')\n")
            subprocess.run(["git", "add", "."], cwd=repo, check=True)
            subprocess.run(["git", "commit", "-m", "fix database schema migration rollback"], cwd=repo, check=True, capture_output=True)

            out = self.run_cli("--registry", str(reg), "dogfood", str(repo), "--out", str(report)).stdout
            self.assertIn("dogfood report", out)
            self.assertTrue(report.exists())
            text = report.read_text()
            self.assertIn("# Betavibe Dogfood Report", text)
            self.assertIn("## Resolver probes", text)
            self.assertIn("pre_spec", text)
            self.assertIn("pre_implement", text)
            self.assertIn("fix database schema migration rollback", text)
            pending = json.loads(self.run_cli("--registry", str(reg), "pending", "--json").stdout)
            self.assertTrue(pending)
            self.assertIn("schema", pending[0]["tags"])

if __name__ == "__main__":
    unittest.main()
