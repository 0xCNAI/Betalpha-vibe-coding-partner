from __future__ import annotations

from pathlib import Path
import json
import time


def _commands(events_path: Path) -> list[dict]:
    if not events_path.exists():
        return []
    out = []
    for line in events_path.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        try:
            item = json.loads(line)
        except Exception:
            continue
        if item.get("kind") == "command":
            out.append(item)
    return out


def latest_valid_run(registry: Path, max_age_minutes: int = 240) -> dict | None:
    runs = registry / "runs"
    if not runs.exists():
        return None
    cutoff = time.time() - max_age_minutes * 60
    candidates = []
    for root in runs.iterdir():
        if not root.is_dir():
            continue
        events = root / "events.jsonl"
        if not events.exists() or events.stat().st_mtime < cutoff:
            continue
        commands = _commands(events)
        has_failed = any(not c.get("ok") for c in commands)
        has_passed = any(c.get("ok") for c in commands)
        if commands and has_passed:
            candidates.append({
                "id": root.name,
                "path": str(root),
                "commands": len(commands),
                "has_failed": has_failed,
                "has_passed": has_passed,
                "mtime": events.stat().st_mtime,
            })
    if not candidates:
        return None
    candidates.sort(key=lambda x: x["mtime"], reverse=True)
    return candidates[0]


def check_runtime_required(registry: Path, max_age_minutes: int = 240, require_failed: bool = False) -> tuple[bool, str]:
    run = latest_valid_run(registry, max_age_minutes=max_age_minutes)
    if not run:
        return False, "No recent Betavibe runtime capture run with passing verification was found."
    if require_failed and not run["has_failed"]:
        return False, f"Recent Betavibe run {run['id']} has passing verification but no failed-command evidence."
    return True, f"Betavibe runtime evidence found: {run['id']} ({run['commands']} captured commands)."
