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
            subprocess.run([
                "git", "commit",
                "-m", "fix auth token refresh regression",
                "-m", "Problem: /users/{uid} lookup failed before token refresh.\nCo-Authored-By: Claude <noreply@example.com>",
            ], cwd=repo, check=True, capture_output=True)
            out = self.run_cli("--registry", str(reg), "scan-git", str(repo)).stdout
            self.assertIn("wrote", out)
            pending = json.loads(self.run_cli("--registry", str(reg), "pending", "--json").stdout)
            self.assertTrue(pending)
            self.assertIn("auth", pending[0]["tags"])
            self.assertEqual(pending[0]["source"]["files"], ["auth_config.py"])

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

    def test_excavate_groups_fix_commit_with_context_and_evidence(self):
        with tempfile.TemporaryDirectory() as td:
            repo = Path(td) / "repo"
            reg = Path(td) / "registry"
            report = Path(td) / "excavate.md"
            repo.mkdir()
            subprocess.run(["git", "init"], cwd=repo, check=True, capture_output=True)
            subprocess.run(["git", "config", "user.email", "t@example.com"], cwd=repo, check=True)
            subprocess.run(["git", "config", "user.name", "t"], cwd=repo, check=True)
            (repo / "mobile_auth.ts").write_text("export const status='broken'\n")
            subprocess.run(["git", "add", "."], cwd=repo, check=True)
            subprocess.run(["git", "commit", "-m", "feat auth bootstrap"], cwd=repo, check=True, capture_output=True)
            (repo / "mobile_auth.ts").write_text("export const status='fixed'\n")
            subprocess.run(["git", "add", "."], cwd=repo, check=True)
            subprocess.run(["git", "commit", "-m", "fix auth bootstrap login regression"], cwd=repo, check=True, capture_output=True)

            out = self.run_cli("--registry", str(reg), "excavate", str(repo), "--out", str(report)).stdout
            self.assertIn("excavation report", out)
            text = report.read_text()
            self.assertIn("# Betavibe Forensic Excavation Report", text)
            self.assertIn("fix auth bootstrap login regression", text)
            pending = json.loads(self.run_cli("--registry", str(reg), "pending", "--json").stdout)
            self.assertTrue(pending)
            self.assertEqual(pending[0]["source"]["kind"], "forensic_git_cluster")
            self.assertIn("evidence", pending[0]["draft"])

    def test_doctor_explains_gbrain_optional_layer(self):
        with tempfile.TemporaryDirectory() as td:
            reg = Path(td) / "registry"
            out = self.run_cli("--registry", str(reg), "doctor").stdout
            self.assertIn("Betavibe doctor", out)
            self.assertIn("cross-harness source of truth", out)
            self.assertIn("semantic layer", out)

    def test_sync_commits_registry_changes(self):
        with tempfile.TemporaryDirectory() as td:
            repo = Path(td) / "repo"
            reg = repo / ".betavibe" / "registry"
            repo.mkdir()
            subprocess.run(["git", "init"], cwd=repo, check=True, capture_output=True)
            subprocess.run(["git", "config", "user.email", "t@example.com"], cwd=repo, check=True)
            subprocess.run(["git", "config", "user.name", "t"], cwd=repo, check=True)
            (repo / "README.md").write_text("repo\n")
            subprocess.run(["git", "add", "."], cwd=repo, check=True)
            subprocess.run(["git", "commit", "-m", "init"], cwd=repo, check=True, capture_output=True)
            self.run_cli("--registry", str(reg), "capture",
                "--type", "pitfall",
                "--title", "Auth bootstrap needs cold-start test",
                "--summary", "Auth bootstrap can regress on cold start.",
                "--tags", "auth",
                "--tech", "node",
                "--symptom", "Login loops on cold start.",
                "--root-cause", "Session restore and user doc loading diverged.",
                "--fix", "Add cold-start auth test.",
                "--prevention-signal", "Before changing auth bootstrap, run cold-start login test.",
                "--verify-trigger", "When auth bootstrap changes.")
            out = self.run_cli("--registry", str(reg), "sync", "--repo", str(repo)).stdout
            self.assertIn("committed registry changes", out)
            log = subprocess.run(["git", "log", "--oneline", "-1"], cwd=repo, text=True, capture_output=True, check=True).stdout
            self.assertIn("sync reviewed insights", log)

if __name__ == "__main__":
    unittest.main()
