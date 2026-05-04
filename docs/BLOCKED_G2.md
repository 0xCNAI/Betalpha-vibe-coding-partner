# BLOCKED_G2

G2 is blocked by an impossible acceptance threshold after the accepted G0 baseline.

## Objective

G2 requires local semantic search plus a two-layer schema:

- Bake MiniLM-L6-v2 into the pack with size <=30MB.
- Auto-embed captures into `registry/insights/embeddings.sqlite`.
- Require `concrete_evidence`, `transferable_pattern`, and domain metadata on every insight.
- Add hybrid retrieval over semantic pattern search plus tag/tech filters.
- Add `migrate-schema`.
- Pass benchmark gates against the G0 baseline.

## Failed Attempts

1. Checked local MiniLM artifacts.
   - Found `/Users/betalpha/.cache/chroma/onnx_models/all-MiniLM-L6-v2`.
   - It is 166MB total, with `model.onnx` at 86MB and `onnx.tar.gz` at 79MB.
   - This does not satisfy the <=30MB baked-pack requirement.

2. Tried quantizing the local ONNX model.
   - `onnxruntime.quantization` failed because the `onnx` Python package was missing.
   - Installed `onnx==1.16.2` into `/tmp/betavibe_onnx_pkg` as a temporary build dependency.
   - Quantization then produced `models/minilm-l6-v2/model.int8.onnx` at 22,869,075 bytes and total model pack bytes of 23,813,537.
   - This shows the size gate is technically feasible, but the generated model was not enough to satisfy the benchmark gate below.

3. Audited the G2 benchmark threshold against G0.
   - G0 accepted baseline hit_rate: `0.7205882352941176`.
   - G2 says hit_rate must improve `>=50% relative to G0`.
   - Required hit_rate would be `0.7205882352941176 * 1.5 = 1.0808823529411764`.
   - A hit_rate cannot exceed `1.0`.

## Blocker

The G2 acceptance criterion is mathematically impossible with the accepted G0 baseline.

```text
required_hit_rate = 108.09%
maximum_possible_hit_rate = 100.00%
```

## Required Decision

Pick one replacement threshold before G2 can continue:

1. Improve hit_rate by at least 50% of the remaining gap to 100%.
   - Required: `0.7205882352941176 + (1 - 0.7205882352941176) * 0.5 = 0.8602941176470589`.
2. Improve absolute hit_rate by at least 5 percentage points without increasing false positives by more than 5pp.
   - Required: `>=0.7705882352941177`.
3. Re-run G0 with a stricter classifier that produces a lower baseline, then use the original relative-improvement threshold.

## Stop Condition

Per the goal instructions, G3 must not start while G2 is blocked.

## Resolution

Resolved by G0-redo on 2026-05-04.

The original G0 baseline was invalid because it used a 1-insight registry and a permissive classifier. G0-redo populated 30 reviewed insights, added 10% NULL-control cases, tightened hit classification around `prevention_signal` overlap with `actual_pitfall`, and produced a valid overall hit_rate baseline of 17.33%.

G2 may resume against the valid target:

```text
0.17333333333333334 * 1.5 = 0.26
```

Follow-up: G2 subsequently passed against the valid G0-redo target. See `docs/BENCHMARKS.md` for the PASS metrics.
