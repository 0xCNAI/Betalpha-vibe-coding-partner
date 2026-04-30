import json
import os
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

    def test_runtime_capture_records_failed_then_passing_command(self):
        with tempfile.TemporaryDirectory() as td:
            repo = Path(td) / "repo"
            reg = repo / ".betavibe" / "registry"
            repo.mkdir()
            subprocess.run(["git", "init"], cwd=repo, check=True, capture_output=True)
            subprocess.run(["git", "config", "user.email", "t@example.com"], cwd=repo, check=True)
            subprocess.run(["git", "config", "user.name", "t"], cwd=repo, check=True)
            run_id = self.run_cli("--registry", str(reg), "run-start", "--task", "fix runtime capture command evidence", "--harness", "openclaw", "--repo", str(repo)).stdout.strip()
            self.run_cli("--registry", str(reg), "run-exec", run_id, "--cwd", str(repo), "--no-fail", "--", sys.executable, "-c", "import sys; print('boom'); sys.exit(2)")
            self.run_cli("--registry", str(reg), "run-exec", run_id, "--cwd", str(repo), "--", sys.executable, "-c", "print('ok')")
            draft = json.loads(self.run_cli("--registry", str(reg), "run-finish", run_id, "--repo", str(repo), "--json").stdout)
            self.assertEqual(draft["confidence"], "high")
            self.assertIn("Command failed", draft["symptom"])
            self.assertIn("Final captured verification passed", draft["fix"])
            self.assertEqual(len(draft["evidence"]["commands"]), 2)

    def test_runtime_capture_includes_files_changed_between_start_and_finish_commits(self):
        with tempfile.TemporaryDirectory() as td:
            repo = Path(td) / "repo"
            reg = repo / ".betavibe" / "registry"
            repo.mkdir()
            subprocess.run(["git", "init"], cwd=repo, check=True, capture_output=True)
            subprocess.run(["git", "config", "user.email", "t@example.com"], cwd=repo, check=True)
            subprocess.run(["git", "config", "user.name", "t"], cwd=repo, check=True)
            (repo / "calc.py").write_text("def add(a, b):\n    return a - b\n")
            subprocess.run(["git", "add", "."], cwd=repo, check=True)
            subprocess.run(["git", "commit", "-m", "init broken calc"], cwd=repo, check=True, capture_output=True)
            run_id = self.run_cli("--registry", str(reg), "run-start", "--task", "fix arithmetic regression", "--harness", "openclaw", "--repo", str(repo)).stdout.strip()
            (repo / "calc.py").write_text("def add(a, b):\n    return a + b\n")
            subprocess.run(["git", "add", "."], cwd=repo, check=True)
            subprocess.run(["git", "commit", "-m", "fix calc"], cwd=repo, check=True, capture_output=True)
            draft = json.loads(self.run_cli("--registry", str(reg), "run-finish", run_id, "--repo", str(repo), "--json").stdout)
            self.assertIn("calc.py", draft["evidence"]["changed_files"])

    def test_enforce_blocks_commit_without_runtime_capture_then_allows_with_evidence(self):
        with tempfile.TemporaryDirectory() as td:
            repo = Path(td) / "repo"
            reg = repo / ".betavibe" / "registry"
            repo.mkdir()
            subprocess.run(["git", "init"], cwd=repo, check=True, capture_output=True)
            subprocess.run(["git", "config", "user.email", "t@example.com"], cwd=repo, check=True)
            subprocess.run(["git", "config", "user.name", "t"], cwd=repo, check=True)
            (repo / "README.md").write_text("init\n")
            subprocess.run(["git", "add", "."], cwd=repo, check=True)
            subprocess.run(["git", "commit", "-m", "init"], cwd=repo, check=True, capture_output=True)

            pack = repo / "Betalpha-vibe-coding-partner"
            subprocess.run(["cp", "-R", str(ROOT), str(pack)], check=True)
            self.run_cli("--registry", str(reg), "install", "--project", str(repo), "--pack-path", "Betalpha-vibe-coding-partner", "--enforce-runtime")

            (repo / "feature.py").write_text("x=1\n")
            subprocess.run(["git", "add", "feature.py"], cwd=repo, check=True)
            blocked = subprocess.run(["git", "commit", "-m", "feature without capture"], cwd=repo, text=True, capture_output=True)
            self.assertNotEqual(blocked.returncode, 0)
            self.assertIn("Betavibe blocked this commit", blocked.stderr + blocked.stdout)

            run_id = self.run_cli("--registry", str(reg), "run-start", "--task", "add feature", "--harness", "codex", "--repo", str(repo)).stdout.strip()
            self.run_cli("--registry", str(reg), "run-exec", run_id, "--cwd", str(repo), "--", sys.executable, "-c", "print('ok')")
            allowed = subprocess.run(["git", "commit", "-m", "add feature"], cwd=repo, text=True, capture_output=True)
            self.assertEqual(allowed.returncode, 0, allowed.stderr + allowed.stdout)

    def test_bugfix_commit_message_requires_failed_and_passing_evidence(self):
        with tempfile.TemporaryDirectory() as td:
            repo = Path(td) / "repo"
            reg = repo / ".betavibe" / "registry"
            repo.mkdir()
            subprocess.run(["git", "init"], cwd=repo, check=True, capture_output=True)
            subprocess.run(["git", "config", "user.email", "t@example.com"], cwd=repo, check=True)
            subprocess.run(["git", "config", "user.name", "t"], cwd=repo, check=True)
            (repo / "README.md").write_text("init\n")
            subprocess.run(["git", "add", "."], cwd=repo, check=True)
            subprocess.run(["git", "commit", "-m", "init"], cwd=repo, check=True, capture_output=True)
            pack = repo / "Betalpha-vibe-coding-partner"
            subprocess.run(["cp", "-R", str(ROOT), str(pack)], check=True)
            self.run_cli("--registry", str(reg), "install", "--project", str(repo), "--pack-path", "Betalpha-vibe-coding-partner", "--enforce-runtime")

            (repo / "bug.py").write_text("fixed = True\n")
            subprocess.run(["git", "add", "bug.py"], cwd=repo, check=True)
            run_id = self.run_cli("--registry", str(reg), "run-start", "--task", "fix bug", "--harness", "codex", "--repo", str(repo)).stdout.strip()
            self.run_cli("--registry", str(reg), "run-exec", run_id, "--cwd", str(repo), "--", sys.executable, "-c", "print('ok')")
            blocked = subprocess.run(["git", "commit", "-m", "fix failing bug"], cwd=repo, text=True, capture_output=True)
            self.assertNotEqual(blocked.returncode, 0)
            self.assertIn("no failed-command evidence", blocked.stderr + blocked.stdout)

            run_id = self.run_cli("--registry", str(reg), "run-start", "--task", "fix bug with evidence", "--harness", "codex", "--repo", str(repo)).stdout.strip()
            self.run_cli("--registry", str(reg), "run-exec", run_id, "--cwd", str(repo), "--no-fail", "--", sys.executable, "-c", "import sys; sys.exit(2)")
            self.run_cli("--registry", str(reg), "run-exec", run_id, "--cwd", str(repo), "--", sys.executable, "-c", "print('ok')")
            allowed = subprocess.run(["git", "commit", "-m", "fix failing bug"], cwd=repo, text=True, capture_output=True)
            self.assertEqual(allowed.returncode, 0, allowed.stderr + allowed.stdout)

    def test_install_writes_gbrain_status_file(self):
        with tempfile.TemporaryDirectory() as td:
            repo = Path(td) / "repo"
            reg = repo / ".betavibe" / "registry"
            repo.mkdir()
            subprocess.run(["git", "init"], cwd=repo, check=True, capture_output=True)
            pack = repo / "Betalpha-vibe-coding-partner"
            subprocess.run(["cp", "-R", str(ROOT), str(pack)], check=True)
            self.run_cli("--registry", str(reg), "install", "--project", str(repo), "--pack-path", "Betalpha-vibe-coding-partner")
            status = repo / ".betavibe" / "GBRAIN_STATUS.md"
            self.assertTrue(status.exists())
            text = status.read_text()
            self.assertIn("GBrain is the optional semantic recall layer", text)
            self.assertIn("Agents must not silently assume GBrain is available", text)

    def test_verify_reuses_task_run_and_learn_creates_pending_for_high_confidence(self):
        with tempfile.TemporaryDirectory() as td:
            repo = Path(td) / "repo"
            reg = Path(td) / "registry"
            repo.mkdir()
            subprocess.run(["git", "init"], cwd=repo, check=True, capture_output=True)
            subprocess.run(["git", "config", "user.email", "t@example.com"], cwd=repo, check=True)
            subprocess.run(["git", "config", "user.name", "t"], cwd=repo, check=True)
            (repo / "calc.py").write_text("def add(a,b): return a-b\n")
            subprocess.run(["git", "add", "."], cwd=repo, check=True)
            subprocess.run(["git", "commit", "-m", "init broken calc"], cwd=repo, check=True, capture_output=True)
            fail = self.run_cli("--registry", str(reg), "verify", "--task", "fix calc bug", "--repo", str(repo), "--cwd", str(repo), "--no-fail", "--", sys.executable, "-c", "import sys; sys.exit(3)")
            self.assertIn("Betavibe verify captured run", fail.stdout)
            run_id = [line for line in fail.stdout.splitlines() if "Betavibe verify captured run" in line][0].split(": ", 1)[1]
            (repo / "calc.py").write_text("def add(a,b): return a+b\n")
            ok = self.run_cli("--registry", str(reg), "verify", "--task", "fix calc bug", "--repo", str(repo), "--cwd", str(repo), "--", sys.executable, "-c", "print('ok')")
            self.assertIn(run_id, ok.stdout)
            summary = json.loads((reg / "runs" / run_id / "summary.json").read_text())
            self.assertEqual(summary["draft"]["confidence"], "high")
            self.assertIn("calc.py", summary["draft"]["evidence"]["changed_files"])
            learned = self.run_cli("--registry", str(reg), "learn").stdout
            self.assertIn("Created pending reusable lesson", learned)
            pending = json.loads(self.run_cli("--registry", str(reg), "pending", "--json").stdout)
            self.assertTrue(pending)
            self.assertEqual(pending[0]["source"]["run_id"], run_id)

    def test_learn_noops_for_pass_only_run(self):
        with tempfile.TemporaryDirectory() as td:
            reg = Path(td) / "registry"
            self.run_cli("--registry", str(reg), "verify", "--task", "add feature", "--cwd", str(ROOT), "--", sys.executable, "-c", "print('ok')")
            out = self.run_cli("--registry", str(reg), "learn", "--allow-noop").stdout
            self.assertIn("not strong enough", out)
            self.assertIn("--force-pending", out)

    def test_learn_force_pending_preserves_human_confirmed_pass_only_run(self):
        with tempfile.TemporaryDirectory() as td:
            reg = Path(td) / "registry"
            captured = self.run_cli("--registry", str(reg), "verify", "--task", "ops debug lesson observed outside wrapper", "--cwd", str(ROOT), "--", sys.executable, "-c", "print('ok')").stdout
            run_id = [line for line in captured.splitlines() if "Betavibe verify captured run" in line][0].split(": ", 1)[1]
            out = self.run_cli("--registry", str(reg), "learn", "--force-pending").stdout
            self.assertIn("Created pending reusable lesson", out)
            pending = json.loads(self.run_cli("--registry", str(reg), "pending", "--json").stdout)
            self.assertEqual(pending[0]["source"]["run_id"], run_id)
            self.assertIn("human-requested weak runtime draft", pending[0]["reasons"])
            self.assertEqual(pending[0]["score"], 5)

    def test_recall_logs_usage_and_metrics_reports_cold_start(self):
        with tempfile.TemporaryDirectory() as td:
            reg = Path(td) / "registry"
            self.run_cli("--registry", str(reg), "init")
            self.run_cli("--registry", str(reg), "recall", "fix auth deploy bug", "--no-gbrain")
            usage = reg.parent / "usage" / "resolver_events.jsonl"
            self.assertTrue(usage.exists())
            rows = [json.loads(line) for line in usage.read_text().splitlines() if line.strip()]
            self.assertEqual(rows[-1]["phase"], "pre_implement")
            out = self.run_cli("--registry", str(reg), "metrics").stdout
            self.assertIn("resolver_calls: 1", out)
            self.assertIn("Cold-start note", out)

    def test_journal_logs_misses_and_metrics_counts_them(self):
        with tempfile.TemporaryDirectory() as td:
            reg = Path(td) / "registry"
            self.run_cli("--registry", str(reg), "journal", "--task", "fix gateway sessions", "--miss", "sessions.list payload cap should have existed", "--wrong-path", "looked at Discord reconnect first")
            out = self.run_cli("--registry", str(reg), "metrics", "--json").stdout
            metrics = json.loads(out)
            self.assertEqual(metrics["journal_entries"], 1)
            self.assertEqual(metrics["journal_misses"], 1)
            self.assertEqual(metrics["journal_wrong_paths"], 1)

    def test_excavate_adaptive_topic_from_openclaw_style_paths(self):
        from betavibe.excavate import _topic
        topic = _topic({"subject": "fix session list timeout", "body": "", "files": ["packages/gateway/src/sessions/store.ts", "packages/browser/src/mcp/client.ts"]})
        self.assertIn("sessions", topic)
        self.assertNotEqual(topic, "general")

    def test_usage_logs_are_sibling_to_registry_not_inside_registry(self):
        with tempfile.TemporaryDirectory() as td:
            reg = Path(td) / ".betavibe" / "registry"
            self.run_cli("--registry", str(reg), "journal", "--miss", "portable lesson missing")
            self.assertTrue((reg.parent / "usage" / "journal.jsonl").exists())
            self.assertFalse((reg / "usage").exists())

    def test_personal_registry_is_included_in_recall_and_seed_can_copy(self):
        with tempfile.TemporaryDirectory() as td:
            home = Path(td) / "home"
            repo_reg = Path(td) / "repo" / ".betavibe" / "registry"
            personal = home / ".betavibe" / "personal"
            env = {"HOME": str(home), "BETAVIBE_PERSONAL_REGISTRY": str(personal)}
            self.run_cli(
                "--registry", str(personal), "capture",
                "--type", "pitfall",
                "--title", "Argparse remainder swallows run-exec options",
                "--summary", "Python argparse REMAINDER can swallow options after a positional command unless flags are parsed before the remainder.",
                "--tags", "python,cli,argparse",
                "--tech", "python",
                "--symptom", "CLI options passed after a command disappeared into the remainder argument.",
                "--root-cause", "argparse REMAINDER captured later options before command execution saw them.",
                "--fix", "Place parser options before REMAINDER and document -- separator usage.",
                "--prevention-signal", "Before changing Python CLI wrappers that forward commands, check argparse REMAINDER placement.",
                "--verify-trigger", "When adding forwarded command arguments to Python CLIs.",
                cwd=ROOT,
            )
            recall = subprocess.run([sys.executable, "-m", "betavibe", "--registry", str(repo_reg), "recall", "python cli remainder bug", "--no-gbrain"], cwd=ROOT, env={**os.environ, **env}, text=True, capture_output=True, check=True)
            self.assertIn("Argparse remainder", recall.stdout)
            self.assertIn("[portable]", recall.stdout)
            metrics = subprocess.run([sys.executable, "-m", "betavibe", "--registry", str(repo_reg), "metrics", "--json"], cwd=ROOT, env={**os.environ, **env}, text=True, capture_output=True, check=True)
            self.assertEqual(json.loads(metrics.stdout)["resolver_personal_hit_events"], 1)
            seeded = subprocess.run([sys.executable, "-m", "betavibe", "--registry", str(repo_reg), "seed", "--from-personal", "--tags", "python"], cwd=ROOT, env={**os.environ, **env}, text=True, capture_output=True, check=True)
            self.assertIn("seeded 1 insights", seeded.stdout)
            self.assertTrue(list((repo_reg / "insights").rglob("INSIGHT.md")))
            recall_after_seed = subprocess.run([sys.executable, "-m", "betavibe", "--registry", str(repo_reg), "recall", "python cli remainder bug", "--no-gbrain"], cwd=ROOT, env={**os.environ, **env}, text=True, capture_output=True, check=True)
            self.assertEqual(recall_after_seed.stdout.count("## [pitfall]"), 1, recall_after_seed.stdout)
            self.assertNotIn("[portable]", recall_after_seed.stdout)

    def test_install_dry_run_and_minimal_do_not_write_extra_files(self):
        with tempfile.TemporaryDirectory() as td:
            repo = Path(td) / "repo"
            reg = repo / ".betavibe" / "registry"
            repo.mkdir()
            proc = subprocess.run([sys.executable, "-m", "betavibe", "--registry", str(reg), "install", "--project", str(repo), "--pack-path", "vendor/Betalpha-vibe-coding-partner", "--minimal", "--dry-run"], cwd=ROOT, text=True, capture_output=True, check=True)
            self.assertIn("Dry-run diff", proc.stdout)
            self.assertFalse((repo / "AGENTS.md").exists())
            self.assertFalse((repo / ".betavibe").exists())
            self.run_cli("--registry", str(reg), "install", "--project", str(repo), "--pack-path", "vendor/Betalpha-vibe-coding-partner", "--minimal")
            self.assertTrue((repo / "AGENTS.md").exists())
            self.assertFalse((repo / "CLAUDE.md").exists())
            self.assertFalse((repo / ".betavibe" / "hooks").exists())

    def test_uninstall_removes_managed_contract(self):
        with tempfile.TemporaryDirectory() as td:
            repo = Path(td) / "repo"
            reg = repo / ".betavibe" / "registry"
            repo.mkdir()
            self.run_cli("--registry", str(reg), "install", "--project", str(repo), "--pack-path", "vendor/Betalpha-vibe-coding-partner", "--minimal")
            self.assertIn("BETAVIBE_AGENT_CONTRACT_START", (repo / "AGENTS.md").read_text())
            proc = self.run_cli("--registry", str(reg), "uninstall", "--project", str(repo))
            self.assertIn("removed", proc.stdout)
            self.assertNotIn("BETAVIBE_AGENT_CONTRACT_START", (repo / "AGENTS.md").read_text())

    def test_bootstrap_from_git_source_clones_and_installs_minimal(self):
        with tempfile.TemporaryDirectory() as td:
            source = Path(td) / "source"
            project = Path(td) / "project"
            reg = project / ".betavibe" / "registry"
            subprocess.run(["git", "clone", str(ROOT), str(source)], check=True, capture_output=True)
            project.mkdir()
            self.run_cli("--registry", str(reg), "bootstrap", str(source), "--project", str(project), "--minimal")
            self.assertTrue((project / "vendor" / "Betalpha-vibe-coding-partner" / "betavibe").exists())
            self.assertTrue((project / "AGENTS.md").exists())
            self.assertFalse((project / "CLAUDE.md").exists())

    def test_metrics_counts_per_insight_retrievals(self):
        with tempfile.TemporaryDirectory() as td:
            reg = Path(td) / "registry"
            self.run_cli(
                "--registry", str(reg), "capture",
                "--type", "pitfall",
                "--title", "OAuth refresh silently kills webhook",
                "--summary", "OAuth refresh token rotation can silently break webhook delivery unless callback health is revalidated.",
                "--tags", "oauth,webhook",
                "--tech", "node",
                "--symptom", "Webhook stopped receiving events after token refresh.",
                "--root-cause", "Refresh flow updated credentials without revalidating webhook delivery.",
                "--fix", "Run webhook self-test after token refresh and fail deployment on callback errors.",
                "--prevention-signal", "Before changing OAuth refresh logic, run webhook delivery self-test.",
                "--verify-trigger", "When OAuth refresh, webhook auth, or callback URLs change.",
            )
            self.run_cli("--registry", str(reg), "recall", "oauth webhook refresh", "--no-gbrain", "--no-personal")
            self.run_cli("--registry", str(reg), "recall", "webhook oauth callback", "--no-gbrain", "--no-personal")
            metrics = json.loads(self.run_cli("--registry", str(reg), "metrics", "--json").stdout)
            self.assertEqual(metrics["insights_recalled_more_than_once"], 1)
            self.assertEqual(metrics["per_insight_retrieval"][0][1], 2)
            text = self.run_cli("--registry", str(reg), "metrics").stdout
            self.assertIn("Top recalled insights", text)

    def test_auto_profile_detects_ops_workspace_and_skips_extra_harness_files_and_enforcement(self):
        with tempfile.TemporaryDirectory() as td:
            repo = Path(td) / "ops"
            reg = repo / ".betavibe" / "registry"
            repo.mkdir()
            subprocess.run(["git", "init"], cwd=repo, check=True, capture_output=True)
            (repo / "AGENTS.md").write_text("# TinoClaw\n\n- agent_id: tino\n- role: 系統維護 + 私人助理\n")
            pack = repo / "vendor" / "Betalpha-vibe-coding-partner"
            subprocess.run(["mkdir", "-p", str(pack.parent)], check=True)
            subprocess.run(["cp", "-R", str(ROOT), str(pack)], check=True)
            out = self.run_cli("--registry", str(reg), "install", "--project", str(repo), "--pack-path", "vendor/Betalpha-vibe-coding-partner", "--enforce-runtime").stdout
            self.assertIn("profile", out)
            self.assertTrue((repo / "AGENTS.md").exists())
            self.assertFalse((repo / "CLAUDE.md").exists())
            self.assertFalse((repo / ".codex" / "AGENTS.md").exists())
            self.assertFalse((repo / ".git" / "hooks" / "pre-commit").exists())
            self.assertTrue((repo / ".betavibe" / "hooks" / "pre_spec.sh").exists())

    def test_project_profile_keeps_full_harness_install(self):
        with tempfile.TemporaryDirectory() as td:
            repo = Path(td) / "app"
            reg = repo / ".betavibe" / "registry"
            repo.mkdir()
            self.run_cli("--registry", str(reg), "install", "--project", str(repo), "--pack-path", "vendor/Betalpha-vibe-coding-partner", "--profile", "project")
            self.assertTrue((repo / "AGENTS.md").exists())
            self.assertTrue((repo / "CLAUDE.md").exists())
            self.assertTrue((repo / ".codex" / "AGENTS.md").exists())

    def test_promote_sync_gbrain_gracefully_falls_back_when_unavailable(self):
        with tempfile.TemporaryDirectory() as td:
            reg = Path(td) / "registry"
            self.run_cli("--registry", str(reg), "init")
            candidate = {
                "id": "manual-1",
                "title": "OAuth refresh silently kills webhook",
                "type": "pitfall",
                "score": 9,
                "summary": "OAuth refresh token rotation can silently break webhook delivery unless callback health is revalidated.",
                "tags": ["oauth", "webhook"],
                "tech_stack": ["node"],
                "reasons": ["manual test"],
                "source": {"kind": "test"},
                "draft": {
                    "symptom": "Webhook stopped receiving events after token refresh.",
                    "root_cause": "Refresh flow updated credentials without revalidating webhook delivery.",
                    "wrong_paths": "Only checking token refresh success.",
                    "fix": "Run webhook self-test after token refresh.",
                    "prevention_signal": "Before changing OAuth refresh logic, run webhook delivery self-test.",
                    "verify_trigger": "When OAuth refresh, webhook auth, or callback URLs change.",
                    "evidence": "test evidence",
                },
            }
            pending = reg / "pending"
            pending.mkdir(parents=True, exist_ok=True)
            (pending / "manual-1.json").write_text(json.dumps(candidate), encoding="utf-8")
            proc = self.run_cli("--registry", str(reg), "promote", "manual-1", "--sync-gbrain")
            self.assertIn("promoted pending candidate", proc.stdout)
            self.assertTrue(list((reg / "insights").rglob("INSIGHT.md")))
            self.assertFalse((pending / "manual-1.json").exists())

if __name__ == "__main__":
    unittest.main()
