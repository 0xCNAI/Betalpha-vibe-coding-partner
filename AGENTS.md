# Betalpha Vibe Coding Partner — Drop-in Agent Contract

This folder is a **drop-in resolver pack** for coding agents. If you are Codex, Claude Code, OpenClaw, Cowork, Cursor, or another code tool and you can read this file, you must use the local insight registry automatically.

The human should not need to remember CLI commands.

## Mental model

The registry stores **hard-won development insights**:

- bugs that took meaningful debugging time
- final verified fixes
- wrong paths that wasted time
- decisions / tool choices that changed delivery stability
- spec guardrails that should prevent repeat failures

Do **not** store routine notes, guesses, generic advice, or raw chat logs.

## Resolver lifecycle

Use these resolvers at the natural points in your work.

### 1. `pre_spec` — before writing a spec

When you are about to design a feature, integration, migration, automation, infra change, or non-trivial refactor:

```bash
python3 -m betavibe resolve pre_spec --context "<concrete task, files, tools, APIs, error messages>"
```

Then:

1. Read the top relevant insight files.
2. Convert relevant `prevention_signal` fields into spec checklist items.
3. Adjust tool choice / architecture if the insight clearly applies.
4. Mention only meaningful hits to the human. Do not spam loose matches.

### 2. `pre_implement` — before editing code

Before changing code for a non-trivial task:

```bash
python3 -m betavibe resolve pre_implement --context "<implementation plan + touched files>"
```

Use results to avoid known wrong paths and pick stable tools.

### 3. `post_debug` — after solving a painful bug

When a session involved substantial debugging, failed attempts, repeated errors, rollback, CI failure, migration issue, auth/config/deploy issue, or any “we finally found it” moment:

```bash
python3 -m betavibe should-capture \
  --debug-minutes <minutes> \
  --attempts <number of wrong attempts> \
  --had-error-log \
  --final-fix-verified \
  --context "<short summary>"
```

If the output says `CAPTURE_RECOMMENDED`, ask the human in conversation:

> This looks like a hard-won debugging lesson. Want me to extract it into Betalpha Vibe Coding Partner? I’ll draft the insight and you approve before it’s saved.

Only write after approval.

### 4. `post_session` — end of meaningful coding session

If the work produced a reusable lesson but was not a bug, ask whether to capture a `decision`, `pattern`, `tool_choice`, or `spec_guardrail`.

## Conversational approval flow

When capture is warranted, do not ask the human to run commands. You ask concise questions, then run the command yourself.

Minimum questions:

1. Symptom: what actually broke / what was confusing?
2. Root cause: what was the real cause, not just the trigger?
3. Wrong paths: what did we try that did not work?
4. Final fix: what solution was verified?
5. Prevention signal: when should a future agent remember this?
6. Verify trigger: what future change could make this stale?

Then write:

```bash
python3 -m betavibe capture ...
```

If the human says “yes, save it” but some fields are inferable from the session, prefill them and ask only what is missing.

## Quality gate — strict

Capture only if at least one is true:

- debugging took ~20+ minutes
- 2+ wrong paths were tried
- a specific error/log/failed behavior was observed
- final fix was verified by test/build/run/manual reproduction
- issue touched risky systems: auth, token, billing, deploy, CI, cron, database migration, schema, config, data loss, external APIs
- the insight would change a future spec or tool choice

Reject or defer capture if:

- the lesson is generic
- the fix is not verified
- root cause is unknown
- it is just a preference without trade-offs
- it would not help a future agent act differently

## Required before claiming done

For code changes to this repository, run:

```bash
python3 -m unittest discover -s tests -v
```

## Registry paths

- Reviewed insights: `registry/insights/**/INSIGHT.md`
- Auto-mined candidates: `registry/pending/*.json`
- Schema: `registry/schema/INSIGHT_SCHEMA.md`

Use `BETAVIBE_REGISTRY` if set. Otherwise use local `registry/`.
