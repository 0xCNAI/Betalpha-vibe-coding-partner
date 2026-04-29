import subprocess
import sys
import tempfile
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]

class ResolverTest(unittest.TestCase):
    def run_cli(self, *args):
        return subprocess.run([sys.executable, "-m", "betavibe", *args], cwd=ROOT, text=True, capture_output=True, check=True)

    def test_should_capture_recommends_only_verified_hard_won_debug(self):
        out = self.run_cli(
            "should-capture",
            "--debug-minutes", "35",
            "--attempts", "3",
            "--had-error-log",
            "--final-fix-verified",
            "--context", "OAuth webhook token refresh bug",
        ).stdout
        self.assertIn("CAPTURE_RECOMMENDED", out)

    def test_should_capture_blocks_unverified(self):
        out = self.run_cli(
            "should-capture",
            "--debug-minutes", "35",
            "--attempts", "3",
            "--had-error-log",
            "--context", "OAuth webhook token refresh bug",
        ).stdout
        self.assertIn("CAPTURE_AFTER_VERIFICATION", out)

    def test_resolve_surfaces_prevention_signal(self):
        with tempfile.TemporaryDirectory() as td:
            reg = Path(td) / "registry"
            self.run_cli("--registry", str(reg), "init")
            self.run_cli(
                "--registry", str(reg), "capture",
                "--type", "spec_guardrail",
                "--title", "OAuth webhook refresh needs delivery self-test",
                "--summary", "Specs for OAuth webhook refresh flows must include a delivery self-test because token rotation can succeed while webhook delivery fails.",
                "--tags", "oauth,webhook,spec",
                "--tech", "node,line",
                "--symptom", "Token refresh looked successful but webhook delivery was broken.",
                "--root-cause", "Spec lacked a post-refresh delivery verification step.",
                "--fix", "Add delivery self-test to spec and CI/deploy gate.",
                "--prevention-signal", "Before writing any OAuth webhook refresh spec, include a delivery self-test gate.",
                "--verify-trigger", "When webhook provider auth or delivery semantics change.",
            )
            out = self.run_cli("--registry", str(reg), "resolve", "pre_spec", "--context", "LINE OAuth webhook refresh").stdout
            self.assertIn("Before writing any OAuth webhook refresh spec", out)
            self.assertIn("Agent instruction", out)

if __name__ == "__main__":
    unittest.main()
