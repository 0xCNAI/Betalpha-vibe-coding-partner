from __future__ import annotations

from dataclasses import dataclass
import os
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


@dataclass
class GBrainStatus:
    installed: bool
    healthy: bool
    detail: str
    install_hint: str
    binary: str | None = None


def _timeout(default: float = 4.0) -> float:
    raw = os.environ.get("BETAVIBE_GBRAIN_TIMEOUT_SEC")
    if not raw:
        return default
    try:
        return max(0.5, float(raw))
    except ValueError:
        return default


def status() -> GBrainStatus:
    binary = shutil.which("gbrain")
    if not binary:
        return GBrainStatus(
            installed=False,
            healthy=False,
            detail="gbrain CLI not found on PATH",
            install_hint="GBrain is optional but recommended for semantic recall. Install/configure the `gbrain` CLI, ensure it is on PATH, then rerun `python3 -m betavibe doctor`. Until then, Betavibe still works with local registry + git sync.",
            binary=None,
        )
    try:
        proc = subprocess.run(["gbrain", "doctor", "--fast", "--json"], capture_output=True, text=True, timeout=_timeout())
    except Exception as exc:
        return GBrainStatus(True, False, f"gbrain doctor failed to run: {exc}", "Run `gbrain doctor` manually and fix the reported setup issue.", binary=binary)
    if proc.returncode == 0:
        return GBrainStatus(True, True, "gbrain doctor passed", "No action needed.", binary=binary)
    detail = (proc.stderr or proc.stdout or "gbrain doctor returned non-zero").strip()
    return GBrainStatus(True, False, detail, "Run `gbrain doctor` and complete initialization/auth/import fixes before enabling semantic sync.", binary=binary)


def available() -> bool:
    s = status()
    return s.installed and s.healthy


def query(question: str, limit: int = 5) -> list[GBrainHit]:
    if not shutil.which("gbrain"):
        return []
    try:
        proc = subprocess.run(
            ["gbrain", "query", question, "--limit", str(limit), "--detail", "low"],
            capture_output=True,
            text=True,
            timeout=_timeout(),
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
        subprocess.run(["gbrain", "put", slug], input=content, capture_output=True, text=True, timeout=_timeout(), check=True)
        try:
            subprocess.run(["gbrain", "embed", slug], capture_output=True, text=True, timeout=_timeout(), check=False)
        except Exception:
            pass
        return slug
    except subprocess.TimeoutExpired:
        return None
    except Exception:
        # fallback: import via temporary directory for older gbrain put behavior
        try:
            with tempfile.TemporaryDirectory() as td:
                root = Path(td) / "dev-insights"
                root.mkdir(parents=True, exist_ok=True)
                (root / f"{insight.slug}.md").write_text(content, encoding="utf-8")
                subprocess.run(["gbrain", "import", td], capture_output=True, text=True, timeout=_timeout(), check=True)
            return slug
        except subprocess.TimeoutExpired:
            return None
        except Exception:
            return None
