# Resolvers

Resolvers are simple lifecycle hooks that any coding agent can call after reading this project folder.

They are not magic background daemons. They are a shared contract:

- agent recognizes a work phase
- agent calls the matching resolver
- resolver returns relevant prior insights and next actions
- agent applies them to spec / implementation / capture flow

## Resolver phases

### `pre_spec`

Use before writing or revising a spec.

Goal: prevent bad direction early.

Output should affect:

- requirements
- architecture
- tool choice
- verification plan
- known risky subsystems

### `pre_implement`

Use before editing code.

Goal: avoid known wrong paths and pick stable implementation tactics.

Output should affect:

- file checklist
- test plan
- migration / deployment order
- API / browser / local-script tool choice

### `post_debug`

Use after a bug is solved.

Goal: decide whether the session deserves a reviewed insight.

A capture-worthy session usually includes:

- meaningful time lost
- concrete error / log / observed failure
- multiple failed attempts
- verified final fix
- risky subsystem

### `post_session`

Use after non-bug sessions that still produced reusable knowledge.

Examples:

- chose Codex over Claude Code for a certain refactor class
- learned a spec should always include rollout checklist for migration work
- discovered a stable pattern for GitHub Actions release gates

## Commands

```bash
python3 -m betavibe resolve pre_spec --context "<task>"
python3 -m betavibe resolve pre_implement --context "<plan>"
python3 -m betavibe should-capture --debug-minutes 35 --attempts 3 --had-error-log --final-fix-verified --context "<bug>"
```

## Agent behavior

If resolver finds relevant insights:

1. Read the full `INSIGHT.md` file.
2. Quote only the relevant `prevention_signal` to the human.
3. Apply it, do not just report it.
4. If stale, verify before relying.

If `should-capture` recommends capture:

1. Draft fields from session context.
2. Ask the human for approval.
3. Ask only missing judgment fields.
4. Run `capture`.
5. Report the path written.
