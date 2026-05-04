import json
import subprocess
import sys
import tempfile
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


VALID_SPEC = """# Spec: Valid

## Task

Ship a change.

## Relevant Betavibe Insights

No relevant local insight.

## Spec Guardrails

- Keep verification explicit.

## Implementation Plan

- Edit the target files.

## Verification Plan

- Run unit tests.
"""


class SpecFlowTest(unittest.TestCase):
    def run_cli(self, *args, cwd=ROOT, check=True):
        return subprocess.run([sys.executable, "-m", "betavibe", *args], cwd=cwd, text=True, capture_output=True, check=check)

    def test_spec_start_generates_required_sections_and_implement_start_accepts(self):
        with tempfile.TemporaryDirectory() as td:
            reg = Path(td) / "registry"
            spec = Path(td) / "specs" / "demo.md"
            out = self.run_cli("--registry", str(reg), "spec-start", "--task", "demo task", "--context", "resolver output", "--out", str(spec)).stdout
            self.assertIn("spec started", out)
            text = spec.read_text()
            for section in ["Task", "Relevant Betavibe Insights", "Spec Guardrails", "Implementation Plan", "Verification Plan"]:
                self.assertIn(f"## {section}", text)
            self.assertEqual(self.run_cli("--registry", str(reg), "spec-validate", str(spec)).returncode, 0)
            self.assertIn("implementation may start", self.run_cli("--registry", str(reg), "implement-start", "--spec", str(spec)).stdout)

    def test_spec_validate_is_accurate_on_ten_handcrafted_specs(self):
        with tempfile.TemporaryDirectory() as td:
            reg = Path(td) / "registry"
            root = Path(td) / "specs"
            root.mkdir()
            valid_paths = []
            invalid_paths = []
            for idx in range(5):
                path = root / f"valid-{idx}.md"
                path.write_text(VALID_SPEC.replace("Ship a change.", f"Ship change {idx}."), encoding="utf-8")
                valid_paths.append(path)
            invalid_bodies = [
                VALID_SPEC.replace("## Task\n\nShip a change.\n\n", ""),
                VALID_SPEC.replace("## Verification Plan\n\n- Run unit tests.\n", ""),
                VALID_SPEC.replace("## Spec Guardrails\n\n- Keep verification explicit.\n", "## Spec Guardrails\n\n"),
                "# Spec: Empty\n",
                VALID_SPEC.replace("## Implementation Plan\n\n- Edit the target files.\n", "## Implementation Plan\n\n"),
            ]
            for idx, body in enumerate(invalid_bodies):
                path = root / f"invalid-{idx}.md"
                path.write_text(body, encoding="utf-8")
                invalid_paths.append(path)
            for path in valid_paths:
                self.assertEqual(self.run_cli("--registry", str(reg), "spec-validate", str(path)).returncode, 0, path.read_text())
            for path in invalid_paths:
                proc = self.run_cli("--registry", str(reg), "spec-validate", str(path), check=False)
                self.assertNotEqual(proc.returncode, 0, path.read_text())

    def test_compliance_sessions_meet_g1_rate(self):
        out = self.run_cli("spec-validate", "--compliance-dir", str(ROOT / "tests" / "compliance_sessions"), "--json").stdout
        data = json.loads(out)
        self.assertEqual(data["sessions"], 5)
        self.assertEqual(data["specs_written"], 5)
        self.assertEqual(data["spec_start_called"], 4)
        self.assertGreaterEqual(data["compliance_rate"], 0.8)

    def test_pre_commit_hook_blocks_invalid_staged_spec(self):
        with tempfile.TemporaryDirectory() as td:
            repo = Path(td) / "repo"
            reg = repo / ".betavibe" / "registry"
            repo.mkdir()
            subprocess.run(["git", "init"], cwd=repo, check=True, capture_output=True)
            subprocess.run(["git", "config", "user.email", "t@example.com"], cwd=repo, check=True)
            subprocess.run(["git", "config", "user.name", "t"], cwd=repo, check=True)
            pack = repo / "Betalpha-vibe-coding-partner"
            subprocess.run(["cp", "-R", str(ROOT), str(pack)], check=True)
            self.run_cli("--registry", str(reg), "install", "--project", str(repo), "--pack-path", "Betalpha-vibe-coding-partner", "--enforce-runtime")
            specs = repo / "specs"
            specs.mkdir()
            bad = specs / "bad.md"
            bad.write_text("# Spec: Bad\n\n## Task\n\nMissing required sections.\n", encoding="utf-8")
            subprocess.run(["git", "add", "specs/bad.md"], cwd=repo, check=True)
            blocked = subprocess.run(["git", "commit", "-m", "add invalid spec"], cwd=repo, text=True, capture_output=True)
            self.assertNotEqual(blocked.returncode, 0)
            self.assertIn("staged spec is missing required sections", blocked.stderr + blocked.stdout)


if __name__ == "__main__":
    unittest.main()
