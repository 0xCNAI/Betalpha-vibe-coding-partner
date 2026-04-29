from __future__ import annotations

from pathlib import Path
import shutil
from . import gbrain_adapter

START = "<!-- BETAVIBE_AGENT_CONTRACT_START -->"
END = "<!-- BETAVIBE_AGENT_CONTRACT_END -->"


def contract_block(pack_path: str = ".") -> str:
    p = pack_path.rstrip("/") or "."
    prefix = f"cd {p} && " if p != "." else ""
    return f"""{START}
# Betalpha Vibe Coding Partner — mandatory resolver contract

This project uses Betalpha Vibe Coding Partner. Do not wait for the human to remember commands.

Before writing a spec for any non-trivial feature/integration/migration/refactor, run:

```bash
{prefix}python3 -m betavibe resolve pre_spec --context "<task, APIs, files, tools, risks>"
```

Before non-trivial implementation, run:

```bash
{prefix}python3 -m betavibe resolve pre_implement --context "<implementation plan and touched files>"
```

During implementation, use Betavibe as a lightweight evidence wrapper for meaningful verification commands. Do not record every shell command. Record tests/build/lint/typecheck/deploy/emulator/smoke checks that prove or disprove the change:

```bash
{prefix}python3 -m betavibe verify --task "<task>" --cwd .. -- <test-build-lint-or-smoke-command>
```

Repeated `verify --task "<same task>"` calls append to the same runtime run, so a bugfix can naturally contain both the failing command and the later passing verification. If you hit a bug/regression, preserve the failing command evidence before fixing when feasible. Do not intentionally break working code just to satisfy evidence unless the commit gate explicitly asks and no original failure was captured.

After a painful debugging session, run:

```bash
{prefix}python3 -m betavibe should-capture --debug-minutes <minutes> --attempts <wrong_attempts> --had-error-log --final-fix-verified --context "<bug summary>"
```

If it returns `CAPTURE_RECOMMENDED`, first try:

```bash
{prefix}python3 -m betavibe learn
```

If `learn` creates a pending reusable lesson, ask human approval before promotion. If it says the run is not strong enough, use the Betavibe insight skill/workflow: ask human approval, prefill inferred fields, ask only missing judgment fields, then save with `capture ... --sync-gbrain`.

If recall missed a lesson that should have existed, log it cheaply instead of letting the cold-start gap disappear:

```bash
{prefix}python3 -m betavibe journal --task "<task>" --miss "<what prior lesson should have existed>"
```

Memory layers:
- Repo-local registry files are the source of truth for project-specific lessons.
- `~/.betavibe/personal` is the strict portable registry for cross-repo lessons only. Keep it small (target <=30 high-value insights) and use it when a lesson applies across stacks/repos.
- GBrain is an optional semantic federation layer. Check with `{prefix}python3 -m betavibe doctor`; if GBrain is missing/unhealthy, continue with repo-local + personal registries and tell the human how to install/fix GBrain instead of blocking.
- Placement rule: store an insight where the fix lives. Code change -> source repo registry. Config/cron/env/ops change -> operations repo registry. Truly portable lesson -> personal registry.
- After promoting reviewed insights, commit the registry so experience travels across devices/harnesses:

```bash
{prefix}python3 -m betavibe sync --repo .. --push
```

For finished projects, prefer forensic excavation over raw git scanning:

```bash
{prefix}python3 -m betavibe excavate ..
```

Capture only hard-won, verified lessons: concrete symptom, root cause, wrong paths, verified final fix, prevention signal, verify trigger. Do not store routine edits, guesses, generic advice, or unverified fixes.
{END}
"""


def upsert_block(path: Path, block: str) -> bool:
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
    changed = new != existing
    if changed:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(new, encoding="utf-8")
    return changed


def install_contract(project: Path, pack_path: str = "Betalpha-vibe-coding-partner") -> list[Path]:
    block = contract_block(pack_path)
    targets = [
        project / "AGENTS.md",
        project / "CLAUDE.md",
        project / ".codex" / "AGENTS.md",
        project / ".claude" / "CLAUDE.md",
    ]
    changed = []
    for target in targets:
        if upsert_block(target, block):
            changed.append(target)
    return changed


# Backward-compatible name used by older CLI/tests.
def install(project: Path, pack_path: str = "Betalpha-vibe-coding-partner") -> list[Path]:
    return install_contract(project, pack_path)


def package_root() -> Path:
    return Path(__file__).resolve().parents[1]


def install_skill(project: Path) -> list[Path]:
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
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(text, encoding="utf-8")
            changed.append(target)
    return changed


def write_gbrain_status(project: Path) -> list[Path]:
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
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")
        return [path]
    return []


def install_git_enforcement(project: Path, pack_path: str = "Betalpha-vibe-coding-partner", strict_runtime: bool = False) -> list[Path]:
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
            hook.parent.mkdir(parents=True, exist_ok=True)
            hook.write_text(new, encoding="utf-8")
            hook.chmod(0o755)
            changed.append(hook)
    return changed


def install_hooks(project: Path, pack_path: str = "Betalpha-vibe-coding-partner") -> list[Path]:
    hooks_dir = project / ".betavibe" / "hooks"
    hooks_dir.mkdir(parents=True, exist_ok=True)
    scripts = {
        "pre_spec.sh": f"""#!/usr/bin/env bash
set -euo pipefail
cd \"$(dirname \"$0\")/../..\"
cd {pack_path!r}
python3 -m betavibe resolve pre_spec --context \"${{*:-}}\"
""",
        "pre_implement.sh": f"""#!/usr/bin/env bash
set -euo pipefail
cd \"$(dirname \"$0\")/../..\"
cd {pack_path!r}
python3 -m betavibe resolve pre_implement --context \"${{*:-}}\"
""",
        "should_capture.sh": f"""#!/usr/bin/env bash
set -euo pipefail
cd \"$(dirname \"$0\")/../..\"
cd {pack_path!r}
python3 -m betavibe should-capture "$@"
""",
    }
    changed: list[Path] = []
    for name, text in scripts.items():
        path = hooks_dir / name
        old = path.read_text(encoding="utf-8") if path.exists() else None
        if old != text:
            path.write_text(text, encoding="utf-8")
            path.chmod(0o755)
            changed.append(path)
    return changed


def install_all(project: Path, pack_path: str = "Betalpha-vibe-coding-partner", enforce_runtime: bool = False, strict_runtime: bool = False) -> dict[str, list[Path]]:
    result = {
        "contract": install_contract(project, pack_path),
        "skill": install_skill(project),
        "hooks": install_hooks(project, pack_path),
        "gbrain_status": write_gbrain_status(project),
    }
    if enforce_runtime:
        result["git_enforcement"] = install_git_enforcement(project, pack_path, strict_runtime=strict_runtime)
    return result
