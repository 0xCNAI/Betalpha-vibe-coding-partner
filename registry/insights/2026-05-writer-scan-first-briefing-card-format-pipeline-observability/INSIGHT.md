---
{
  "title": "writer SCAN-first: briefing card format + pipeline observability",
  "type": "spec_guardrail",
  "tags": [
    "test"
  ],
  "tech_stack": [
    "python"
  ],
  "summary": "Git history candidate from `clawd` commit `460f8e0d3ae1`: writer SCAN-first: briefing card format + pipeline observability",
  "prevention_signal": "Before modifying `research/data/runtime/pipelines/alpha-distil/2026-03-26T18-55-08+0800-alpha-distil-9028b4/artifacts/route/route_decisions.json` or adjacent subsystem, search this registry and inspect the original fixing commit.",
  "verify_trigger": "When the touched subsystem, framework version, or deployment environment changes.",
  "concrete_evidence": "{\n  \"commit\": \"460f8e0d3ae13198753baa66133ba735bdfd185d\",\n  \"files\": [\n    \"jonathan/skills/threads-scout/data/current_recommendations.md\",\n    \"jonathan/skills/threads-scout/data/keywords.md\",\n    \"jonathan/skills/threads-scout/data/recommended_history.md\",\n    \"research/data/pipeline_events.jsonl\",\n    \"research/data/runtime/event_chains.json\",\n    \"research/data/runtime/pipelines/alpha-distil/2026-03-26T18-55-08+0800-alpha-distil-9028b4/artifacts/fetch/defillama_items.json\",\n    \"research/data/runtime/pipelines/alpha-distil/2026-03-26T18-55-08+0800-alpha-distil-9028b4/artifacts/fetch/docs_items.json\",\n    \"research/data/runtime/pipelines/alpha-distil/2026-03-26T18-55-08+0800-alpha-distil-9028b4/artifacts/fetch/governance_items.json\",\n    \"research/data/runtime/pipelines/alpha-distil/2026-03-26T18-55-08+0800-alpha-distil-9028b4/artifacts/fetch/manifest.json\",\n    \"research/data/runtime/pipelines/alpha-distil/2026-03-26T18-55-08+0800-alpha-distil-9028b4/artifacts/fetch/manifest.json.meta.json\",\n    \"research/data/runtime/pipelines/alpha-distil/2026-03-26T18-55-08+0800-alpha-distil-9028b4/artifacts/fetch/x_items.json\",\n    \"research/data/runtime/pipelines/alpha-distil/2026-03-26T18-55-08+0800-alpha-distil-9028b4/artifacts/ingest/fast_ingest.json\",\n    \"research/data/runtime/pipelines/alpha-distil/2026-03-26T18-55-08+0800-alpha-distil-9028b4/artifacts/ingest/fast_ingest.json.meta.json\",\n    \"research/data/runtime/pipelines/alpha-distil/2026-03-26T18-55-08+0800-alpha-distil-9028b4/artifacts/pool/upsert_result.json\",\n    \"research/data/runtime/pipelines/alpha-distil/2026-03-26T18-55-08+0800-alpha-distil-9028b4/artifacts/pool/upsert_result.json.meta.json\",\n    \"research/data/runtime/pipelines/alpha-distil/2026-03-26T18-55-08+0800-alpha-distil-9028b4/artifacts/route/cluster_route.json\",\n    \"research/data/runtime/pipelines/alpha-distil/2026-03-26T18-55-08+0800-alpha-distil-9028b4/artifacts/route/cluster_route.json.meta.json\",\n    \"research/data/runtime/pipelines/alpha-distil/2026-03-26T18-55-08+0800-alpha-distil-9028b4/artifacts/route/route_decisions.json\",\n    \"research/data/runtime/pipelines/alpha-distil/2026-03-26T18-55-08+0800-alpha-distil-9028b4/artifacts/route/route_decisions.json.meta.json\",\n    \"research/data/runtime/pipelines/alpha-distil/2026-03-26T18-55-08+0800-alpha-distil-9028b4/manifest.json\"\n  ],\n  \"reasons\": [\n    \"touches risky subsystem: research/data/runtime/pipelines/alpha-distil/2026-03-26T18-55-08+0800-alpha-distil-9028b4/artifacts/route/route_decisions.json, research/data/runtime/pipelines/alpha-distil/2026-03-26T18-55-08+0800-alpha-distil-9028b4/artifacts/route/route_decisions.json.meta.json, research/data/runtime/pipelines/alpha-distil/2026-03-26T19-55-07+0800-alpha-distil-6dc229/artifacts/route/route_decisions.json, research/data/runtime/pipelines/alpha-distil/2026-03-26T19-55-07+0800-alpha-distil-6dc229/artifacts/route/route_decisions.json.meta.json\",\n    \"large change set: 94 files\"\n  ]\n}",
  "transferable_pattern": "Before modifying `research/data/runtime/pipelines/alpha-distil/2026-03-26T18-55-08+0800-alpha-distil-9028b4/artifacts/route/route_decisions.json` or adjacent subsystem, search this registry and inspect the original fixing commit.",
  "domain_metadata": {
    "tags": [
      "test"
    ],
    "tech_stack": [
      "python"
    ],
    "source_kind": "git_commit"
  },
  "tech_versions_last_seen": {},
  "created_at": "2026-05-04",
  "last_verified_at": "2026-05-04",
  "source": {
    "kind": "git_commit",
    "repo": "/Users/betalpha/clawd",
    "sha": "460f8e0d3ae13198753baa66133ba735bdfd185d",
    "date": "2026-03-26T20:11:45+08:00",
    "files": [
      "jonathan/skills/threads-scout/data/current_recommendations.md",
      "jonathan/skills/threads-scout/data/keywords.md",
      "jonathan/skills/threads-scout/data/recommended_history.md",
      "research/data/pipeline_events.jsonl",
      "research/data/runtime/event_chains.json",
      "research/data/runtime/pipelines/alpha-distil/2026-03-26T18-55-08+0800-alpha-distil-9028b4/artifacts/fetch/defillama_items.json",
      "research/data/runtime/pipelines/alpha-distil/2026-03-26T18-55-08+0800-alpha-distil-9028b4/artifacts/fetch/docs_items.json",
      "research/data/runtime/pipelines/alpha-distil/2026-03-26T18-55-08+0800-alpha-distil-9028b4/artifacts/fetch/governance_items.json",
      "research/data/runtime/pipelines/alpha-distil/2026-03-26T18-55-08+0800-alpha-distil-9028b4/artifacts/fetch/manifest.json",
      "research/data/runtime/pipelines/alpha-distil/2026-03-26T18-55-08+0800-alpha-distil-9028b4/artifacts/fetch/manifest.json.meta.json",
      "research/data/runtime/pipelines/alpha-distil/2026-03-26T18-55-08+0800-alpha-distil-9028b4/artifacts/fetch/x_items.json",
      "research/data/runtime/pipelines/alpha-distil/2026-03-26T18-55-08+0800-alpha-distil-9028b4/artifacts/ingest/fast_ingest.json",
      "research/data/runtime/pipelines/alpha-distil/2026-03-26T18-55-08+0800-alpha-distil-9028b4/artifacts/ingest/fast_ingest.json.meta.json",
      "research/data/runtime/pipelines/alpha-distil/2026-03-26T18-55-08+0800-alpha-distil-9028b4/artifacts/pool/upsert_result.json",
      "research/data/runtime/pipelines/alpha-distil/2026-03-26T18-55-08+0800-alpha-distil-9028b4/artifacts/pool/upsert_result.json.meta.json",
      "research/data/runtime/pipelines/alpha-distil/2026-03-26T18-55-08+0800-alpha-distil-9028b4/artifacts/route/cluster_route.json",
      "research/data/runtime/pipelines/alpha-distil/2026-03-26T18-55-08+0800-alpha-distil-9028b4/artifacts/route/cluster_route.json.meta.json",
      "research/data/runtime/pipelines/alpha-distil/2026-03-26T18-55-08+0800-alpha-distil-9028b4/artifacts/route/route_decisions.json",
      "research/data/runtime/pipelines/alpha-distil/2026-03-26T18-55-08+0800-alpha-distil-9028b4/artifacts/route/route_decisions.json.meta.json",
      "research/data/runtime/pipelines/alpha-distil/2026-03-26T18-55-08+0800-alpha-distil-9028b4/manifest.json",
      "research/data/runtime/pipelines/alpha-distil/2026-03-26T18-55-08+0800-alpha-distil-9028b4/receipts/fetch_sources.json",
      "research/data/runtime/pipelines/alpha-distil/2026-03-26T18-55-08+0800-alpha-distil-9028b4/receipts/ingest_signals.json",
      "research/data/runtime/pipelines/alpha-distil/2026-03-26T18-55-08+0800-alpha-distil-9028b4/receipts/pool_upsert.json",
      "research/data/runtime/pipelines/alpha-distil/2026-03-26T18-55-08+0800-alpha-distil-9028b4/receipts/score_and_route.json",
      "research/data/runtime/pipelines/alpha-distil/2026-03-26T18-55-08+0800-alpha-distil-9028b4/status.json",
      "research/data/runtime/pipelines/alpha-distil/2026-03-26T18-55-08+0800-alpha-distil-9028b4/summary.json",
      "research/data/runtime/pipelines/alpha-distil/2026-03-26T19-55-07+0800-alpha-distil-6dc229/artifacts/fetch/defillama_items.json",
      "research/data/runtime/pipelines/alpha-distil/2026-03-26T19-55-07+0800-alpha-distil-6dc229/artifacts/fetch/docs_items.json",
      "research/data/runtime/pipelines/alpha-distil/2026-03-26T19-55-07+0800-alpha-distil-6dc229/artifacts/fetch/governance_items.json",
      "research/data/runtime/pipelines/alpha-distil/2026-03-26T19-55-07+0800-alpha-distil-6dc229/artifacts/fetch/manifest.json"
    ]
  }
}
---

## Symptom

Commit message suggests a potential lesson: writer SCAN-first: briefing card format + pipeline observability

## Root Cause

Review the commit diff / PR discussion before promotion.

## Wrong Paths

Unknown from git log alone.

## Fix

Inspect with: git show --stat --patch 460f8e0d3ae13198753baa66133ba735bdfd185d

## Evidence

{
  "commit": "460f8e0d3ae13198753baa66133ba735bdfd185d",
  "files": [
    "jonathan/skills/threads-scout/data/current_recommendations.md",
    "jonathan/skills/threads-scout/data/keywords.md",
    "jonathan/skills/threads-scout/data/recommended_history.md",
    "research/data/pipeline_events.jsonl",
    "research/data/runtime/event_chains.json",
    "research/data/runtime/pipelines/alpha-distil/2026-03-26T18-55-08+0800-alpha-distil-9028b4/artifacts/fetch/defillama_items.json",
    "research/data/runtime/pipelines/alpha-distil/2026-03-26T18-55-08+0800-alpha-distil-9028b4/artifacts/fetch/docs_items.json",
    "research/data/runtime/pipelines/alpha-distil/2026-03-26T18-55-08+0800-alpha-distil-9028b4/artifacts/fetch/governance_items.json",
    "research/data/runtime/pipelines/alpha-distil/2026-03-26T18-55-08+0800-alpha-distil-9028b4/artifacts/fetch/manifest.json",
    "research/data/runtime/pipelines/alpha-distil/2026-03-26T18-55-08+0800-alpha-distil-9028b4/artifacts/fetch/manifest.json.meta.json",
    "research/data/runtime/pipelines/alpha-distil/2026-03-26T18-55-08+0800-alpha-distil-9028b4/artifacts/fetch/x_items.json",
    "research/data/runtime/pipelines/alpha-distil/2026-03-26T18-55-08+0800-alpha-distil-9028b4/artifacts/ingest/fast_ingest.json",
    "research/data/runtime/pipelines/alpha-distil/2026-03-26T18-55-08+0800-alpha-distil-9028b4/artifacts/ingest/fast_ingest.json.meta.json",
    "research/data/runtime/pipelines/alpha-distil/2026-03-26T18-55-08+0800-alpha-distil-9028b4/artifacts/pool/upsert_result.json",
    "research/data/runtime/pipelines/alpha-distil/2026-03-26T18-55-08+0800-alpha-distil-9028b4/artifacts/pool/upsert_result.json.meta.json",
    "research/data/runtime/pipelines/alpha-distil/2026-03-26T18-55-08+0800-alpha-distil-9028b4/artifacts/route/cluster_route.json",
    "research/data/runtime/pipelines/alpha-distil/2026-03-26T18-55-08+0800-alpha-distil-9028b4/artifacts/route/cluster_route.json.meta.json",
    "research/data/runtime/pipelines/alpha-distil/2026-03-26T18-55-08+0800-alpha-distil-9028b4/artifacts/route/route_decisions.json",
    "research/data/runtime/pipelines/alpha-distil/2026-03-26T18-55-08+0800-alpha-distil-9028b4/artifacts/route/route_decisions.json.meta.json",
    "research/data/runtime/pipelines/alpha-distil/2026-03-26T18-55-08+0800-alpha-distil-9028b4/manifest.json"
  ],
  "reasons": [
    "touches risky subsystem: research/data/runtime/pipelines/alpha-distil/2026-03-26T18-55-08+0800-alpha-distil-9028b4/artifacts/route/route_decisions.json, research/data/runtime/pipelines/alpha-distil/2026-03-26T18-55-08+0800-alpha-distil-9028b4/artifacts/route/route_decisions.json.meta.json, research/data/runtime/pipelines/alpha-distil/2026-03-26T19-55-07+0800-alpha-distil-6dc229/artifacts/route/route_decisions.json, research/data/runtime/pipelines/alpha-distil/2026-03-26T19-55-07+0800-alpha-distil-6dc229/artifacts/route/route_decisions.json.meta.json",
    "large change set: 94 files"
  ]
}
