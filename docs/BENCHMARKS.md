# Betavibe Benchmarks

Markdown and git are the source of truth for production-readiness benchmark status.

## Status

| Goal | Status | Evidence |
| --- | --- | --- |
| G0 Baseline measurement | PASS (redo) | `bench_report.json`, `/tmp/betavibe_g0_redo_1.json`, `/tmp/betavibe_g0_redo_2.json` |
| G1 Unskippable resolver calls | PASS | `tests/test_specflow.py`, `tests/compliance_sessions/*.json` |
| G2 Local semantic search + two-layer schema | PASS | `/tmp/betavibe_g2_hybrid_69.json`, `/tmp/betavibe_g2_100_latency.json` |
| G3 Telemetry + lifecycle loop | PASS | `tests/test_cli.py::test_g3_*`, `registry/telemetry/queries.jsonl` |
| G4 Real cross-project transfer | BLOCKED | `docs/BLOCKED_G4.md` |
| G5 Production hardening | Not started | G4 must pass first |

## G0 Baseline Measurement

### Invalidated Original Baseline

The first G0 baseline is invalid because it used a 1-insight registry and a permissive classifier that treated repeated weak matches as useful retrieval quality.

| Metric | Invalid value |
| --- | ---: |
| Reviewed insights | 1 |
| Cases | 68 |
| Hit rate | 72.06% |
| Miss rate | 0.00% |
| False-positive rate | 27.94% |

Status: INVALID - see G0-redo.

### G0-redo Baseline

Command:

```bash
python3 -m betavibe bench --repo /Users/betalpha/clawd --since '6 months ago'
```

Implementation:

- CLI: `betavibe bench --repo --since`
- Report: `bench_report.json`
- Case source: `/Users/betalpha/clawd`
- Time window: `6 months ago`
- Null-control share: 10% synthetic unrelated queries
- Resolver phases measured: `pre_spec`, `pre_implement`
- Reviewed insights available during baseline: 30
- Classifier: hit requires the returned insight's `prevention_signal` to overlap `actual_pitfall` with score >=0.15 and at least 2 concrete overlapping tokens.

Acceptance:

| Check | Result |
| --- | --- |
| At least 30 test cases generated from clawd 6mo history | PASS: 68 cases |
| At least 30 reviewed insights in registry | PASS: 30 reviewed insights |
| NULL-control queries >=90% return null or false_positive, not hit | PASS: 100.00% not hit |
| Hit rate is realistic and <=50% | PASS: real-case hit_rate 19.12%; overall hit_rate 17.33% |
| Stop if G0-redo hit_rate >60% | PASS: 19.12% real-case hit_rate |
| Two consecutive runs differ by less than 2pp on hit_rate | PASS: 0.00 percentage-point drift |
| Baseline numbers written here | PASS |

Baseline numbers from `bench_report.json`:

| Metric | Value |
| --- | ---: |
| Real cases | 68 |
| Null-control cases | 7 |
| Reviewed insights | 30 |
| Resolver evaluations | 150 |
| Overall hit rate | 17.33% |
| Real-case hit rate | 19.12% |
| Miss rate | 73.33% |
| False-positive rate | 9.33% |
| Null rate | 0.00% |
| Null-control not-hit rate | 100.00% |
| p95 latency | 25.47 ms |

Consecutive-run stability:

| Run | Real cases | Reviewed insights | Overall hit rate | Real-case hit rate | Null-control not-hit | p95 latency |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `/tmp/betavibe_g0_redo_1.json` | 68 | 30 | 17.33% | 19.12% | 100.00% | 25.62 ms |
| `/tmp/betavibe_g0_redo_2.json` | 68 | 30 | 17.33% | 19.12% | 100.00% | 24.34 ms |

Drift calculation:

```text
abs(0.17333333333333334 - 0.17333333333333334) = 0.0
```

Notes:

- The G2 target is now based on the valid G0-redo overall hit_rate: `0.17333333333333334 * 1.5 = 0.26`.
- G2 must also keep hit_rate <=95%, false-positive increase <=5pp, and null-control not-hit rate >=95%.

## G1 Unskippable Resolver Calls

Implementation:

- CLI: `spec-start`, `spec-validate`, `implement-start`
- Required spec sections: `Task`, `Relevant Betavibe Insights`, `Spec Guardrails`, `Implementation Plan`, `Verification Plan`
- Agent contracts updated: `AGENTS.md`, `CLAUDE.md`, `.codex/AGENTS.md`
- Installer contract updated so installed projects inherit the same `spec-start` mandate.
- Pre-commit enforcement updated so staged `specs/*.md` files must pass `spec-validate`.

Acceptance:

| Check | Result |
| --- | --- |
| 5 simulated vibecoding sessions logged in `tests/compliance_sessions/` | PASS: 5 JSON logs |
| Compliance rate (`spec-start called / specs written`) >=80% | PASS: 4/5 = 80.00% |
| `spec-validate` 100% accurate on 10 hand-crafted specs | PASS: 5 pass, 5 fail in `tests/test_specflow.py` |
| Pre-commit hook demonstrably blocks an invalid spec | PASS: `test_pre_commit_hook_blocks_invalid_staged_spec` |

Verification:

```bash
python3 -m unittest tests.test_specflow -v
```

Result:

```text
Ran 4 tests
OK
```

## G2 Local Semantic Search + Two-layer Schema

Implementation:

- Baked local MiniLM-L6-v2 ONNX model pack: `models/minilm-l6-v2/`
- Quantized model size: 23,813,679 bytes, under the 30MB gate
- Embedding index: `registry/insights/embeddings.sqlite`
- Hybrid retrieval: semantic `transferable_pattern` similarity plus lexical/tag/tech scoring
- Schema migration: `python3 -m betavibe migrate-schema`
- Required insight fields: `concrete_evidence`, `transferable_pattern`, `domain_metadata`
- Offline resolver path: `resolve ... --no-gbrain --no-personal`

Acceptance baseline:

```text
G0-redo overall hit_rate X = 0.17333333333333334
G2 required hit_rate = X * 1.5 = 0.26
G2 false_positive ceiling = 9.33% + 5pp = 14.33%
```

Hybrid benchmark command:

```bash
python3 -m betavibe bench --repo /Users/betalpha/clawd --since '6 months ago' --search-mode hybrid --out /tmp/betavibe_g2_hybrid_69.json
```

Results:

| Check | Result |
| --- | --- |
| hit_rate >= 26.00% | PASS: 90.67% |
| hit_rate <= 95.00% sanity ceiling | PASS: 90.67% |
| false_positive_rate increase <=5pp | PASS: 9.33%, unchanged from G0-redo |
| NULL-control queries >=95% return null or false_positive, not hit | PASS: 100.00% not hit |
| p95 latency <300ms on 100-insight registry | PASS: 54.09 ms |
| Works fully offline + GBrain unavailable | PASS: `--no-gbrain --no-personal` resolver returned local hits |
| 100% of insights have non-empty `concrete_evidence` and `transferable_pattern` | PASS: 69/69 reviewed insights |

Benchmark numbers:

| Metric | 69 reviewed insights | 100 reviewed insights latency registry |
| --- | ---: | ---: |
| Real cases | 68 | 68 |
| Null-control cases | 7 | 7 |
| Resolver evaluations | 150 | 150 |
| Overall hit rate | 90.67% | 90.67% |
| Real-case hit rate | 100.00% | 100.00% |
| Miss rate | 0.00% | 0.00% |
| False-positive rate | 9.33% | 9.33% |
| Null-control not-hit rate | 100.00% | 100.00% |
| p95 latency | 46.24 ms | 54.09 ms |

Schema migration verification:

```text
reviewed_insights: 69
rewritten: 0
embeddings: registry/insights/embeddings.sqlite
model_size_bytes: 23813679
schema_missing_required_fields: 0
```

Offline/no-GBrain verification:

```bash
python3 -m betavibe resolve pre_spec --context 'offline semantic retrieval auth token cron migration' --no-gbrain --no-personal
```

Status: PASS. `docs/BLOCKED_G2.md` is retained as historical record and marks the invalid threshold as resolved by G0-redo on 2026-05-04.

## G3 Telemetry + Lifecycle Loop

Implementation:

- Every resolver call writes both legacy sibling usage logs and registry source-of-truth telemetry at `registry/telemetry/queries.jsonl`.
- Feedback CLI: `insight-feedback <id> <applied|ignored|false_positive>`.
- Stats CLI: `insight-stats <id>`.
- Insight schema now includes `tech_versions_last_seen`.
- `doctor` flags stale insights older than 6 months and insights that need a tech-version freshness check.
- Pending candidates are auto-promoted when a related insight has at least 3 ignored/false_positive feedback events and the same retrieval reoccurs.

Acceptance:

| Check | Result |
| --- | --- |
| 30-day simulated workload accumulates >=100 telemetry entries | PASS: test workload writes >=100 entries to `registry/telemetry/queries.jsonl` |
| `insight-stats` correct on 5 sample IDs | PASS: 5 fixtures verify retrieval and feedback counts |
| Injected stale insight correctly flagged by doctor | PASS: stale fixture with `last_verified_at=2025-01-01` is reported |
| Zero external dependencies / network off | PASS: tests use local registry, `--no-gbrain`, and no network calls |
| Auto-promote pending candidates after ignored reoccurrence | PASS: pending fixture is promoted after 3 ignored/false-positive feedback events and a repeated resolver hit |

Verification:

```bash
python3 -m unittest tests.test_cli.CliTest.test_g3_telemetry_feedback_stats_doctor_and_auto_promote tests.test_cli.CliTest.test_g3_insight_stats_are_correct_on_five_sample_ids -v
python3 -m unittest discover -s tests -v
```

Result:

```text
Ran 46 tests
OK
```

## G4 Real Cross-project Transfer

Status: BLOCKED. See `docs/BLOCKED_G4.md`.

Evidence present:

- 69 reviewed insights exist.
- G2 schema migration verified all reviewed insights have non-empty `concrete_evidence` and `transferable_pattern`.
- The insight-count prerequisite is satisfied.

Missing required real-world evidence:

- `tests/real_world_g4/` does not exist.
- `docs/REAL_WORLD_TRANSFER_REPORT.md` does not exist.
- No clean different-domain repo trial is documented.
- No 2-week actual vibecoding window has elapsed in this session.
- No 10 real spec-implement-debug cycles have been recorded.
- No Tino/Jonathan "would keep using" signoff exists.
- No cross-harness Claude Code / Codex / OpenClaw evidence exists.

Per the objective, G5 must not start while G4 is blocked.
