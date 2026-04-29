import subprocess
import sys
import tempfile
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]

class HybridResolverTest(unittest.TestCase):
    def run_cli(self, *args):
        return subprocess.run([sys.executable, "-m", "betavibe", *args], cwd=ROOT, text=True, capture_output=True, check=True)

    def test_resolve_outputs_spec_ready_sections_even_without_hits(self):
        with tempfile.TemporaryDirectory() as td:
            reg = Path(td) / "registry"
            self.run_cli("--registry", str(reg), "init")
            out = self.run_cli("--registry", str(reg), "resolve", "pre_spec", "--context", "unknown new integration", "--no-gbrain").stdout
            self.assertIn("# Spec-ready synthesis", out)
            self.assertIn("## Spec guardrails", out)
            self.assertIn("## Known wrong paths", out)
            self.assertIn("## Tools to prefer / avoid", out)
            self.assertIn("## Verification requirements", out)

    def test_capture_accepts_sync_gbrain_flag_without_gbrain_requirement(self):
        with tempfile.TemporaryDirectory() as td:
            reg = Path(td) / "registry"
            self.run_cli("--registry", str(reg), "init")
            out = self.run_cli(
                "--registry", str(reg), "capture",
                "--type", "pitfall",
                "--title", "Webhook token refresh requires delivery self-test",
                "--summary", "Webhook token refresh can appear successful while delivery is broken, so deployment needs an explicit self-test gate.",
                "--tags", "webhook,token,deploy",
                "--tech", "python",
                "--symptom", "Delivery stopped after token refresh.",
                "--root-cause", "Credential update was not equivalent to end-to-end delivery validation.",
                "--fix", "Run delivery self-test and fail deploy if callback is not observed.",
                "--prevention-signal", "Before deploying webhook token refresh code, run an end-to-end delivery self-test.",
                "--verify-trigger", "When webhook provider delivery/auth behavior changes.",
                "--sync-gbrain",
            ).stdout
            self.assertIn("wrote insight", out)

if __name__ == "__main__":
    unittest.main()
