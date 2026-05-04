from __future__ import annotations

from pathlib import Path, PurePosixPath
import difflib
import shutil
import subprocess
from . import gbrain_adapter

START = "<!-- BETAVIBE_AGENT_CONTRACT_START -->"
END = "<!-- BETAVIBE_AGENT_CONTRACT_END -->"


def _relative_depth(path: str) -> int:
    p = path.rstrip("/") or "."
    if p == ".":
        return 0
    parts = [part for part in PurePosixPath(p).parts if part not in (".", "")]
    return len(parts)


def _project_rel_from_pack(pack_path: str) -> str:
    depth = _relative_depth(pack_path)
    return "." if depth == 0 else "/".join([".."] * depth)


def _registry_rel_from_pack(pack_path: str) -> str:
    root = _project_rel_from_pack(pack_path)
    return ".betavibe/registry" if root == "." else f"{root}/.betavibe/registry"


def contract_block(pack_path: str = ".") -> str:
    p = pack_path.rstrip("/") or "."
    prefix = f"cd {p} && " if p != "." else ""
    registry = _registry_rel_from_pack(p)
    project_root = _project_rel_from_pack(p)
    base = f"python3 -m betavibe --registry {registry}"
    return f"""{START}
# Betalpha Vibe Coding Partner

Use Betavibe as a low-friction debug immune system, not a logging ritual.

- Before non-trivial spec/design: `{prefix}{base} recall "<task/context>"` (shortcut for `resolve pre_spec`)
- Before non-trivial implementation: `{prefix}{base} resolve pre_implement --context "<plan/files/risks>"`
- During bug/debug work, run verification through `.betavibe/hooks/verify.sh --task "<task>" -- <test/build/lint/typecheck/smoke>` instead of running bare test commands. Use `--no-fail` for the initial known-failing reproduction so the session can continue; rerun the same task after the fix without `--no-fail`.
- For meaningful verification commands outside installed hooks: `{prefix}{base} verify --task "<task>" --cwd {project_root} --repo {project_root} -- <test/build/lint/typecheck/smoke>`; same `--task` appends to one run for fail→fix→pass cycles.
- After painful verified debugging: optionally run `should-capture`, then `.betavibe/hooks/learn.sh` or `{prefix}{base} learn`; `learn` creates pending drafts only — never promote without human approval. If the original failure was observed outside Betavibe but Tino says it is reusable, run `{prefix}{base} learn --force-pending` to create a review-only pending draft instead of losing the lesson.
- If recall missed a lesson that should exist: `{prefix}{base} journal --task "<task>" --miss "<missing lesson>"`

Memory placement: project-specific lessons stay in this repo's `.betavibe/registry`; portable cross-repo lessons stay in `~/.betavibe/personal`; GBrain is optional semantic federation, not the source of truth. Store an insight where the fix lives: code -> source repo, config/cron/env -> ops repo, truly portable -> personal.

Capture only hard-won, verified, reusable lessons. Do not store routine edits, guesses, generic advice, or unverified fixes.
{END}
"""

def planned_upsert(path: Path, block: str) -> tuple[bool, str, str]:
    existing = path.read_text(encoding="utf-8") if path.exists() else ""
    if START in existing and END in existing:
        before = existing.split(START, 1)[0].rstrip()
        after = existing.split(END, 1)[1].lstrip()
        pieces = []
        if before:
            pieces.append(before)
        pieces.append(block.rstrip())
        if after:
            pieces.append(after.rstrip())
        new = "\n\n".join(pieces) + "\n"
    else:
        new = existing.rstrip() + "\n\n" + block.rstrip() + "\n" if existing.strip() else block.rstrip() + "\n"
    return new != existing, existing, new


def diff_text(path: Path, old: str, new: str) -> str:
    return "".join(difflib.unified_diff(old.splitlines(True), new.splitlines(True), fromfile=str(path), tofile=str(path)))


def upsert_block(path: Path, block: str, dry_run: bool = False, diffs: list[str] | None = None) -> bool:
    changed, old, new = planned_upsert(path, block)
    if changed:
        if diffs is not None:
            diffs.append(diff_text(path, old, new))
        if not dry_run:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(new, encoding="utf-8")
    return changed


def remove_between_markers(text: str, start: str, end: str) -> str:
    if start not in text or end not in text:
        return text
    before = text.split(start, 1)[0].rstrip()
    after = text.split(end, 1)[1].lstrip()
    if before and after:
        return before + "\n\n" + after
    if before:
        return before + "\n"
    if after:
        return after
    return ""


def detect_profile(project: Path) -> str:
    """Return 'ops' for agent/operations workspaces, otherwise 'project'."""
    markers = []
    for rel in ["AGENTS.md", "HEARTBEAT.md", "USER.md"]:
        path = project / rel
        if path.exists():
            markers.append(path.read_text(encoding="utf-8", errors="ignore")[:4000].lower())
    text = "\n".join(markers)
    ops_terms = ["agent_id", "tinoclaw", "heartbeat", "cron", "私人助理", "系統維護", "agent ops", "operations"]
    return "ops" if any(term in text for term in ops_terms) else "project"


def contract_targets(project: Path, profile: str = "project", minimal: bool = False) -> list[Path]:
    if minimal or profile in {"ops", "openclaw"}:
        return [project / "AGENTS.md"]
    return [
        project / "AGENTS.md",
        project / "CLAUDE.md",
        project / ".codex" / "AGENTS.md",
        project / ".claude" / "CLAUDE.md",
    ]


def install_contract(project: Path, pack_path: str = "Betalpha-vibe-coding-partner", minimal: bool = False, dry_run: bool = False, diffs: list[str] | None = None, profile: str = "project") -> list[Path]:
    block = contract_block(pack_path)
    targets = contract_targets(project, profile=profile, minimal=minimal)
    changed = []
    for target in targets:
        if upsert_block(target, block, dry_run=dry_run, diffs=diffs):
            changed.append(target)
    return changed


# Backward-compatible name used by older CLI/tests.
def install(project: Path, pack_path: str = "Betalpha-vibe-coding-partner") -> list[Path]:
    return install_contract(project, pack_path)


def package_root() -> Path:
    return Path(__file__).resolve().parents[1]


def install_skill(project: Path, dry_run: bool = False, diffs: list[str] | None = None) -> list[Path]:
    src = package_root() / "skills" / "betavibe-insight" / "SKILL.md"
    if not src.exists():
        raise FileNotFoundError(f"missing bundled skill: {src}")
    targets = [
        project / "skills" / "betavibe-insight" / "SKILL.md",
        project / ".claude" / "skills" / "betavibe-insight" / "SKILL.md",
    ]
    changed: list[Path] = []
    for target in targets:
        existing = target.read_text(encoding="utf-8") if target.exists() else None
        text = src.read_text(encoding="utf-8")
        if existing != text:
            if diffs is not None:
                diffs.append(diff_text(target, existing or "", text))
            if not dry_run:
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_text(text, encoding="utf-8")
            changed.append(target)
    return changed


def write_gbrain_status(project: Path, dry_run: bool = False, diffs: list[str] | None = None) -> list[Path]:
    status = gbrain_adapter.status()
    path = project / ".betavibe" / "GBRAIN_STATUS.md"
    lines = [
        "# Betavibe GBrain Status",
        "",
        "GBrain is the optional semantic recall layer. The git registry remains the source of truth.",
        "",
        f"- installed: {'yes' if status.installed else 'no'}",
        f"- healthy: {'yes' if status.healthy else 'no'}",
        f"- binary: `{status.binary or 'not found on PATH'}`",
        f"- detail: {status.detail}",
        f"- guidance: {status.install_hint}",
        "",
        "Agents must not silently assume GBrain is available. If this file says unhealthy/missing, continue with local registry and tell the human that semantic sync is disabled.",
        "",
    ]
    old = path.read_text(encoding="utf-8") if path.exists() else None
    text = "\n".join(lines)
    if old != text:
        if diffs is not None:
            diffs.append(diff_text(path, old or "", text))
        if not dry_run:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(text, encoding="utf-8")
        return [path]
    return []


def install_git_enforcement(project: Path, pack_path: str = "Betalpha-vibe-coding-partner", strict_runtime: bool = False, dry_run: bool = False, diffs: list[str] | None = None) -> list[Path]:
    git_dir = project / ".git"
    if not git_dir.exists():
        return []
    changed: list[Path] = []
    pre_commit = git_dir / "hooks" / "pre-commit"
    commit_msg = git_dir / "hooks" / "commit-msg"
    pre_marker_start = "# BETAVIBE_PRE_COMMIT_START"
    pre_marker_end = "# BETAVIBE_PRE_COMMIT_END"
    msg_marker_start = "# BETAVIBE_COMMIT_MSG_START"
    msg_marker_end = "# BETAVIBE_COMMIT_MSG_END"
    strict_flag = "strict" if strict_runtime else "pass"
    pre_block = f'''{pre_marker_start}
# Betavibe lightweight verification gate. Installed by Betalpha Vibe Coding Partner.
PROJECT_ROOT="$(git rev-parse --show-toplevel)"
REGISTRY="$PROJECT_ROOT/.betavibe/registry"
PACK="$PROJECT_ROOT/{pack_path}"
if [ -d "$PACK" ]; then
  cd "$PACK"
  python3 -m betavibe --registry "$REGISTRY" enforce --max-age-minutes 240 --mode {strict_flag}
  STATUS=$?
  cd "$PROJECT_ROOT"
  if [ "$STATUS" -ne 0 ]; then
    cat <<'EOF'

Betavibe blocked this commit because no recent passing verification was captured.

Run your normal test/build/lint/typecheck command through Betavibe once, then retry:

  RUN_ID=$(cd Betalpha-vibe-coding-partner && python3 -m betavibe --registry ../.betavibe/registry run-start --task "<task>" --harness codex --repo ..)
  cd Betalpha-vibe-coding-partner && python3 -m betavibe --registry ../.betavibe/registry run-exec "$RUN_ID" --cwd .. -- <verification-command>
  cd Betalpha-vibe-coding-partner && python3 -m betavibe --registry ../.betavibe/registry run-finish "$RUN_ID" --repo ..

For bugfix/regression/high-risk commits, the commit-msg hook may additionally require failed-command evidence.
EOF
    exit "$STATUS"
  fi
fi
{pre_marker_end}'''
    msg_block = f'''{msg_marker_start}
# Betavibe risk-aware bugfix gate. Installed by Betalpha Vibe Coding Partner.
PROJECT_ROOT="$(git rev-parse --show-toplevel)"
REGISTRY="$PROJECT_ROOT/.betavibe/registry"
PACK="$PROJECT_ROOT/{pack_path}"
MSG_FILE="$1"
case "$MSG_FILE" in
  /*) ;;
  *) MSG_FILE="$PROJECT_ROOT/$MSG_FILE" ;;
esac
if [ -d "$PACK" ] && [ -f "$MSG_FILE" ]; then
  cd "$PACK"
  python3 -m betavibe --registry "$REGISTRY" enforce --max-age-minutes 240 --mode auto --commit-message-file "$MSG_FILE"
  STATUS=$?
  cd "$PROJECT_ROOT"
  if [ "$STATUS" -ne 0 ]; then
    cat <<'EOF'

Betavibe blocked this bugfix/high-risk commit because it has passing verification but no captured failing-command evidence.

This only applies when the commit message looks like bugfix/regression/auth/migration/schema/deploy/security work.
If this is genuinely not a bugfix/high-risk commit, rewrite the commit message more accurately.
If it is a bugfix, capture the original failure and the later passing verification in the same Betavibe run.
EOF
    exit "$STATUS"
  fi
fi
{msg_marker_end}'''
    for hook, start, end, block in [(pre_commit, pre_marker_start, pre_marker_end, pre_block), (commit_msg, msg_marker_start, msg_marker_end, msg_block)]:
        old = hook.read_text(encoding="utf-8") if hook.exists() else "#!/usr/bin/env bash\nset -uo pipefail\n"
        if start in old and end in old:
            before = old.split(start, 1)[0].rstrip()
            after = old.split(end, 1)[1].lstrip()
            new = before + "\n" + block + "\n" + after
        else:
            new = old.rstrip() + "\n\n" + block + "\n"
        if new != old:
            if diffs is not None:
                diffs.append(diff_text(hook, old, new))
            if not dry_run:
                hook.parent.mkdir(parents=True, exist_ok=True)
                hook.write_text(new, encoding="utf-8")
                hook.chmod(0o755)
            changed.append(hook)
    return changed


def install_hooks(project: Path, pack_path: str = "Betalpha-vibe-coding-partner", dry_run: bool = False, diffs: list[str] | None = None) -> list[Path]:
    hooks_dir = project / ".betavibe" / "hooks"
    if not dry_run:
        hooks_dir.mkdir(parents=True, exist_ok=True)
    scripts = {
        "pre_spec.sh": f"""#!/usr/bin/env bash
set -euo pipefail
PROJECT_ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
cd "$PROJECT_ROOT"
cd {pack_path!r}
python3 -m betavibe --registry "$PROJECT_ROOT/.betavibe/registry" resolve pre_spec --context "${{*:-}}"
""",
        "pre_implement.sh": f"""#!/usr/bin/env bash
set -euo pipefail
PROJECT_ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
cd "$PROJECT_ROOT"
cd {pack_path!r}
python3 -m betavibe --registry "$PROJECT_ROOT/.betavibe/registry" resolve pre_implement --context "${{*:-}}"
""",
        "should_capture.sh": f"""#!/usr/bin/env bash
set -euo pipefail
PROJECT_ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
cd "$PROJECT_ROOT"
cd {pack_path!r}
python3 -m betavibe --registry "$PROJECT_ROOT/.betavibe/registry" should-capture "$@"
""",
        "verify.sh": f"""#!/usr/bin/env bash
set -euo pipefail
PROJECT_ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
cd "$PROJECT_ROOT"
cd {pack_path!r}
python3 -m betavibe --registry "$PROJECT_ROOT/.betavibe/registry" verify --cwd "$PROJECT_ROOT" --repo "$PROJECT_ROOT" "$@"
""",
        "learn.sh": f"""#!/usr/bin/env bash
set -euo pipefail
PROJECT_ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
cd "$PROJECT_ROOT"
cd {pack_path!r}
python3 -m betavibe --registry "$PROJECT_ROOT/.betavibe/registry" learn "$@"
""",
    }
    changed: list[Path] = []
    for name, text in scripts.items():
        path = hooks_dir / name
        old = path.read_text(encoding="utf-8") if path.exists() else None
        if old != text:
            if diffs is not None:
                diffs.append(diff_text(path, old or "", text))
            if not dry_run:
                path.write_text(text, encoding="utf-8")
                path.chmod(0o755)
            changed.append(path)
    return changed

def install_all(project: Path, pack_path: str = "Betalpha-vibe-coding-partner", enforce_runtime: bool = False, strict_runtime: bool = False, minimal: bool = False, dry_run: bool = False, profile: str = "auto") -> dict[str, list[Path] | list[str]]:
    effective_profile = detect_profile(project) if profile == "auto" else profile
    diffs: list[str] = []
    result: dict[str, list[Path] | list[str]] = {
        "profile": [Path(effective_profile)],
        "contract": install_contract(project, pack_path, minimal=minimal, dry_run=dry_run, diffs=diffs, profile=effective_profile),
    }
    if not minimal:
        result.update({
            "skill": install_skill(project, dry_run=dry_run, diffs=diffs),
            "hooks": install_hooks(project, pack_path, dry_run=dry_run, diffs=diffs),
            "gbrain_status": write_gbrain_status(project, dry_run=dry_run, diffs=diffs),
        })
    if enforce_runtime and not minimal and effective_profile == "project":
        result["git_enforcement"] = install_git_enforcement(project, pack_path, strict_runtime=strict_runtime, dry_run=dry_run, diffs=diffs)
    elif enforce_runtime and effective_profile != "project":
        result["git_enforcement"] = []
        diffs.append(f"Skipped commit enforcement for {effective_profile} workspace. Use --profile project only in product/source repos.\n")
    result["diffs"] = diffs
    return result


def uninstall_all(project: Path, dry_run: bool = False) -> dict[str, list[Path] | list[str]]:
    diffs: list[str] = []
    changed: list[Path] = []
    files = [project / "AGENTS.md", project / "CLAUDE.md", project / ".codex" / "AGENTS.md", project / ".claude" / "CLAUDE.md"]
    for path in files:
        if not path.exists():
            continue
        old = path.read_text(encoding="utf-8")
        new = remove_between_markers(old, START, END)
        if new != old:
            diffs.append(diff_text(path, old, new))
            if not dry_run:
                path.write_text(new, encoding="utf-8")
            changed.append(path)
    hook_specs = [
        (project / ".git" / "hooks" / "pre-commit", "# BETAVIBE_PRE_COMMIT_START", "# BETAVIBE_PRE_COMMIT_END"),
        (project / ".git" / "hooks" / "commit-msg", "# BETAVIBE_COMMIT_MSG_START", "# BETAVIBE_COMMIT_MSG_END"),
    ]
    for path, start, end in hook_specs:
        if not path.exists():
            continue
        old = path.read_text(encoding="utf-8")
        new = remove_between_markers(old, start, end)
        if new != old:
            diffs.append(diff_text(path, old, new))
            if not dry_run:
                path.write_text(new, encoding="utf-8")
            changed.append(path)
    return {"removed": changed, "diffs": diffs}


def bootstrap(project: Path, source: str, vendor_path: str = "vendor/Betalpha-vibe-coding-partner", minimal: bool = False, enforce_runtime: bool = False, strict_runtime: bool = False, dry_run: bool = False, profile: str = "auto") -> dict[str, list[Path] | list[str]]:
    vendor = project / vendor_path
    diffs: list[str] = []
    changed: list[Path] = []
    if not vendor.exists():
        if dry_run:
            diffs.append(f"Would clone {source} -> {vendor}\n")
            changed.append(vendor)
        else:
            vendor.parent.mkdir(parents=True, exist_ok=True)
            subprocess.run(["git", "clone", source, str(vendor)], check=True)
            changed.append(vendor)
    elif (vendor / ".git").exists():
        if dry_run:
            diffs.append(f"Would update existing Betavibe vendor repo at {vendor}\n")
        else:
            subprocess.run(["git", "pull", "--ff-only"], cwd=vendor, check=True)
    result = install_all(project, pack_path=vendor_path, enforce_runtime=enforce_runtime, strict_runtime=strict_runtime, minimal=minimal, dry_run=dry_run, profile=profile)
    result["vendor"] = changed
    result["diffs"] = [*diffs, *result.get("diffs", [])]
    return result
