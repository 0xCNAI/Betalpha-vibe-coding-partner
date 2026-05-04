# Claude Code Usage

Read `AGENTS.md` first.

Do not wait for the human to remember commands. Automatically call:

- `python3 -m betavibe resolve pre_spec --context "..."` before specs
- `python3 -m betavibe resolve pre_implement --context "..."` before non-trivial edits
- `.betavibe/hooks/verify.sh --task "<task>" --no-fail -- <failing command>` when reproducing a bug
- `.betavibe/hooks/verify.sh --task "<task>" -- <passing verification>` after the fix
- `.betavibe/hooks/learn.sh` after a verified fail→pass debug cycle; this creates pending only
- `python3 -m betavibe should-capture ...` after painful debugging

If capture is recommended, ask for conversational approval and then save the reviewed insight with `capture`.
Never promote pending lessons or sync GBrain without human approval.
