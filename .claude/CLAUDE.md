# Claude Code Local Instructions

Follow `../AGENTS.md`.

Use lifecycle resolvers automatically:

```bash
python3 -m betavibe resolve pre_spec --context "<task>"
python3 -m betavibe resolve pre_implement --context "<plan/files>"
python3 -m betavibe should-capture --debug-minutes <n> --attempts <n> --had-error-log --final-fix-verified --context "<bug>"
```

When capture is recommended, ask the human for approval and save only reviewed, verified insights.
