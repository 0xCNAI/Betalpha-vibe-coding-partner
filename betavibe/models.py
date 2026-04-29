from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date
from pathlib import Path
from typing import Any
import json
import re

VALID_TYPES = {"pitfall", "decision", "pattern", "tool_choice", "spec_guardrail"}

@dataclass
class Insight:
    title: str
    type: str
    tags: list[str]
    tech_stack: list[str]
    summary: str
    prevention_signal: str
    verify_trigger: str
    created_at: str = field(default_factory=lambda: date.today().isoformat())
    last_verified_at: str = field(default_factory=lambda: date.today().isoformat())
    source: dict[str, Any] = field(default_factory=dict)
    body: dict[str, str] = field(default_factory=dict)
    path: Path | None = None

    @property
    def slug(self) -> str:
        return slugify(self.title)

    def validate(self) -> list[str]:
        errors: list[str] = []
        if self.type not in VALID_TYPES:
            errors.append(f"invalid type: {self.type}")
        if len(self.title.strip()) < 8:
            errors.append("title too short")
        if len(self.summary.strip()) < 30:
            errors.append("summary too short; include concrete context")
        if not self.tags:
            errors.append("at least one tag required")
        if len(self.prevention_signal.strip()) < 15:
            errors.append("prevention_signal too short / vague")
        if not self.verify_trigger.strip():
            errors.append("verify_trigger required; use 'never' only if truly stable")
        for field_name in ("created_at", "last_verified_at"):
            try:
                date.fromisoformat(getattr(self, field_name))
            except ValueError:
                errors.append(f"{field_name} must be YYYY-MM-DD")
        return errors

    def to_markdown(self) -> str:
        fm = {
            "title": self.title,
            "type": self.type,
            "tags": self.tags,
            "tech_stack": self.tech_stack,
            "summary": self.summary,
            "prevention_signal": self.prevention_signal,
            "verify_trigger": self.verify_trigger,
            "created_at": self.created_at,
            "last_verified_at": self.last_verified_at,
            "source": self.source,
        }
        parts = ["---", json.dumps(fm, ensure_ascii=False, indent=2), "---", ""]
        order = ["symptom", "root_cause", "wrong_paths", "fix", "decision", "tradeoffs", "pattern", "tool_guidance", "evidence"]
        for key in order:
            val = (self.body.get(key) or "").strip()
            if val:
                parts.append(f"## {key.replace('_', ' ').title()}")
                parts.append("")
                parts.append(val)
                parts.append("")
        return "\n".join(parts).rstrip() + "\n"

    @classmethod
    def from_markdown(cls, text: str, path: Path | None = None) -> "Insight":
        if not text.startswith("---\n"):
            raise ValueError("missing frontmatter")
        _, raw, body_text = text.split("---", 2)
        data = json.loads(raw)
        body = parse_sections(body_text)
        return cls(
            title=data["title"],
            type=data["type"],
            tags=list(data.get("tags") or []),
            tech_stack=list(data.get("tech_stack") or []),
            summary=data["summary"],
            prevention_signal=data["prevention_signal"],
            verify_trigger=data["verify_trigger"],
            created_at=str(data.get("created_at") or date.today().isoformat()),
            last_verified_at=str(data.get("last_verified_at") or data.get("created_at") or date.today().isoformat()),
            source=dict(data.get("source") or {}),
            body=body,
            path=path,
        )


def slugify(text: str) -> str:
    s = text.lower().strip()
    s = re.sub(r"[^a-z0-9\u4e00-\u9fff]+", "-", s)
    s = re.sub(r"-+", "-", s).strip("-")
    return s[:80] or "insight"


def parse_sections(body_text: str) -> dict[str, str]:
    sections: dict[str, str] = {}
    current = None
    buf: list[str] = []
    for line in body_text.splitlines():
        if line.startswith("## "):
            if current:
                sections[current] = "\n".join(buf).strip()
            current = line[3:].strip().lower().replace(" ", "_")
            buf = []
        elif current:
            buf.append(line)
    if current:
        sections[current] = "\n".join(buf).strip()
    return sections
