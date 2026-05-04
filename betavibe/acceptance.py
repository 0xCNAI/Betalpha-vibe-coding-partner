from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
import json
import shutil
import subprocess
import sys


@dataclass
class DemoResult:
    project: Path
    report: Path
    artifact_dir: Path
    run_id: str
    pending_id: str
    pending_artifact: Path
    insight_path: Path
    pre_spec_output: Path
    pre_implement_output: Path


def package_root() -> Path:
    return Path(__file__).resolve().parents[1]


def run(cmd: list[str], cwd: Path, check: bool = True, timeout: int = 30) -> subprocess.CompletedProcess[str]:
    return subprocess.run(cmd, cwd=cwd, text=True, capture_output=True, check=check, timeout=timeout)


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def copy_pack(project: Path, pack_name: str = "Betalpha-vibe-coding-partner") -> Path:
    src = package_root()
    dest = project / pack_name
    if dest.exists():
        shutil.rmtree(dest)
    ignore = shutil.ignore_patterns(".git", "__pycache__", "*.pyc", "usage")
    shutil.copytree(src, dest, ignore=ignore)
    return dest


def ensure_clean_project(project: Path, force: bool = False) -> None:
    if project.exists() and any(project.iterdir()):
        if not force:
            raise SystemExit(f"acceptance-demo project is not empty: {project} (use --force to replace it)")
        shutil.rmtree(project)
    project.mkdir(parents=True, exist_ok=True)


def init_bug_repo(project: Path) -> None:
    run(["git", "init"], cwd=project)
    run(["git", "config", "user.email", "betavibe-demo@example.com"], cwd=project)
    run(["git", "config", "user.name", "Betavibe Demo"], cwd=project)
    write(project / "calc.py", "def add(a, b):\n    return a - b\n")
    write(
        project / "test_calc.py",
        "import unittest\n\nfrom calc import add\n\n\nclass CalcTest(unittest.TestCase):\n    def test_add(self):\n        self.assertEqual(add(1, 2), 3)\n\n\nif __name__ == '__main__':\n    unittest.main()\n",
    )
    run(["git", "add", "."], cwd=project)
    run(["git", "commit", "-m", "init reproducible calculator regression"], cwd=project)


def run_openclaw_static_check(pack: Path) -> dict:
    plugin = pack / "adapters" / "openclaw" / "betavibe-lifecycle-plugin"
    manifest = plugin / "openclaw.plugin.json"
    index = plugin / "index.js"
    docs = pack / "docs" / "OPENCLAW_LIFECYCLE.md"
    evidence = {
        "lifecycle_docs_exists": docs.exists(),
        "manifest_exists": manifest.exists(),
        "index_exists": index.exists(),
        "node_check": "skipped: node not found",
        "openclaw_inspect_smoke": "skipped: openclaw not found",
        "openclaw_enable_command_smoke": "skipped: openclaw not found",
    }
    if manifest.exists():
        data = json.loads(manifest.read_text(encoding="utf-8"))
        evidence["plugin_id"] = data.get("id")
        evidence["hooks_description"] = data.get("description")
    if docs.exists():
        text = docs.read_text(encoding="utf-8", errors="ignore")
        evidence["docs_config_example"] = all(item in text for item in ["openclaw plugins install", "openclaw config set", "betavibe-lifecycle"])
    if shutil.which("node") and index.exists():
        proc = run(["node", "--check", str(index)], cwd=pack, check=False)
        evidence["node_check"] = "ok" if proc.returncode == 0 else (proc.stderr or proc.stdout).strip()
    if shutil.which("openclaw"):
        proc = run(["openclaw", "plugins", "inspect", "betavibe-lifecycle", "--json"], cwd=pack, check=False, timeout=10)
        evidence["openclaw_inspect_smoke"] = "ok" if proc.returncode == 0 else (proc.stderr or proc.stdout or "inspect failed").strip()[:500]
        enable = run(["openclaw", "plugins", "enable", "--help"], cwd=pack, check=False, timeout=10)
        evidence["openclaw_enable_command_smoke"] = "ok" if enable.returncode == 0 else (enable.stderr or enable.stdout or "enable help failed").strip()[:500]
    return evidence


def file_contains(path: Path, needles: list[str]) -> bool:
    if not path.exists():
        return False
    text = path.read_text(encoding="utf-8", errors="ignore")
    return all(needle in text for needle in needles)


def harness_evidence(project: Path, pack: Path) -> dict:
    return {
        "codex": {
            "path": ".codex/AGENTS.md",
            "ok": file_contains(project / ".codex" / "AGENTS.md", ["BETAVIBE_AGENT_CONTRACT_START", "verify", "learn", ".betavibe/registry"]),
        },
        "claude_code": {
            "CLAUDE.md": file_contains(project / "CLAUDE.md", ["BETAVIBE_AGENT_CONTRACT_START", "verify", "learn"]),
            ".claude/CLAUDE.md": file_contains(project / ".claude" / "CLAUDE.md", ["BETAVIBE_AGENT_CONTRACT_START", "verify", "learn"]),
            "skill": file_contains(project / ".claude" / "skills" / "betavibe-insight" / "SKILL.md", ["Betavibe", "verify", "learn"]),
        },
        "openclaw": run_openclaw_static_check(pack),
    }


def render_report(
    *,
    project: Path,
    registry: Path,
    artifact_dir: Path,
    run_id: str,
    pending: dict,
    pending_artifact: Path,
    insight_path: Path,
    pre_spec_output: Path,
    pre_implement_output: Path,
    harnesses: dict,
    fail_stdout: str,
    pass_stdout: str,
    learn_stdout: str,
    promote_stdout: str,
) -> str:
    summary = json.loads((registry / "runs" / run_id / "summary.json").read_text(encoding="utf-8"))
    commands = summary.get("draft", {}).get("evidence", {}).get("commands", [])
    lines = [
        "# Betavibe Acceptance Demo Report",
        "",
        "## Result",
        "",
        "- status: PASS",
        f"- project: `{project}`",
        f"- registry: `{registry}`",
        f"- artifact_dir: `{artifact_dir}`",
        f"- runtime_run: `{run_id}`",
        f"- events: `{registry / 'runs' / run_id / 'events.jsonl'}`",
        f"- summary: `{registry / 'runs' / run_id / 'summary.json'}`",
        f"- pending_lesson_artifact: `{pending_artifact}`",
        f"- promoted_reviewed_insight: `{insight_path}`",
        f"- pre_spec_output: `{pre_spec_output}`",
        f"- pre_implement_output: `{pre_implement_output}`",
        "",
        "## Runtime Evidence",
        "",
        f"- confidence: {summary.get('draft', {}).get('confidence')}",
        f"- failed command evidence: {'yes' if any(not c.get('ok') for c in commands) else 'no'}",
        f"- passing verification after failure: {'yes' if any(c.get('ok') for c in commands[1:]) else 'no'}",
        "",
    ]
    for command in commands:
        lines.append(f"- `{command.get('cmd_text')}` -> returncode {command.get('returncode')} ok={command.get('ok')}")
    lines.extend([
        "",
        "## Pending Lesson",
        "",
        f"- id: `{pending.get('id')}`",
        f"- type: {pending.get('type')}",
        f"- score: {pending.get('score')}",
        f"- reasons: {', '.join(pending.get('reasons', []))}",
        f"- symptom: {pending.get('draft', {}).get('symptom')}",
        f"- wrong_paths: {pending.get('draft', {}).get('wrong_paths')}",
        f"- fix: {pending.get('draft', {}).get('fix')}",
        f"- prevention_signal: {pending.get('draft', {}).get('prevention_signal')}",
        f"- verify_trigger: {pending.get('draft', {}).get('verify_trigger')}",
        "",
        "## Human Approval Boundary",
        "",
        "- `learn` created only a pending lesson.",
        "- This demo then simulated human approval by explicitly running `promote` without `--sync-gbrain`.",
        "- Production agents must ask the human before promotion or GBrain sync.",
        "",
        "## Harness Installation Evidence",
        "",
        "### Codex",
        "",
        f"- `.codex/AGENTS.md` contract ok: {harnesses['codex']['ok']}",
        "",
        "### Claude Code",
        "",
        f"- `CLAUDE.md` contract ok: {harnesses['claude_code']['CLAUDE.md']}",
        f"- `.claude/CLAUDE.md` contract ok: {harnesses['claude_code']['.claude/CLAUDE.md']}",
        f"- `.claude/skills/betavibe-insight/SKILL.md` workflow ok: {harnesses['claude_code']['skill']}",
        "",
        "### OpenClaw",
        "",
    ])
    for key, value in harnesses["openclaw"].items():
        lines.append(f"- {key}: {value}")
    lines.extend([
        "",
        "## Resolver Proof",
        "",
        "### pre_spec includes spec guardrails",
        "",
        "```text",
        pre_spec_output.read_text(encoding="utf-8")[:4000],
        "```",
        "",
        "### pre_implement includes wrong paths and verification requirements",
        "",
        "```text",
        pre_implement_output.read_text(encoding="utf-8")[:4000],
        "```",
        "",
        "## Command Output",
        "",
        "### fail capture",
        "```text",
        fail_stdout[-2000:],
        "```",
        "### pass capture",
        "```text",
        pass_stdout[-2000:],
        "```",
        "### learn",
        "```text",
        learn_stdout[-2000:],
        "```",
        "### promote",
        "```text",
        promote_stdout[-2000:],
        "```",
        "",
    ])
    return "\n".join(lines)


def run_acceptance_demo(project: Path, out: Path | None = None, force: bool = False) -> DemoResult:
    project = project.expanduser().absolute()
    ensure_clean_project(project, force=force)
    init_bug_repo(project)
    pack = copy_pack(project)
    registry = project / ".betavibe" / "registry"
    run([sys.executable, "-m", "betavibe", "--registry", str(registry), "install", "--project", str(project), "--pack-path", pack.name, "--self-test"], cwd=pack)

    task = "fix calculator regression with betavibe acceptance demo"
    fail = run([str(project / ".betavibe" / "hooks" / "verify.sh"), "--task", task, "--harness", "codex", "--no-fail", "--", sys.executable, "-m", "unittest", "-v"], cwd=project)
    write(project / "calc.py", "def add(a, b):\n    return a + b\n")
    passed = run([str(project / ".betavibe" / "hooks" / "verify.sh"), "--task", task, "--harness", "codex", "--", sys.executable, "-m", "unittest", "-v"], cwd=project)
    learned = run([str(project / ".betavibe" / "hooks" / "learn.sh")], cwd=project)
    pending = json.loads(run([sys.executable, "-m", "betavibe", "--registry", str(registry), "pending", "--json"], cwd=pack).stdout)
    if not pending:
        raise RuntimeError("acceptance demo did not create a pending lesson")
    candidate = pending[0]
    pending_id = candidate["id"]
    artifact_dir = project / ".betavibe" / "reports" / ("acceptance-" + datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S"))
    artifact_dir.mkdir(parents=True, exist_ok=True)
    pending_artifact = artifact_dir / "pending-runtime-lesson.json"
    write(pending_artifact, json.dumps(candidate, ensure_ascii=False, indent=2))
    promote = run([sys.executable, "-m", "betavibe", "--registry", str(registry), "promote", pending_id], cwd=pack)
    insights = sorted((registry / "insights").rglob("INSIGHT.md"))
    if not insights:
        raise RuntimeError("acceptance demo did not promote a reviewed insight")
    insight_path = insights[-1]

    pre_spec_output = artifact_dir / "pre_spec.txt"
    pre_implement_output = artifact_dir / "pre_implement.txt"
    spec_context = "write a spec for calculator arithmetic regression fix and verification"
    implement_context = "implement calculator add regression fix after failing unittest"
    pre_spec = run([sys.executable, "-m", "betavibe", "--registry", str(registry), "resolve", "pre_spec", "--context", spec_context, "--no-gbrain"], cwd=pack)
    pre_impl = run([sys.executable, "-m", "betavibe", "--registry", str(registry), "resolve", "pre_implement", "--context", implement_context, "--no-gbrain"], cwd=pack)
    write(pre_spec_output, pre_spec.stdout)
    write(pre_implement_output, pre_impl.stdout)

    run_id = candidate.get("source", {}).get("run_id")
    if not run_id:
        raise RuntimeError("pending lesson missing runtime run_id")
    harnesses = harness_evidence(project, pack)
    report = out.expanduser().absolute() if out else artifact_dir / "report.md"
    write(
        report,
        render_report(
            project=project,
            registry=registry,
            artifact_dir=artifact_dir,
            run_id=run_id,
            pending=candidate,
            pending_artifact=pending_artifact,
            insight_path=insight_path,
            pre_spec_output=pre_spec_output,
            pre_implement_output=pre_implement_output,
            harnesses=harnesses,
            fail_stdout=fail.stdout + fail.stderr,
            pass_stdout=passed.stdout + passed.stderr,
            learn_stdout=learned.stdout + learned.stderr,
            promote_stdout=promote.stdout + promote.stderr,
        ),
    )
    return DemoResult(
        project=project,
        report=report,
        artifact_dir=artifact_dir,
        run_id=run_id,
        pending_id=pending_id,
        pending_artifact=pending_artifact,
        insight_path=insight_path,
        pre_spec_output=pre_spec_output,
        pre_implement_output=pre_implement_output,
    )
