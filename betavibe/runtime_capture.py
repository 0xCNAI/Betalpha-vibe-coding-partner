from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
import json
import os
import shlex
import subprocess
import uuid


@dataclass
class RunPaths:
    root: Path
    events: Path
    summary: Path


def now() -> str:
    return datetime.now(timezone.utc).isoformat()


def runs_root(registry: Path) -> Path:
    return registry / "runs"


def run_paths(registry: Path, run_id: str) -> RunPaths:
    root = runs_root(registry) / run_id
    return RunPaths(root=root, events=root / "events.jsonl", summary=root / "summary.json")


def append_event(registry: Path, run_id: str, event: dict) -> None:
    paths = run_paths(registry, run_id)
    paths.root.mkdir(parents=True, exist_ok=True)
    event = {"ts": now(), **event}
    with paths.events.open("a", encoding="utf-8") as f:
        f.write(json.dumps(event, ensure_ascii=False) + "\n")


def start_run(registry: Path, task: str, harness: str | None = None, repo: Path | None = None) -> str:
    run_id = datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S") + "-" + uuid.uuid4().hex[:8]
    paths = run_paths(registry, run_id)
    paths.root.mkdir(parents=True, exist_ok=True)
    summary = {
        "id": run_id,
        "task": task,
        "harness": harness or os.environ.get("BETAVIBE_HARNESS") or "unknown",
        "repo": str(repo.resolve()) if repo else None,
        "started_at": now(),
        "status": "running",
    }
    paths.summary.write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
    append_event(registry, run_id, {"kind": "start", "task": task, "harness": summary["harness"], "repo": summary["repo"]})
    return run_id


def read_events(registry: Path, run_id: str) -> list[dict]:
    path = run_paths(registry, run_id).events
    if not path.exists():
        return []
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def command_event(command: list[str], cwd: Path, proc: subprocess.CompletedProcess[str]) -> dict:
    stdout = proc.stdout or ""
    stderr = proc.stderr or ""
    return {
        "kind": "command",
        "cmd": command,
        "cmd_text": shlex.join(command),
        "cwd": str(cwd),
        "returncode": proc.returncode,
        "ok": proc.returncode == 0,
        "stdout_tail": stdout[-4000:],
        "stderr_tail": stderr[-4000:],
    }


def run_command(registry: Path, run_id: str, command: list[str], cwd: Path) -> int:
    proc = subprocess.run(command, cwd=cwd, text=True, capture_output=True)
    append_event(registry, run_id, command_event(command, cwd, proc))
    if proc.stdout:
        print(proc.stdout, end="")
    if proc.stderr:
        print(proc.stderr, end="")
    return proc.returncode


def git_changed_files(repo: Path | None) -> list[str]:
    if not repo or not (repo / ".git").exists():
        return []
    proc = subprocess.run(["git", "status", "--short"], cwd=repo, capture_output=True, text=True, check=False)
    return [line[3:] for line in proc.stdout.splitlines() if line.strip()]


def infer_draft(events: list[dict], task: str, repo: Path | None = None) -> dict:
    commands = [e for e in events if e.get("kind") == "command"]
    failed = [e for e in commands if not e.get("ok")]
    passed_after_failure = []
    seen_failure = False
    for e in commands:
        if not e.get("ok"):
            seen_failure = True
        elif seen_failure:
            passed_after_failure.append(e)
    changed = git_changed_files(repo)
    risky = any(word in task.lower() for word in ["auth", "schema", "migration", "gbrain", "sync", "capture", "runtime", "test", "ci"])
    confidence = "high" if failed and passed_after_failure else ("medium" if failed or commands else "low")
    title = task.strip()[:90] or "Runtime captured development lesson"
    symptom = "No command failure captured. Treat as low-confidence unless human adds evidence."
    if failed:
        first = failed[0]
        symptom = f"Command failed during implementation: `{first.get('cmd_text')}` exited {first.get('returncode')}."
    fix = "No passing verification captured yet."
    if passed_after_failure:
        fix = f"Final captured verification passed: `{passed_after_failure[-1].get('cmd_text')}`."
    elif commands and commands[-1].get("ok"):
        fix = f"Captured verification passed: `{commands[-1].get('cmd_text')}`."
    prevention = "Before similar work, inspect this run evidence and rerun the captured verification commands."
    if risky:
        prevention = "Before similar risky work, run Betavibe pre_implement, capture failed commands, and require a final passing verification before promotion."
    return {
        "title": title,
        "type": "pitfall" if failed else "pattern",
        "confidence": confidence,
        "tags": ["runtime-capture"],
        "tech_stack": [],
        "summary": f"Runtime-captured lesson for task: {task}",
        "symptom": symptom,
        "root_cause": "Inferred from runtime evidence; review command logs and diff before promotion.",
        "wrong_paths": "Commands that failed before the final verification are wrong-path evidence.",
        "fix": fix,
        "prevention_signal": prevention,
        "verify_trigger": "When touching the same subsystem or when captured verification commands change.",
        "evidence": {
            "commands": [{k: e.get(k) for k in ["cmd_text", "cwd", "returncode", "ok", "stdout_tail", "stderr_tail"]} for e in commands],
            "changed_files": changed,
        },
    }


def finish_run(registry: Path, run_id: str, repo: Path | None = None) -> dict:
    events = read_events(registry, run_id)
    start = next((e for e in events if e.get("kind") == "start"), {})
    task = start.get("task", "")
    draft = infer_draft(events, task, repo=repo)
    append_event(registry, run_id, {"kind": "finish", "draft": draft})
    summary_path = run_paths(registry, run_id).summary
    summary = json.loads(summary_path.read_text(encoding="utf-8")) if summary_path.exists() else {"id": run_id}
    summary.update({"status": "finished", "finished_at": now(), "draft": draft})
    summary_path.write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
    return draft
