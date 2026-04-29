# Cowork Instructions

Use the markdown registry and resolver lifecycle described in `AGENTS.md`.

If shell access is available, run:

```bash
python3 -m betavibe resolve pre_spec --context "<task>"
python3 -m betavibe resolve pre_implement --context "<plan/files>"
python3 -m betavibe should-capture ...
```

If shell access is unavailable, read `registry/insights/**/INSIGHT.md` directly and search by tags, summaries, and prevention signals.

Never save unverified or generic notes as reviewed insights.
