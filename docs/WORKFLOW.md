# Workflow

## 1. Before spec

Run the pre-spec resolver with concrete task context. If hits appear, read the relevant insight file and convert prevention signals into spec checklist items, verification gates, and explicit non-goals for known wrong paths.

```bash
python3 -m betavibe resolve pre_spec --context "<task, APIs, files, tools, risks>"
```

## 2. Before implementation

Run the pre-implementation resolver before non-trivial edits. Apply the output to the file plan, tool choice, migration/deploy order, and verification plan.

```bash
python3 -m betavibe resolve pre_implement --context "<plan and touched files>"
```

## 3. During debugging

Capture meaningful verification commands through Betavibe so a fail -> fix -> pass cycle leaves evidence. Installed projects can use `.betavibe/hooks/verify.sh` from any harness:

```bash
.betavibe/hooks/verify.sh --task "fix auth bootstrap" --no-fail -- npm test
.betavibe/hooks/verify.sh --task "fix auth bootstrap" -- npm test
```

If the run contains failed command evidence plus later passing verification, create a review-only pending lesson:

```bash
.betavibe/hooks/learn.sh
```

Never promote pending lessons into reviewed insights without human approval.

## 4. End of work

Use `should-capture` or `learn` for reviewable drafts. Use `capture` or `promote` only after human approval. If the lesson comes from old project history, run `scan-git` or `excavate`, inspect candidates, then `promote` only the useful ones.

## 5. Existing GitHub project onboarding

```bash
python3 -m betavibe scan-git ~/project --since "1 year ago" --registry ~/.betalpha-vibe/registry
python3 -m betavibe pending --registry ~/.betalpha-vibe/registry
python3 -m betavibe promote <id> --registry ~/.betalpha-vibe/registry
```

Git log alone cannot know the full root cause. Promotion is intentionally reviewable.
