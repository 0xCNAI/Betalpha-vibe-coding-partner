# BLOCKED_G4

G4 is blocked because the required real-world transfer evidence does not exist yet, and the acceptance criteria explicitly prohibit fake numbers.

## Objective

G4 requires a reality checkpoint:

- Excavate at least 30 `transferable_pattern` insights from `/Users/betalpha/clawd`.
- Install Betavibe in a clean test repo from a different domain, not `clawd`.
- Run at least 10 real spec-implement-debug cycles over at least 2 weeks of actual vibecoding.
- Cover Tino and Jonathan across Claude Code, Codex, and OpenClaw.
- Write `docs/REAL_WORLD_TRANSFER_REPORT.md`.
- Store all evidence in `tests/real_world_g4/`.

## Evidence Present

- Reviewed insights available: 69.
- G2 schema migration verified all 69 reviewed insights have non-empty `concrete_evidence` and `transferable_pattern`.
- The clawd excavation/promote work satisfies the insight-count prerequisite.

## Missing Evidence

- No `tests/real_world_g4/` evidence directory exists.
- No `docs/REAL_WORLD_TRANSFER_REPORT.md` exists.
- No clean different-domain test repo has been documented for G4.
- No 2-week observation window has elapsed inside this work session.
- No 10 real spec-implement-debug cycles have been recorded.
- No Tino and Jonathan signoff exists.
- No cross-harness evidence across Claude Code, Codex, and OpenClaw exists.

## Acceptance Status

| Check | Status |
| --- | --- |
| Cross-project hit_rate >=25% | BLOCKED: no real cycles recorded |
| Avoided-pitfall count >=5 | BLOCKED: no real cycles recorded |
| Repeated-pitfall count <=2 | BLOCKED: no real cycles recorded |
| Both Tino and Jonathan mark "would keep using" | BLOCKED: no signoff recorded |
| All evidence in `tests/real_world_g4/` | BLOCKED: directory missing |

## Stop Condition

Per the production-readiness goal, G5 must not start while G4 is blocked.

Do not replace this with synthetic tests. G4 is intentionally a real-world checkpoint.

## Next Required Input

Run a real G4 trial over at least 2 weeks in a clean repo from a different domain. Record each cycle under `tests/real_world_g4/` with:

- date/time
- actor: Tino or Jonathan
- harness: Claude Code, Codex, or OpenClaw
- task/spec
- returned insights
- whether each insight was applied, ignored, or false_positive
- avoided pitfall evidence
- repeated pitfall evidence
- verification result

After at least 10 cycles, compute the G4 metrics and write `docs/REAL_WORLD_TRANSFER_REPORT.md`.
