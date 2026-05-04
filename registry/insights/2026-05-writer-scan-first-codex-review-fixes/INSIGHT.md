---
{
  "title": "writer SCAN-first: codex review fixes",
  "type": "spec_guardrail",
  "tags": [
    "git-history"
  ],
  "tech_stack": [
    "python"
  ],
  "summary": "Git history candidate from `clawd` commit `fa5f96a61cee`: writer SCAN-first: codex review fixes",
  "prevention_signal": "Before modifying `research/config/alpha_distil_sources.json` or adjacent subsystem, search this registry and inspect the original fixing commit.",
  "verify_trigger": "When the touched subsystem, framework version, or deployment environment changes.",
  "concrete_evidence": "{\n  \"commit\": \"fa5f96a61ceee5f137941018043581a7184760b6\",\n  \"files\": [\n    \"research/config/alpha_distil_sources.json\",\n    \"research/data/pipeline_events.jsonl\",\n    \"research/data/runtime/event_chains.json\",\n    \"research/data/runtime/pipelines/flash-news/2026-03-26T20-12-07+0800-flash-news-db4f8a/artifacts/prescan/prescan_context.json\",\n    \"research/data/runtime/pipelines/flash-news/2026-03-26T20-12-07+0800-flash-news-db4f8a/artifacts/prescan/prescan_context.json.meta.json\",\n    \"research/data/runtime/pipelines/flash-news/2026-03-26T20-12-07+0800-flash-news-db4f8a/artifacts/prescan/raw_candidates.json\",\n    \"research/data/runtime/pipelines/flash-news/2026-03-26T20-12-07+0800-flash-news-db4f8a/artifacts/prescan/raw_candidates.json.meta.json\",\n    \"research/data/runtime/pipelines/flash-news/2026-03-26T20-12-07+0800-flash-news-db4f8a/artifacts/scout/event_candidates.json\",\n    \"research/data/runtime/pipelines/flash-news/2026-03-26T20-12-07+0800-flash-news-db4f8a/artifacts/scout/event_candidates.json.meta.json\",\n    \"research/data/runtime/pipelines/flash-news/2026-03-26T20-12-07+0800-flash-news-db4f8a/artifacts/scout/scout_output.json\",\n    \"research/data/runtime/pipelines/flash-news/2026-03-26T20-12-07+0800-flash-news-db4f8a/artifacts/scout/scout_output.json.meta.json\",\n    \"research/data/runtime/pipelines/flash-news/2026-03-26T20-12-07+0800-flash-news-db4f8a/artifacts/writer/drafts.json\",\n    \"research/data/runtime/pipelines/flash-news/2026-03-26T20-12-07+0800-flash-news-db4f8a/artifacts/writer/drafts.json.meta.json\",\n    \"research/data/runtime/pipelines/flash-news/2026-03-26T20-12-07+0800-flash-news-db4f8a/artifacts/writer/writer_output.json\",\n    \"research/data/runtime/pipelines/flash-news/2026-03-26T20-12-07+0800-flash-news-db4f8a/artifacts/writer/writer_output.json.meta.json\",\n    \"research/data/runtime/pipelines/flash-news/2026-03-26T20-12-07+0800-flash-news-db4f8a/manifest.json\",\n    \"research/data/runtime/pipelines/flash-news/2026-03-26T20-12-07+0800-flash-news-db4f8a/receipts/prescan_ingest.json\",\n    \"research/data/runtime/pipelines/flash-news/2026-03-26T20-12-07+0800-flash-news-db4f8a/receipts/scout_select.json\",\n    \"research/data/runtime/pipelines/flash-news/2026-03-26T20-12-07+0800-flash-news-db4f8a/receipts/writer_draft.json\",\n    \"research/data/runtime/pipelines/flash-news/2026-03-26T20-12-07+0800-flash-news-db4f8a/status.json\"\n  ],\n  \"reasons\": [\n    \"touches risky subsystem: research/config/alpha_distil_sources.json, research/data/runtime/pipelines/flash-news/2026-03-26T20-12-07+0800-flash-news-db4f8a/artifacts/prescan/prescan_context.json, research/data/runtime/pipelines/flash-news/2026-03-26T20-12-07+0800-flash-news-db4f8a/artifacts/prescan/prescan_context.json.meta.json, research/data/runtime/pipelines/flash-news/2026-03-26T20-12-07+0800-flash-news-db4f8a/artifacts/prescan/raw_candidates.json\",\n    \"large change set: 32 files\"\n  ]\n}",
  "transferable_pattern": "Before modifying `research/config/alpha_distil_sources.json` or adjacent subsystem, search this registry and inspect the original fixing commit.",
  "domain_metadata": {
    "tags": [
      "git-history"
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
    "sha": "fa5f96a61ceee5f137941018043581a7184760b6",
    "date": "2026-03-26T20:30:19+08:00",
    "files": [
      "research/config/alpha_distil_sources.json",
      "research/data/pipeline_events.jsonl",
      "research/data/runtime/event_chains.json",
      "research/data/runtime/pipelines/flash-news/2026-03-26T20-12-07+0800-flash-news-db4f8a/artifacts/prescan/prescan_context.json",
      "research/data/runtime/pipelines/flash-news/2026-03-26T20-12-07+0800-flash-news-db4f8a/artifacts/prescan/prescan_context.json.meta.json",
      "research/data/runtime/pipelines/flash-news/2026-03-26T20-12-07+0800-flash-news-db4f8a/artifacts/prescan/raw_candidates.json",
      "research/data/runtime/pipelines/flash-news/2026-03-26T20-12-07+0800-flash-news-db4f8a/artifacts/prescan/raw_candidates.json.meta.json",
      "research/data/runtime/pipelines/flash-news/2026-03-26T20-12-07+0800-flash-news-db4f8a/artifacts/scout/event_candidates.json",
      "research/data/runtime/pipelines/flash-news/2026-03-26T20-12-07+0800-flash-news-db4f8a/artifacts/scout/event_candidates.json.meta.json",
      "research/data/runtime/pipelines/flash-news/2026-03-26T20-12-07+0800-flash-news-db4f8a/artifacts/scout/scout_output.json",
      "research/data/runtime/pipelines/flash-news/2026-03-26T20-12-07+0800-flash-news-db4f8a/artifacts/scout/scout_output.json.meta.json",
      "research/data/runtime/pipelines/flash-news/2026-03-26T20-12-07+0800-flash-news-db4f8a/artifacts/writer/drafts.json",
      "research/data/runtime/pipelines/flash-news/2026-03-26T20-12-07+0800-flash-news-db4f8a/artifacts/writer/drafts.json.meta.json",
      "research/data/runtime/pipelines/flash-news/2026-03-26T20-12-07+0800-flash-news-db4f8a/artifacts/writer/writer_output.json",
      "research/data/runtime/pipelines/flash-news/2026-03-26T20-12-07+0800-flash-news-db4f8a/artifacts/writer/writer_output.json.meta.json",
      "research/data/runtime/pipelines/flash-news/2026-03-26T20-12-07+0800-flash-news-db4f8a/manifest.json",
      "research/data/runtime/pipelines/flash-news/2026-03-26T20-12-07+0800-flash-news-db4f8a/receipts/prescan_ingest.json",
      "research/data/runtime/pipelines/flash-news/2026-03-26T20-12-07+0800-flash-news-db4f8a/receipts/scout_select.json",
      "research/data/runtime/pipelines/flash-news/2026-03-26T20-12-07+0800-flash-news-db4f8a/receipts/writer_draft.json",
      "research/data/runtime/pipelines/flash-news/2026-03-26T20-12-07+0800-flash-news-db4f8a/status.json",
      "research/data/runtime/pipelines/flash-news/current_run.json",
      "research/data/runtime/qmd_maintenance/history.jsonl",
      "research/data/runtime/qmd_maintenance/lock",
      "research/data/runtime/qmd_maintenance/state.json",
      "research/data/training/flash-news.jsonl",
      "research/openspec/changes/writer-scan-first/REVIEW.md",
      "research/openspec/changes/writer-scan-first/REVIEW_DEBUG_REPORT.md",
      "research/scripts/alpha_distil_fast_fetch.py",
      "research/scripts/alpha_distil_source_registry.py",
      "research/scripts/pipeline_framework/betalpha_news_native.py"
    ]
  }
}
---

## Symptom

Commit message suggests a potential lesson: writer SCAN-first: codex review fixes

## Root Cause

Review the commit diff / PR discussion before promotion.

## Wrong Paths

Unknown from git log alone.

## Fix

Inspect with: git show --stat --patch fa5f96a61ceee5f137941018043581a7184760b6

## Evidence

{
  "commit": "fa5f96a61ceee5f137941018043581a7184760b6",
  "files": [
    "research/config/alpha_distil_sources.json",
    "research/data/pipeline_events.jsonl",
    "research/data/runtime/event_chains.json",
    "research/data/runtime/pipelines/flash-news/2026-03-26T20-12-07+0800-flash-news-db4f8a/artifacts/prescan/prescan_context.json",
    "research/data/runtime/pipelines/flash-news/2026-03-26T20-12-07+0800-flash-news-db4f8a/artifacts/prescan/prescan_context.json.meta.json",
    "research/data/runtime/pipelines/flash-news/2026-03-26T20-12-07+0800-flash-news-db4f8a/artifacts/prescan/raw_candidates.json",
    "research/data/runtime/pipelines/flash-news/2026-03-26T20-12-07+0800-flash-news-db4f8a/artifacts/prescan/raw_candidates.json.meta.json",
    "research/data/runtime/pipelines/flash-news/2026-03-26T20-12-07+0800-flash-news-db4f8a/artifacts/scout/event_candidates.json",
    "research/data/runtime/pipelines/flash-news/2026-03-26T20-12-07+0800-flash-news-db4f8a/artifacts/scout/event_candidates.json.meta.json",
    "research/data/runtime/pipelines/flash-news/2026-03-26T20-12-07+0800-flash-news-db4f8a/artifacts/scout/scout_output.json",
    "research/data/runtime/pipelines/flash-news/2026-03-26T20-12-07+0800-flash-news-db4f8a/artifacts/scout/scout_output.json.meta.json",
    "research/data/runtime/pipelines/flash-news/2026-03-26T20-12-07+0800-flash-news-db4f8a/artifacts/writer/drafts.json",
    "research/data/runtime/pipelines/flash-news/2026-03-26T20-12-07+0800-flash-news-db4f8a/artifacts/writer/drafts.json.meta.json",
    "research/data/runtime/pipelines/flash-news/2026-03-26T20-12-07+0800-flash-news-db4f8a/artifacts/writer/writer_output.json",
    "research/data/runtime/pipelines/flash-news/2026-03-26T20-12-07+0800-flash-news-db4f8a/artifacts/writer/writer_output.json.meta.json",
    "research/data/runtime/pipelines/flash-news/2026-03-26T20-12-07+0800-flash-news-db4f8a/manifest.json",
    "research/data/runtime/pipelines/flash-news/2026-03-26T20-12-07+0800-flash-news-db4f8a/receipts/prescan_ingest.json",
    "research/data/runtime/pipelines/flash-news/2026-03-26T20-12-07+0800-flash-news-db4f8a/receipts/scout_select.json",
    "research/data/runtime/pipelines/flash-news/2026-03-26T20-12-07+0800-flash-news-db4f8a/receipts/writer_draft.json",
    "research/data/runtime/pipelines/flash-news/2026-03-26T20-12-07+0800-flash-news-db4f8a/status.json"
  ],
  "reasons": [
    "touches risky subsystem: research/config/alpha_distil_sources.json, research/data/runtime/pipelines/flash-news/2026-03-26T20-12-07+0800-flash-news-db4f8a/artifacts/prescan/prescan_context.json, research/data/runtime/pipelines/flash-news/2026-03-26T20-12-07+0800-flash-news-db4f8a/artifacts/prescan/prescan_context.json.meta.json, research/data/runtime/pipelines/flash-news/2026-03-26T20-12-07+0800-flash-news-db4f8a/artifacts/prescan/raw_candidates.json",
    "large change set: 32 files"
  ]
}
