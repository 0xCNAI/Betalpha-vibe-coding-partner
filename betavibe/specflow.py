from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
import json
import re
import subprocess

from .models import slugify


REQUIRED_SECTIONS = [
    "Task",
    "Relevant Betavibe Insights",
    "Spec Guardrails",
    "Implementation Plan",
    "Verification Plan",
]


@dataclass
class SpecValidation:
    ok: bool
    path: Path
    missing: list[str]
    empty: list[str]


def _now() -> str:
    return datetime.now(timezone.utc).isoformat()


def _section_re(title: str) -> re.Pattern:
    return re.compile(rf"^##\s+{re.escape(title)}\s*$", re.IGNORECASE | re.MULTILINE)


def _section_body(text: str, title: str) -> str:
    match = _section_re(title).search(text)
    if not match:
        return ""
    rest = text[match.end():]
    next_section = re.search(r"^##\s+", rest, re.MULTILINE)
    body = rest[: next_section.start()] if next_section else rest
    return body.strip()


def default_spec_path(task: str, specs_dir: Path | None = None) -> Path:
    date = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    return (specs_dir or Path("specs")) / f"{date}-{slugify(task)[:48]}.md"


def write_spec_start(registry: Path, task: str, context: str = "", out: Path | None = None) -> Path:
    path = out or default_spec_path(task)
    if not path.is_absolute():
        path = (Path.cwd() / path).resolve()
    path.parent.mkdir(parents=True, exist_ok=True)
    text = "\n".join([
        f"# Spec: {task}",
        "",
        "## Task",
        "",
        task,
        "",
        "## Relevant Betavibe Insights",
        "",
        context or "Run `python3 -m betavibe resolve pre_spec --context \"<task/context>\"` and paste meaningful hits here.",
        "",
        "## Spec Guardrails",
        "",
        "- Convert relevant prevention_signal fields into concrete checklist items.",
        "",
        "## Implementation Plan",
        "",
        "- List touched files, data flow, migration/config risks, and non-goals.",
        "",
        "## Verification Plan",
        "",
        "- Define the test/build/lint/smoke gate that must pass before claiming done.",
        "",
    ])
    path.write_text(text, encoding="utf-8")
    log_spec_event(registry, "spec_start", {"task": task, "spec_path": str(path), "context": context})
    return path


def validate_spec(path: Path) -> SpecValidation:
    path = path.expanduser()
    text = path.read_text(encoding="utf-8") if path.exists() else ""
    missing = [section for section in REQUIRED_SECTIONS if not _section_re(section).search(text)]
    empty = [section for section in REQUIRED_SECTIONS if section not in missing and not _section_body(text, section)]
    return SpecValidation(ok=not missing and not empty, path=path, missing=missing, empty=empty)


def staged_spec_paths(repo: Path | None = None) -> list[Path]:
    cwd = repo or Path.cwd()
    proc = subprocess.run(["git", "diff", "--cached", "--name-only", "--diff-filter=ACM"], cwd=cwd, text=True, capture_output=True, check=True)
    paths = []
    for rel in proc.stdout.splitlines():
        if not rel.startswith("specs/") or not rel.endswith(".md"):
            continue
        paths.append((cwd / rel).resolve())
    return paths


def validate_many(paths: list[Path]) -> list[SpecValidation]:
    return [validate_spec(path) for path in paths]


def log_spec_event(registry: Path, event: str, payload: dict) -> Path:
    log_dir = registry.parent / "usage"
    log_dir.mkdir(parents=True, exist_ok=True)
    path = log_dir / "spec_events.jsonl"
    row = {"ts": _now(), "event": event, **payload}
    with path.open("a", encoding="utf-8") as fh:
        fh.write(json.dumps(row, ensure_ascii=False) + "\n")
    return path


def compliance_rate(session_dir: Path) -> dict:
    rows = []
    for path in sorted(session_dir.glob("*.json")):
        rows.append(json.loads(path.read_text(encoding="utf-8")))
    specs_written = sum(1 for row in rows if row.get("spec_written"))
    spec_start_called = sum(1 for row in rows if row.get("spec_written") and row.get("spec_start_called"))
    rate = spec_start_called / specs_written if specs_written else 1.0
    return {
        "sessions": len(rows),
        "specs_written": specs_written,
        "spec_start_called": spec_start_called,
        "compliance_rate": rate,
    }
