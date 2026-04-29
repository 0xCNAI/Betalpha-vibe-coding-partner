# Betalpha Vibe Coding Partner

Drop this folder into a project and coding agents should automatically reuse and capture hard-won development insights.

It is designed for OpenClaw, Claude Code, Codex, Cowork, Cursor, and any tool that reads project instruction files.

## What you should experience

You should **not** need to remember commands.

A good agent will:

1. **Before writing a spec**: search prior insights and add relevant guardrails.
2. **Before implementation**: check known pitfalls / wrong paths / tool-choice lessons.
3. **After painful debugging**: notice the session is worth capturing, ask you for approval, then save a structured insight.
4. **When onboarding old projects**: scan git / GitHub history and produce reviewable candidate insights.

## Install into a project

Copy this whole folder into your project, or keep it as a shared submodule / folder, then run the full installer from inside the Betavibe pack:

```bash
python3 -m betavibe install --project /path/to/project --pack-path Betalpha-vibe-coding-partner --self-test
```

The installer adds a managed root contract, agent skills, local hook wrappers, and initializes the registry. It writes managed blocks instead of overwriting existing instructions.

Recommended shared registry:

```bash
export BETAVIBE_REGISTRY="$HOME/.betalpha-vibe/registry"
python3 -m betavibe install --project /path/to/project --pack-path Betalpha-vibe-coding-partner --registry "$BETAVIBE_REGISTRY" --self-test
```

If no shared registry is configured, it uses local `registry/`.

## Agent-facing contract

Agents should read the root managed contract and/or the installed `betavibe-insight` skill, then use resolver commands automatically:

```bash
python3 -m betavibe resolve pre_spec --context "<task>"
python3 -m betavibe resolve pre_implement --context "<plan and files>"
python3 -m betavibe should-capture --debug-minutes 35 --attempts 3 --had-error-log --final-fix-verified --context "<bug summary>"
```

If capture is recommended, the agent asks you for approval in chat, then writes the insight.

## Human-facing commands, only when needed

Check relevant insights:

```bash
python3 -m betavibe advise "oauth line bot refresh token"
```

Capture a reviewed lesson:

```bash
python3 -m betavibe capture \
  --type pitfall \
  --title "LINE OAuth token refresh silently kills webhook" \
  --summary "Token rotation caused webhook delivery to stop until self-test revalidation was added." \
  --tags "oauth,line-bot,webhook" \
  --tech "node,line" \
  --symptom "Webhook stopped receiving events after token refresh." \
  --root-cause "Refresh flow updated credentials without revalidating delivery." \
  --wrong-paths "Rotating only the token did not prove webhook delivery still worked." \
  --fix "Add webhook self-test after token refresh and fail deploy if it does not pass." \
  --prevention-signal "Before deploying any LINE OAuth refresh flow, add or run webhook delivery self-test." \
  --verify-trigger "When LINE Messaging API auth behavior changes."
```

Scan a project’s evolution for candidate insights:

```bash
python3 -m betavibe scan-git /path/to/project --with-github --since "1 year ago"
python3 -m betavibe pending
python3 -m betavibe promote <pending-id>
```

Run the dogfood loop against a real repo and produce a usefulness report:

```bash
python3 -m betavibe dogfood /path/to/project --out /tmp/betavibe-dogfood.md
```

`dogfood` mines local git history, writes pending candidates, probes `pre_spec` and `pre_implement` resolver behavior, and emits a markdown report. It does not need GitHub, GBrain, or network access unless `--with-github` is explicitly passed.

## Insight types

- `pitfall`: hard-won bug / failure mode and verified fix.
- `decision`: choice among options and accepted trade-offs.
- `pattern`: reusable implementation / delivery pattern.
- `tool_choice`: when to use OpenClaw / Claude Code / Codex / Cowork / local scripts / browser / APIs.
- `spec_guardrail`: checklist item that should shape future specs.

## Why approval is required

Bad memory is worse than missing memory. Git history and agents can draft candidates, but only reviewed insights should enter `registry/insights/`.

## Hybrid with GBrain

Betavibe is the workflow / schema / resolver layer. GBrain is the semantic memory backend.

- `capture --sync-gbrain` writes reviewed insights to local markdown and GBrain when available.
- `resolve` searches local reviewed insights and also queries GBrain semantic memory unless `--no-gbrain` is passed.
- Local markdown remains the source of truth; GBrain improves recall across wording, projects, and related concepts.

## Testing whether it is useful

Read `docs/USEFULNESS_TESTING.md`. The short version: test against old painful bugs and compare resolver-assisted vs non-assisted agents. If it only creates nicer notes but does not avoid wrong paths, improve it or kill it.

## Key files

- `AGENTS.md` — main drop-in instructions for all agents.
- `CLAUDE.md`, `.claude/CLAUDE.md` — Claude Code entrypoints.
- `.codex/AGENTS.md` — Codex entrypoint.
- `COWORK.md` — Cowork-readable guidance.
- `docs/RESOLVERS.md` — lifecycle resolver behavior.
- `docs/USEFULNESS_TESTING.md` — A/B tests for real usefulness.
- `skills/betavibe-insight/SKILL.md` — bundled agent skill for correct capture workflow.
- `.betavibe/hooks/` after install — deterministic wrappers agents/hooks can call.
- `docs/OPENCLAW_LIFECYCLE.md` — optional OpenClaw plugin integration for automatic resolver/capture lifecycle hooks.
- `betavibe/` — resolver CLI.
- `registry/insights/` — reviewed insight database.
- `registry/pending/` — auto-mined candidates awaiting review.
