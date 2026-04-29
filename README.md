# Betalpha Vibe Coding Partner

A portable development-insight registry for vibe-coding teams.

It helps OpenClaw, Claude Code, Codex, Cowork, and future coding tools reuse hard-won engineering lessons before writing specs or code.

## What it does

1. **Before work**: `advise` searches past pitfalls, decisions, patterns, and tool choices relevant to the current task.
2. **After work**: `capture` writes reviewed insights into a durable markdown registry.
3. **From existing history**: `scan-git` mines a project’s git / GitHub evolution for candidate insights: fixes, reverts, migrations, regressions, CI failures, risky files, and repeated churn.
4. **Across agents**: instructions in `AGENTS.md`, `CLAUDE.md`, `.codex/AGENTS.md`, and `.claude/CLAUDE.md` teach tools how to use the same registry.

This is intentionally **not silent auto-learning**. The system can draft candidates automatically, but reviewed insights are promoted explicitly. Bad memory is worse than missing memory.

## Quick start

```bash
# From this repo
python3 -m betavibe init
python3 -m betavibe advise "oauth line bot refresh token"
python3 -m betavibe scan-git /path/to/project --since "90 days ago"
python3 -m betavibe pending
python3 -m betavibe promote <pending-id>
```

Default registry: `./registry`. Use `--registry ~/.betalpha-vibe/registry` for a shared central registry.

## Recommended setup for real use

Use one shared registry and mount/copy this package into projects:

```bash
export BETAVIBE_REGISTRY="$HOME/.betalpha-vibe/registry"
python3 -m betavibe init --registry "$BETAVIBE_REGISTRY"
python3 -m betavibe scan-git ~/code/my-project --registry "$BETAVIBE_REGISTRY"
python3 -m betavibe advise "new auth integration" --registry "$BETAVIBE_REGISTRY"
```

## Insight types

- `pitfall`: painful bug / regression / failure mode with a verified fix.
- `decision`: choice among options, including accepted trade-offs.
- `pattern`: reusable implementation or delivery pattern.
- `tool_choice`: when to use OpenClaw / Claude Code / Codex / Cowork / local scripts / browser / APIs.
- `spec_guardrail`: checklist item that should appear before implementation starts.

## Agent contract

Before non-trivial spec or implementation:

```bash
python3 -m betavibe advise "<task keywords>" --registry "$BETAVIBE_REGISTRY"
```

After tricky work:

```bash
python3 -m betavibe capture --type pitfall --title "..." --symptom "..." --root-cause "..." --fix "..." --prevention-signal "..."
```

When onboarding an existing project:

```bash
python3 -m betavibe scan-git /path/to/project --with-github
python3 -m betavibe pending
python3 -m betavibe promote <id>
```

## Why markdown

Markdown keeps the registry readable by every agent. The CLI adds validation, search, and history mining; the source of truth remains plain files.
