from __future__ import annotations

from pathlib import Path
import json
import os
from .models import Insight

DEFAULT_PERSONAL_REGISTRY = Path(os.environ.get("BETAVIBE_PERSONAL_REGISTRY", "~/.betavibe/personal")).expanduser()


def _nearest_project_registry(start: Path | None = None) -> Path | None:
    """Find the nearest host-project registry from the current working tree.

    Betavibe is often vendored under `vendor/Betalpha-vibe-coding-partner`.
    In that layout, the dangerous historical default was `./registry`, which
    writes evidence into the vendored pack instead of the host project.  Prefer
    the nearest parent containing `.betavibe/` so plain `python3 -m betavibe ...`
    still lands in the project registry.
    """

    cursor = (start or Path.cwd()).resolve()
    for parent in (cursor, *cursor.parents):
        marker = parent / ".betavibe"
        if marker.exists():
            return marker / "registry"
    return None


def resolve_registry(path: str | Path | None = None) -> Path:
    if path:
        return Path(path)
    env_registry = os.environ.get("BETAVIBE_REGISTRY")
    if env_registry:
        return Path(env_registry)
    return _nearest_project_registry() or Path("registry")


def personal_registry() -> Path:
    return DEFAULT_PERSONAL_REGISTRY


def init_registry(registry: Path) -> None:
    (registry / "insights").mkdir(parents=True, exist_ok=True)
    (registry / "pending").mkdir(parents=True, exist_ok=True)
    (registry / "schema").mkdir(parents=True, exist_ok=True)
    readme = registry / "README.md"
    if not readme.exists():
        readme.write_text("# Betalpha Vibe Coding Partner Registry\n\nReviewed insights live in `insights/`; auto-mined candidates live in `pending/`.\n", encoding="utf-8")


def write_insight(insight: Insight, registry: Path) -> Path:
    errors = insight.validate()
    if errors:
        raise ValueError("invalid insight:\n- " + "\n- ".join(errors))
    folder = registry / "insights" / f"{insight.created_at[:7]}-{insight.slug}"
    folder.mkdir(parents=True, exist_ok=True)
    path = folder / "INSIGHT.md"
    path.write_text(insight.to_markdown(), encoding="utf-8")
    return path


def list_insights(registry: Path) -> list[Insight]:
    root = registry / "insights"
    if not root.exists():
        return []
    out: list[Insight] = []
    for path in root.rglob("INSIGHT.md"):
        try:
            out.append(Insight.from_markdown(path.read_text(encoding="utf-8"), path=path))
        except Exception as exc:
            print(f"[warn] skipped malformed insight {path}: {exc}")
    return out


def list_scoped_insights(registry: Path, include_personal: bool = True) -> list[Insight]:
    insights = list_insights(registry)
    if include_personal:
        seen_slugs = {i.slug for i in insights}
        for insight in list_insights(personal_registry()):
            if insight.slug in seen_slugs:
                continue
            insight.tags = list(dict.fromkeys([*insight.tags, "portable"]))
            insights.append(insight)
            seen_slugs.add(insight.slug)
    return insights


def write_pending(candidate: dict, registry: Path) -> Path:
    (registry / "pending").mkdir(parents=True, exist_ok=True)
    path = registry / "pending" / f"{candidate['id']}.json"
    path.write_text(json.dumps(candidate, ensure_ascii=False, indent=2), encoding="utf-8")
    return path


def list_pending(registry: Path) -> list[dict]:
    root = registry / "pending"
    if not root.exists():
        return []
    out = []
    for path in root.glob("*.json"):
        try:
            item = json.loads(path.read_text(encoding="utf-8"))
            item["_path"] = str(path)
            out.append(item)
        except Exception as exc:
            print(f"[warn] skipped malformed pending {path}: {exc}")
    out.sort(key=lambda x: (-int(x.get("score", 0)), x.get("id", "")))
    return out
