import json
import subprocess
import sys
import tempfile
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class AcceptanceDemoTest(unittest.TestCase):
    def test_acceptance_demo_proves_fail_pass_learn_promote_and_recall(self):
        with tempfile.TemporaryDirectory() as td:
            project = Path(td) / "acceptance-project"
            report = Path(td) / "acceptance-report.md"
            proc = subprocess.run(
                [sys.executable, "-m", "betavibe", "acceptance-demo", str(project), "--out", str(report)],
                cwd=ROOT,
                text=True,
                capture_output=True,
                check=True,
            )
            self.assertIn("acceptance demo report", proc.stdout)
            self.assertTrue(report.exists())
            text = report.read_text(encoding="utf-8")
            self.assertIn("# Betavibe Acceptance Demo Report", text)
            self.assertIn("status: PASS", text)
            self.assertIn("failed command evidence: yes", text)
            self.assertIn("passing verification after failure: yes", text)
            self.assertIn("simulated human approval", text)
            self.assertIn("Spec guardrails", text)
            self.assertIn("Known wrong paths", text)
            self.assertIn("Verification requirements", text)
            self.assertIn(".codex/AGENTS.md", text)
            self.assertIn("CLAUDE.md", text)
            self.assertIn("openclaw", text.lower())

            registry = project / ".betavibe" / "registry"
            runs = list((registry / "runs").glob("*/events.jsonl"))
            self.assertTrue(runs)
            events = [json.loads(line) for line in runs[0].read_text(encoding="utf-8").splitlines() if line.strip()]
            commands = [e for e in events if e.get("kind") == "command"]
            self.assertTrue(any(not c.get("ok") for c in commands))
            self.assertTrue(any(c.get("ok") for c in commands))

            pending_artifacts = list((project / ".betavibe" / "reports").rglob("pending-runtime-lesson.json"))
            self.assertTrue(pending_artifacts)
            pending = json.loads(pending_artifacts[0].read_text(encoding="utf-8"))
            self.assertEqual(pending["source"]["kind"], "runtime")
            self.assertIn("failed command evidence", pending["reasons"])
            self.assertIn("passing verification", pending["reasons"])

            self.assertFalse(list((registry / "pending").glob("*.json")), "promote should remove pending from registry after the pending artifact is preserved")
            insights = list((registry / "insights").rglob("INSIGHT.md"))
            self.assertTrue(insights)
            insight_text = insights[0].read_text(encoding="utf-8")
            self.assertIn("## Symptom", insight_text)
            self.assertIn("## Wrong Paths", insight_text)
            self.assertIn("## Fix", insight_text)
            self.assertIn("## Evidence", insight_text)

            pre_spec = list((project / ".betavibe" / "reports").rglob("pre_spec.txt"))[0].read_text(encoding="utf-8")
            pre_impl = list((project / ".betavibe" / "reports").rglob("pre_implement.txt"))[0].read_text(encoding="utf-8")
            self.assertIn("# Spec-ready synthesis", pre_spec)
            self.assertIn("## Spec guardrails", pre_spec)
            self.assertIn("# Spec-ready synthesis", pre_impl)
            self.assertIn("Commands that failed", pre_impl)


if __name__ == "__main__":
    unittest.main()
