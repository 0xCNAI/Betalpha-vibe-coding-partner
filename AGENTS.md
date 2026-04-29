# Betalpha Vibe Coding Partner — Agent Instructions

This repo contains a reusable insight registry for coding agents.

## Mandatory workflow for coding agents

Before writing a spec, changing architecture, debugging a non-trivial issue, or choosing tools, run:

```bash
python3 -m betavibe advise "<concrete task keywords>" --registry "${BETAVIBE_REGISTRY:-registry}"
```

Use concrete keywords: package names, API names, error messages, file paths, framework names.

If relevant insights appear:

1. Read the referenced markdown file.
2. Apply the `prevention_signal` as a checklist item.
3. If an insight is stale, verify it before relying on it.
4. Do not blindly obey old insights; treat them as evidence.

After a session that produced a reusable lesson, create a reviewed insight:

```bash
python3 -m betavibe capture \
  --type pitfall \
  --title "short concrete title" \
  --tags "api,auth,node" \
  --tech "node,line" \
  --symptom "what failed" \
  --root-cause "actual cause" \
  --fix "verified fix" \
  --prevention-signal "when future agents should remember this" \
  --verify-trigger "what would make this stale"
```

## Do not

- Do not dump raw chat logs as insights.
- Do not promote auto-mined candidates without review.
- Do not write vague titles like “remember cron issue”.
- Do not modify insight schema casually; update tests and docs first.

## Quality bar

An insight is useful only if a future agent can answer:

- When should this be surfaced?
- What exact failure / trade-off happened?
- What was tried and failed?
- What fixed or improved it?
- How do we know if it is stale?
