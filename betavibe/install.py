from __future__ import annotations

from pathlib import Path

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

If it returns `CAPTURE_RECOMMENDED`, ask the human for conversational approval, prefill inferred fields, ask only missing judgment fields, then save with:

```bash
{prefix}python3 -m betavibe capture ... --sync-gbrain
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


def install(project: Path, pack_path: str = "Betalpha-vibe-coding-partner") -> list[Path]:
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
