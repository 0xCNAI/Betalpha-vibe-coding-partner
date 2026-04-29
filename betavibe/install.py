from __future__ import annotations

from pathlib import Path
import shutil

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

After a painful debugging session, run:

```bash
{prefix}python3 -m betavibe should-capture --debug-minutes <minutes> --attempts <wrong_attempts> --had-error-log --final-fix-verified --context "<bug summary>"
```

If it returns `CAPTURE_RECOMMENDED`, use the Betavibe insight skill/workflow: ask human approval, prefill inferred fields, ask only missing judgment fields, then save with:

```bash
{prefix}python3 -m betavibe capture ... --sync-gbrain
```

Memory layers:
- Local registry files are the source of truth across OpenClaw, Claude Code, Codex, Cursor, and other harnesses.
- GBrain is an optional semantic index. Check with `{prefix}python3 -m betavibe doctor`; if GBrain is missing/unhealthy, continue with the local registry and tell the human how to install/fix GBrain instead of blocking.
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


def install_git_enforcement(project: Path, pack_path: str = "Betalpha-vibe-coding-partner", require_failed: bool = False) -> list[Path]:
    git_dir = project / ".git"
    if not git_dir.exists():
        return []
    hook = git_dir / "hooks" / "pre-commit"
    marker_start = "# BETAVIBE_PRE_COMMIT_START"
    marker_end = "# BETAVIBE_PRE_COMMIT_END"
    require_failed_value = "1" if require_failed else "0"
    block = f'''{marker_start}
# Betavibe runtime-capture enforcement. Installed by Betalpha Vibe Coding Partner.
PROJECT_ROOT="$(git rev-parse --show-toplevel)"
REGISTRY="$PROJECT_ROOT/.betavibe/registry"
PACK="$PROJECT_ROOT/{pack_path}"
if [ -d "$PACK" ]; then
  cd "$PACK"
  python3 -m betavibe --registry "$REGISTRY" enforce --max-age-minutes 240 --require-failed {require_failed_value}
  STATUS=$?
  cd "$PROJECT_ROOT"
  if [ "$STATUS" -ne 0 ]; then
    cat <<'EOF'

Betavibe blocked this commit because no valid runtime capture evidence was found.

Before committing non-trivial code changes, run:

  RUN_ID=$(cd Betalpha-vibe-coding-partner && python3 -m betavibe --registry ../.betavibe/registry run-start --task "<task>" --harness codex --repo ..)
  cd Betalpha-vibe-coding-partner && python3 -m betavibe --registry ../.betavibe/registry run-exec "$RUN_ID" --cwd .. -- <failing-or-verification-command>
  cd Betalpha-vibe-coding-partner && python3 -m betavibe --registry ../.betavibe/registry run-exec "$RUN_ID" --cwd .. -- <passing-verification-command>
  cd Betalpha-vibe-coding-partner && python3 -m betavibe --registry ../.betavibe/registry run-finish "$RUN_ID" --repo ..

Then retry git commit.
EOF
    exit "$STATUS"
  fi
fi
{marker_end}'''
    old = hook.read_text(encoding="utf-8") if hook.exists() else "#!/usr/bin/env bash\nset -uo pipefail\n"
    if marker_start in old and marker_end in old:
        before = old.split(marker_start, 1)[0].rstrip()
        after = old.split(marker_end, 1)[1].lstrip()
        new = before + "\n" + block + "\n" + after
    else:
        new = old.rstrip() + "\n\n" + block + "\n"
    if new != old:
        hook.parent.mkdir(parents=True, exist_ok=True)
        hook.write_text(new, encoding="utf-8")
        hook.chmod(0o755)
        return [hook]
    return []


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


def install_all(project: Path, pack_path: str = "Betalpha-vibe-coding-partner", enforce_runtime: bool = False, require_failed: bool = False) -> dict[str, list[Path]]:
    result = {
        "contract": install_contract(project, pack_path),
        "skill": install_skill(project),
        "hooks": install_hooks(project, pack_path),
    }
    if enforce_runtime:
        result["git_enforcement"] = install_git_enforcement(project, pack_path, require_failed=require_failed)
    return result
