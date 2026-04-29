# Workflow

## 1. Start of work

Run `advise` with task keywords. If hits appear, read the insight file and convert prevention signals into checklist items.

## 2. During work

If you hit a repeated or non-obvious failure, keep notes under symptom / root cause / wrong paths / fix.

## 3. End of work

Use `capture` for reviewed insights. If the lesson comes from old project history, run `scan-git`, inspect candidates, then `promote` only the useful ones.

## 4. Existing GitHub project onboarding

```bash
python3 -m betavibe scan-git ~/project --since "1 year ago" --registry ~/.betalpha-vibe/registry
python3 -m betavibe pending --registry ~/.betalpha-vibe/registry
python3 -m betavibe promote <id> --registry ~/.betalpha-vibe/registry
```

Git log alone cannot know the full root cause. Promotion is intentionally reviewable.
