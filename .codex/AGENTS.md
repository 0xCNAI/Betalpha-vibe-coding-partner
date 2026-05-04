# Codex Instructions

Follow `../AGENTS.md`.

Before specs or implementation, call the resolver commands instead of waiting for the user:

```bash
python3 -m betavibe resolve pre_spec --context "<task>"
python3 -m betavibe resolve pre_implement --context "<plan/files>"
```

After substantial debugging, call `should-capture`. If it recommends capture, ask the human for approval, then write the reviewed insight with `capture`.

During bug/debug work, run the reproduction and final verification through Betavibe instead of bare test commands:

```bash
.betavibe/hooks/verify.sh --task "<task>" --no-fail -- <failing command>
.betavibe/hooks/verify.sh --task "<task>" -- <passing verification>
.betavibe/hooks/learn.sh
```

`learn` creates pending only. Do not promote or sync GBrain without human approval.
