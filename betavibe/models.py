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
    concrete_evidence: str = ""
    transferable_pattern: str = ""
    domain_metadata: dict[str, Any] = field(default_factory=dict)
    tech_versions_last_seen: dict[str, str] = field(default_factory=dict)
    created_at: str = field(default_factory=lambda: date.today().isoformat())
    last_verified_at: str = field(default_factory=lambda: date.today().isoformat())
    source: dict[str, Any] = field(default_factory=dict)
    body: dict[str, str] = field(default_factory=dict)
    path: Path | None = None

    def __post_init__(self) -> None:
        if not self.concrete_evidence:
            self.concrete_evidence = str(self.body.get("evidence") or self.summary)
        if not self.transferable_pattern:
            self.transferable_pattern = str(self.body.get("pattern") or self.prevention_signal)
        if not self.domain_metadata:
            self.domain_metadata = {
                "tags": self.tags,
                "tech_stack": self.tech_stack,
                "source_kind": self.source.get("kind"),
            }

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
        if not self.concrete_evidence.strip():
            errors.append("concrete_evidence required")
        if not self.transferable_pattern.strip():
            errors.append("transferable_pattern required")
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
            "concrete_evidence": self.concrete_evidence,
            "transferable_pattern": self.transferable_pattern,
            "domain_metadata": self.domain_metadata,
            "tech_versions_last_seen": self.tech_versions_last_seen,
            "created_at": self.created_at,
            "last_verified_at": self.last_verified_at,
            "source": self.source,
        }
        parts = ["---", json.dumps(fm, ensure_ascii=False, indent=2), "---", ""]
        order = ["symptom", "root_cause", "wrong_paths", "fix", "decision", "tradeoffs", "pattern", "tool_guidance", "evidence"]
        for key in order:
            raw = self.body.get(key)
            if raw is None:
                val = ""
            elif isinstance(raw, str):
                val = raw.strip()
            else:
                val = json.dumps(raw, ensure_ascii=False, indent=2).strip()
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
        lines = text.splitlines(keepends=True)
        end_index = None
        for idx, line in enumerate(lines[1:], start=1):
            if line.strip() == "---":
                end_index = idx
                break
        if end_index is None:
            raise ValueError("missing closing frontmatter")
        raw = "".join(lines[1:end_index])
        body_text = "".join(lines[end_index + 1:])
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
            concrete_evidence=str(data.get("concrete_evidence") or body.get("evidence") or data.get("summary") or ""),
            transferable_pattern=str(data.get("transferable_pattern") or body.get("pattern") or data.get("prevention_signal") or ""),
            domain_metadata=dict(data.get("domain_metadata") or {}),
            tech_versions_last_seen=dict(data.get("tech_versions_last_seen") or data.get("domain_metadata", {}).get("tech_versions_last_seen") or {}),
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
