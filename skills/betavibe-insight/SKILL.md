---
name: betavibe-insight
description: Use for coding/spec/debug workflows in projects with Betalpha Vibe Coding Partner: run pre-spec/pre-implementation resolvers, validate specs, capture fail→fix→pass verification, decide whether hard-won debugging lessons should become pending/reviewed insights, and sync approved insights to GBrain. Trigger on spec drafting, implementation planning, non-trivial migrations/config changes, painful debugging, finally fixed/root cause/wrong attempts, CI/deploy/auth/database/schema/webhook/cron/external API issues, retrospective, or insight capture.
---

# Betavibe Insight

Use this skill when a repo contains Betalpha Vibe Coding Partner, a `.betavibe/` directory, Betavibe hooks, or a Betavibe agent contract block.

## Core rule

Do not rely on the human to remember Betavibe. You decide when to run it, apply the output, and verify the final code path before claiming done.

## Vendored pack / registry rule

When Betavibe is installed as a vendored pack, commands often need to run from the pack directory so `python3 -m betavibe` imports the bundled module. Always pass the host project registry explicitly so evidence and insights land in the project, not in the vendor repo.

Preferred pattern:

```bash
PROJECT_ROOT="/path/to/host-project"
cd "$PROJECT_ROOT/Betalpha-vibe-coding-partner"  # or vendor/Betalpha-vibe-coding-partner
python3 -m betavibe --registry "$PROJECT_ROOT/.betavibe/registry" resolve pre_implement --context "<task>"
```

Wrong path: `cd vendor/Betalpha-vibe-coding-partner && python3 -m betavibe ...` without `--registry`; that writes telemetry/pending data into the pack repo or default cwd-relative registry and future agents may miss it.

## Before spec

Before drafting a non-trivial spec, run:

```bash
python3 -m betavibe --registry .betavibe/registry resolve pre_spec --context "<task, APIs, files, tools, risks>"
```

Apply the output to the spec:

- `Spec guardrails` → requirements/checklist
- `Known wrong paths` → non-goals / avoided approaches
- `Tools to prefer / avoid` → implementation strategy
- `Verification requirements` → acceptance criteria

## Before implementation

Before non-trivial code edits, run:

```bash
python3 -m betavibe --registry .betavibe/registry resolve pre_implement --context "<implementation plan and touched files>"
```

Use results to adjust file plan, tests, migration/deploy sequence, and tool choice. Do not merely mention the output; apply it.

## Verification capture

For coding/debug work, keep a compact fail→fix→pass trail:

1. failing symptom or issue requirement;
2. changed files / final fix;
3. verification command or manual reproduction gate;
4. final pass/fail result.

Minimum gate before done: unit test, integration test, build, lint/typecheck, CLI smoke, or manual reproduction. If no gate can run, say why.

## After painful debugging

For bug/debug work, prefer capturing the reproduction and final verification through the installed hook instead of running bare test commands:

```bash
.betavibe/hooks/verify.sh --task "<task>" --no-fail -- <failing reproduction/test/build command>
.betavibe/hooks/verify.sh --task "<task>" -- <passing verification command>
```

After the fix is verified, run:

```bash
.betavibe/hooks/learn.sh
```

`learn` creates a review-only pending lesson. It must not promote reviewed insights or sync GBrain without human approval.

Run `should-capture` when any of these happened:

- ~20+ minutes debugging
- 2+ wrong attempts
- concrete error/log/failed behavior
- final fix verified by test/build/run/manual reproduction
- risky subsystem: auth, token, billing, deploy, CI, cron, database migration, schema, config, data loss, external APIs, webhook
- future spec/tool choice would change

Example:

```bash
python3 -m betavibe --registry .betavibe/registry should-capture \
  --debug-minutes 45 \
  --attempts 2 \
  --had-error-log \
  --final-fix-verified \
  --context "webhook callbacks stopped after token refresh; fixed by end-to-end delivery self-test"
```

Interpretation:

- `CAPTURE_RECOMMENDED`: ask approval, then capture.
- `CAPTURE_AFTER_VERIFICATION`: do not save yet; verify final fix first.
- `DO_NOT_CAPTURE_YET`: do not pollute registry.

## Approval flow

If capture is recommended, ask:

> This looks like a hard-won debugging lesson. Want me to save it as a Betavibe insight? I’ll draft it from the session and ask only for missing fields.

Never write reviewed insights without approval.

Minimum fields:

1. symptom: actual failure / log / behavior
2. root cause: actual cause, not just trigger
3. wrong paths: tried but failed
4. final fix: verified solution
5. prevention signal: when future agents should remember this
6. verify trigger: what could make it stale

Then run `capture --sync-gbrain` only after approval.

If the final verification was captured but the original failure happened outside Betavibe, run `learn --force-pending` only after the human confirms the lesson is reusable. This creates a pending review draft, not a reviewed insight.

## Quality bar

Only capture hard-won, verified, reusable lessons. Reject routine edits, generic advice, guesses, unverified fixes, and notes that would not help a future agent act differently.
