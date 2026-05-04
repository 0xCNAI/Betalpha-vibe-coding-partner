# Claude Code Local Instructions

Follow `../AGENTS.md`.

Use lifecycle resolvers automatically:

```bash
python3 -m betavibe spec-start --task "<task>" --context "<task>" --out specs/<name>.md
python3 -m betavibe resolve pre_spec --context "<task>"
python3 -m betavibe spec-validate specs/<name>.md
python3 -m betavibe implement-start --spec specs/<name>.md
python3 -m betavibe resolve pre_implement --context "<plan/files>"
python3 -m betavibe should-capture --debug-minutes <n> --attempts <n> --had-error-log --final-fix-verified --context "<bug>"
```

For bug/debug work, prefer the installed hooks so Betavibe records fail→fix→pass evidence:

```bash
.betavibe/hooks/verify.sh --task "<task>" --no-fail -- <failing command>
.betavibe/hooks/verify.sh --task "<task>" -- <passing verification>
.betavibe/hooks/learn.sh
```

When capture is recommended, ask the human for approval and save only reviewed, verified insights.
Never promote pending lessons or sync GBrain without human approval.
