from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
import hashlib
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


def state_path(registry: Path) -> Path:
    return registry / "runtime_state.json"


def load_state(registry: Path) -> dict:
    path = state_path(registry)
    if not path.exists():
        return {"active_tasks": {}, "latest_run": None}
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return {"active_tasks": {}, "latest_run": None}


def save_state(registry: Path, state: dict) -> None:
    registry.mkdir(parents=True, exist_ok=True)
    state_path(registry).write_text(json.dumps(state, ensure_ascii=False, indent=2), encoding="utf-8")


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
    start_head = None
    if repo and (repo / ".git").exists():
        proc = subprocess.run(["git", "rev-parse", "HEAD"], cwd=repo, capture_output=True, text=True, check=False)
        if proc.returncode == 0:
            start_head = proc.stdout.strip()
    summary = {
        "id": run_id,
        "task": task,
        "harness": harness or os.environ.get("BETAVIBE_HARNESS") or "unknown",
        "repo": str(repo.resolve()) if repo else None,
        "start_head": start_head,
        "started_at": now(),
        "status": "running",
    }
    paths.summary.write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
    append_event(registry, run_id, {"kind": "start", "task": task, "harness": summary["harness"], "repo": summary["repo"]})
    state = load_state(registry)
    state.setdefault("active_tasks", {})[task] = run_id
    state["latest_run"] = run_id
    save_state(registry, state)
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


def git_changed_files(repo: Path | None, start_head: str | None = None) -> list[str]:
    if not repo or not (repo / ".git").exists():
        return []
    files: list[str] = []
    if start_head:
        proc = subprocess.run(["git", "diff", "--name-only", f"{start_head}..HEAD"], cwd=repo, capture_output=True, text=True, check=False)
        if proc.returncode == 0:
            files.extend([line.strip() for line in proc.stdout.splitlines() if line.strip()])
    proc = subprocess.run(["git", "status", "--porcelain"], cwd=repo, capture_output=True, text=True, check=False)
    for line in proc.stdout.splitlines():
        if line.strip():
            path = line[3:]
            if path not in files:
                files.append(path)
    return files


def infer_draft(events: list[dict], task: str, repo: Path | None = None, start_head: str | None = None) -> dict:
    commands = [e for e in events if e.get("kind") == "command"]
    failed = [e for e in commands if not e.get("ok")]
    passed_after_failure = []
    seen_failure = False
    for e in commands:
        if not e.get("ok"):
            seen_failure = True
        elif seen_failure:
            passed_after_failure.append(e)
    changed = git_changed_files(repo, start_head=start_head)
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
    summary_path = run_paths(registry, run_id).summary
    summary = json.loads(summary_path.read_text(encoding="utf-8")) if summary_path.exists() else {"id": run_id}
    draft = infer_draft(events, task, repo=repo, start_head=summary.get("start_head"))
    append_event(registry, run_id, {"kind": "finish", "draft": draft})
    summary.update({"status": "finished", "finished_at": now(), "draft": draft})
    summary_path.write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
    state = load_state(registry)
    state["latest_run"] = run_id
    save_state(registry, state)
    return draft


def latest_run_id(registry: Path) -> str | None:
    state = load_state(registry)
    if state.get("latest_run"):
        return state["latest_run"]
    runs = runs_root(registry)
    if not runs.exists():
        return None
    candidates = [p for p in runs.iterdir() if p.is_dir() and (p / "summary.json").exists()]
    if not candidates:
        return None
    candidates.sort(key=lambda p: (p / "summary.json").stat().st_mtime, reverse=True)
    return candidates[0].name


def verify_command(registry: Path, task: str, command: list[str], cwd: Path, harness: str | None = None, repo: Path | None = None, no_fail: bool = False, run_id: str | None = None) -> tuple[int, str, dict]:
    state = load_state(registry)
    if not run_id:
        run_id = state.get("active_tasks", {}).get(task)
    if not run_id or not run_paths(registry, run_id).summary.exists():
        run_id = start_run(registry, task, harness=harness, repo=repo)
    code = run_command(registry, run_id, command, cwd=cwd)
    draft = finish_run(registry, run_id, repo=repo)
    return (0 if no_fail else code), run_id, draft


def learn_from_run(registry: Path, run_id: str | None = None) -> tuple[str, Path | None]:
    from .registry import write_pending

    run_id = run_id or latest_run_id(registry)
    if not run_id:
        return "No Betavibe runtime run found.", None
    summary_path = run_paths(registry, run_id).summary
    if not summary_path.exists():
        return f"Runtime run not found: {run_id}", None
    summary = json.loads(summary_path.read_text(encoding="utf-8"))
    draft = summary.get("draft") or infer_draft(read_events(registry, run_id), summary.get("task", ""), repo=Path(summary["repo"]) if summary.get("repo") else None, start_head=summary.get("start_head"))
    commands = draft.get("evidence", {}).get("commands", [])
    has_failed = any(not c.get("ok") for c in commands)
    changed = draft.get("evidence", {}).get("changed_files", [])
    if draft.get("confidence") != "high" or not has_failed:
        return f"Run {run_id} is not strong enough to learn automatically (confidence={draft.get('confidence')}, failed_evidence={'yes' if has_failed else 'no'}). Keep it as runtime evidence; promote only if the human says it was a reusable lesson.", None
    key = hashlib.sha1((run_id + draft.get("title", "")).encode("utf-8")).hexdigest()[:10]
    candidate = {
        "id": f"runtime-{key}",
        "title": draft.get("title") or summary.get("task") or "Runtime captured lesson",
        "type": draft.get("type", "pitfall"),
        "score": 8 + min(2, len(changed)),
        "summary": draft.get("summary", ""),
        "tags": draft.get("tags", ["runtime-capture"]),
        "tech_stack": draft.get("tech_stack", []),
        "reasons": ["failed command evidence", "passing verification", "runtime capture"],
        "source": {"kind": "runtime", "run_id": run_id, "changed_files": changed},
        "draft": draft,
    }
    path = write_pending(candidate, registry)
    return f"Created pending reusable lesson from runtime run {run_id}: {path}", path
