from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import shutil
import subprocess
import tempfile
from .models import Insight


@dataclass
class GBrainHit:
    score: float
    slug: str
    snippet: str
    stale: bool = False


def available() -> bool:
    if not shutil.which("gbrain"):
        return False
    try:
        subprocess.run(["gbrain", "doctor", "--fast", "--json"], capture_output=True, text=True, timeout=20)
        return True
    except Exception:
        return False


def query(question: str, limit: int = 5) -> list[GBrainHit]:
    if not shutil.which("gbrain"):
        return []
    try:
        proc = subprocess.run(
            ["gbrain", "query", question, "--limit", str(limit), "--detail", "low"],
            capture_output=True,
            text=True,
            timeout=45,
            check=False,
        )
    except Exception:
        return []
    if proc.returncode != 0:
        return []
    hits: list[GBrainHit] = []
    current: GBrainHit | None = None
    for raw in proc.stdout.splitlines():
        line = raw.rstrip()
        if line.startswith("[") and "]" in line and " -- " in line:
            if current:
                hits.append(current)
            score_raw, rest = line.split("]", 1)
            try:
                score = float(score_raw.strip("["))
            except ValueError:
                score = 0.0
            slug = rest.split("--", 1)[0].strip()
            stale = "(stale)" in line.lower()
            current = GBrainHit(score=score, slug=slug, snippet=line, stale=stale)
        elif current and line.strip():
            current.snippet += "\n" + line
    if current:
        hits.append(current)
    return hits[:limit]


def insight_to_gbrain_markdown(insight: Insight) -> str:
    tags = sorted(set(["betavibe", "dev-insight", insight.type, *insight.tags]))
    frontmatter = ["---"]
    frontmatter.append(f"title: {insight.title}")
    frontmatter.append("type: dev-insight")
    frontmatter.append("tags:")
    for tag in tags:
        frontmatter.append(f"  - {tag}")
    frontmatter.append(f"created_at: {insight.created_at}")
    frontmatter.append(f"last_verified_at: {insight.last_verified_at}")
    frontmatter.append("---")
    body = [
        f"# {insight.title}",
        "",
        f"Summary: {insight.summary}",
        "",
        f"Prevention signal: {insight.prevention_signal}",
        "",
        f"Verify trigger: {insight.verify_trigger}",
        "",
        "## Spec Implication",
        "",
        insight.body.get("spec_implication") or insight.prevention_signal,
        "",
        "## Implementation Checklist",
        "",
        insight.body.get("implementation_checklist") or "- Apply the prevention signal before coding.\n- Verify the final fix in the current environment.",
        "",
        insight.to_markdown(),
    ]
    return "\n".join(frontmatter + [""] + body)


def sync_insight(insight: Insight) -> str | None:
    if not shutil.which("gbrain"):
        return None
    slug = "dev-insights/" + insight.slug
    content = insight_to_gbrain_markdown(insight)
    try:
        subprocess.run(["gbrain", "put", slug], input=content, capture_output=True, text=True, timeout=45, check=True)
        try:
            subprocess.run(["gbrain", "embed", slug], capture_output=True, text=True, timeout=45, check=False)
        except Exception:
            pass
        return slug
    except Exception:
        # fallback: import via temporary directory for older gbrain put behavior
        try:
            with tempfile.TemporaryDirectory() as td:
                root = Path(td) / "dev-insights"
                root.mkdir(parents=True, exist_ok=True)
                (root / f"{insight.slug}.md").write_text(content, encoding="utf-8")
                subprocess.run(["gbrain", "import", td], capture_output=True, text=True, timeout=60, check=True)
            return slug
        except Exception:
            return None
