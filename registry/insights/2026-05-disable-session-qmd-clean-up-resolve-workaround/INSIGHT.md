---
{
  "title": "disable session QMD: clean up resolve workaround",
  "type": "pitfall",
  "tags": [
    "test"
  ],
  "tech_stack": [
    "python"
  ],
  "summary": "Git history candidate from `clawd` commit `8d6aa62ad17b`: disable session QMD: clean up resolve workaround",
  "prevention_signal": "Before modifying `betalpha-social/AGENTS.md` or adjacent subsystem, search this registry and inspect the original fixing commit.",
  "verify_trigger": "When the touched subsystem, framework version, or deployment environment changes.",
  "concrete_evidence": "{\n  \"commit\": \"8d6aa62ad17bd15151142dfec65cd573dbc9802f\",\n  \"files\": [\n    \"betalpha-social/AGENTS.md\",\n    \"jonathan/AGENTS.md\",\n    \"publish/AGENTS.md\",\n    \"research-agent/AGENTS.md\",\n    \"research/AGENTS.md\",\n    \"research/data/runtime/pipelines/portfolio-alpha/2026-03-25T21-57-04+0800-portfolio-alpha-833a5a/artifacts/publish/feedback_receipt.json\",\n    \"research/data/runtime/pipelines/portfolio-alpha/2026-03-25T21-57-04+0800-portfolio-alpha-833a5a/artifacts/publish/feedback_receipt.json.meta.json\",\n    \"research/data/runtime/pipelines/portfolio-alpha/2026-03-25T21-57-04+0800-portfolio-alpha-833a5a/artifacts/review/candidate_pool_snapshot.json\",\n    \"research/data/runtime/pipelines/portfolio-alpha/2026-03-25T21-57-04+0800-portfolio-alpha-833a5a/artifacts/review/candidate_pool_snapshot.json.meta.json\",\n    \"research/data/runtime/pipelines/portfolio-alpha/2026-03-25T21-57-04+0800-portfolio-alpha-833a5a/artifacts/review/latest_feedback_log_entry.json\",\n    \"research/data/runtime/pipelines/portfolio-alpha/2026-03-25T21-57-04+0800-portfolio-alpha-833a5a/artifacts/review/latest_feedback_log_entry.json.meta.json\",\n    \"research/data/runtime/pipelines/portfolio-alpha/2026-03-25T21-57-04+0800-portfolio-alpha-833a5a/artifacts/review/review_decision.json\",\n    \"research/data/runtime/pipelines/portfolio-alpha/2026-03-25T21-57-04+0800-portfolio-alpha-833a5a/artifacts/review/review_decision.json.meta.json\",\n    \"research/data/runtime/pipelines/portfolio-alpha/2026-03-25T21-57-04+0800-portfolio-alpha-833a5a/receipts/publish_or_feedback.json\",\n    \"research/data/runtime/pipelines/portfolio-alpha/2026-03-25T21-57-04+0800-portfolio-alpha-833a5a/receipts/review_decide.json\",\n    \"research/data/runtime/pipelines/portfolio-alpha/2026-03-25T21-57-04+0800-portfolio-alpha-833a5a/status.json\",\n    \"research/data/runtime/pipelines/portfolio-alpha/2026-03-25T21-57-04+0800-portfolio-alpha-833a5a/summary.json\",\n    \"research/data/runtime/qmd_maintenance/history.jsonl\",\n    \"research/data/runtime/qmd_maintenance/lock\",\n    \"research/data/runtime/qmd_maintenance/state.json\"\n  ],\n  \"reasons\": [\n    \"commit message contains failure/fix signal\",\n    \"touches risky subsystem: betalpha-social/AGENTS.md, research/data/runtime/pipelines/portfolio-alpha/2026-03-25T21-57-04+0800-portfolio-alpha-833a5a/artifacts/publish/feedback_receipt.json, research/data/runtime/pipelines/portfolio-alpha/2026-03-25T21-57-04+0800-portfolio-alpha-833a5a/artifacts/publish/feedback_receipt.json.meta.json, research/data/runtime/pipelines/portfolio-alpha/2026-03-25T21-57-04+0800-portfolio-alpha-833a5a/artifacts/review/latest_feedback_log_entry.json\",\n    \"large change set: 23 files\"\n  ]\n}",
  "transferable_pattern": "Before modifying `betalpha-social/AGENTS.md` or adjacent subsystem, search this registry and inspect the original fixing commit.",
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
    "sha": "8d6aa62ad17bd15151142dfec65cd573dbc9802f",
    "date": "2026-03-25T22:39:49+08:00",
    "files": [
      "betalpha-social/AGENTS.md",
      "jonathan/AGENTS.md",
      "publish/AGENTS.md",
      "research-agent/AGENTS.md",
      "research/AGENTS.md",
      "research/data/runtime/pipelines/portfolio-alpha/2026-03-25T21-57-04+0800-portfolio-alpha-833a5a/artifacts/publish/feedback_receipt.json",
      "research/data/runtime/pipelines/portfolio-alpha/2026-03-25T21-57-04+0800-portfolio-alpha-833a5a/artifacts/publish/feedback_receipt.json.meta.json",
      "research/data/runtime/pipelines/portfolio-alpha/2026-03-25T21-57-04+0800-portfolio-alpha-833a5a/artifacts/review/candidate_pool_snapshot.json",
      "research/data/runtime/pipelines/portfolio-alpha/2026-03-25T21-57-04+0800-portfolio-alpha-833a5a/artifacts/review/candidate_pool_snapshot.json.meta.json",
      "research/data/runtime/pipelines/portfolio-alpha/2026-03-25T21-57-04+0800-portfolio-alpha-833a5a/artifacts/review/latest_feedback_log_entry.json",
      "research/data/runtime/pipelines/portfolio-alpha/2026-03-25T21-57-04+0800-portfolio-alpha-833a5a/artifacts/review/latest_feedback_log_entry.json.meta.json",
      "research/data/runtime/pipelines/portfolio-alpha/2026-03-25T21-57-04+0800-portfolio-alpha-833a5a/artifacts/review/review_decision.json",
      "research/data/runtime/pipelines/portfolio-alpha/2026-03-25T21-57-04+0800-portfolio-alpha-833a5a/artifacts/review/review_decision.json.meta.json",
      "research/data/runtime/pipelines/portfolio-alpha/2026-03-25T21-57-04+0800-portfolio-alpha-833a5a/receipts/publish_or_feedback.json",
      "research/data/runtime/pipelines/portfolio-alpha/2026-03-25T21-57-04+0800-portfolio-alpha-833a5a/receipts/review_decide.json",
      "research/data/runtime/pipelines/portfolio-alpha/2026-03-25T21-57-04+0800-portfolio-alpha-833a5a/status.json",
      "research/data/runtime/pipelines/portfolio-alpha/2026-03-25T21-57-04+0800-portfolio-alpha-833a5a/summary.json",
      "research/data/runtime/qmd_maintenance/history.jsonl",
      "research/data/runtime/qmd_maintenance/lock",
      "research/data/runtime/qmd_maintenance/state.json",
      "research/data/scorecards/portfolio-alpha.json",
      "research/memory/MEMORY.md",
      "research/scripts/qmd_maintainer.py"
    ]
  }
}
---

## Symptom

Commit message suggests a potential lesson: disable session QMD: clean up resolve workaround

## Root Cause

Review the commit diff / PR discussion before promotion.

## Wrong Paths

Unknown from git log alone.

## Fix

Inspect with: git show --stat --patch 8d6aa62ad17bd15151142dfec65cd573dbc9802f

## Evidence

{
  "commit": "8d6aa62ad17bd15151142dfec65cd573dbc9802f",
  "files": [
    "betalpha-social/AGENTS.md",
    "jonathan/AGENTS.md",
    "publish/AGENTS.md",
    "research-agent/AGENTS.md",
    "research/AGENTS.md",
    "research/data/runtime/pipelines/portfolio-alpha/2026-03-25T21-57-04+0800-portfolio-alpha-833a5a/artifacts/publish/feedback_receipt.json",
    "research/data/runtime/pipelines/portfolio-alpha/2026-03-25T21-57-04+0800-portfolio-alpha-833a5a/artifacts/publish/feedback_receipt.json.meta.json",
    "research/data/runtime/pipelines/portfolio-alpha/2026-03-25T21-57-04+0800-portfolio-alpha-833a5a/artifacts/review/candidate_pool_snapshot.json",
    "research/data/runtime/pipelines/portfolio-alpha/2026-03-25T21-57-04+0800-portfolio-alpha-833a5a/artifacts/review/candidate_pool_snapshot.json.meta.json",
    "research/data/runtime/pipelines/portfolio-alpha/2026-03-25T21-57-04+0800-portfolio-alpha-833a5a/artifacts/review/latest_feedback_log_entry.json",
    "research/data/runtime/pipelines/portfolio-alpha/2026-03-25T21-57-04+0800-portfolio-alpha-833a5a/artifacts/review/latest_feedback_log_entry.json.meta.json",
    "research/data/runtime/pipelines/portfolio-alpha/2026-03-25T21-57-04+0800-portfolio-alpha-833a5a/artifacts/review/review_decision.json",
    "research/data/runtime/pipelines/portfolio-alpha/2026-03-25T21-57-04+0800-portfolio-alpha-833a5a/artifacts/review/review_decision.json.meta.json",
    "research/data/runtime/pipelines/portfolio-alpha/2026-03-25T21-57-04+0800-portfolio-alpha-833a5a/receipts/publish_or_feedback.json",
    "research/data/runtime/pipelines/portfolio-alpha/2026-03-25T21-57-04+0800-portfolio-alpha-833a5a/receipts/review_decide.json",
    "research/data/runtime/pipelines/portfolio-alpha/2026-03-25T21-57-04+0800-portfolio-alpha-833a5a/status.json",
    "research/data/runtime/pipelines/portfolio-alpha/2026-03-25T21-57-04+0800-portfolio-alpha-833a5a/summary.json",
    "research/data/runtime/qmd_maintenance/history.jsonl",
    "research/data/runtime/qmd_maintenance/lock",
    "research/data/runtime/qmd_maintenance/state.json"
  ],
  "reasons": [
    "commit message contains failure/fix signal",
    "touches risky subsystem: betalpha-social/AGENTS.md, research/data/runtime/pipelines/portfolio-alpha/2026-03-25T21-57-04+0800-portfolio-alpha-833a5a/artifacts/publish/feedback_receipt.json, research/data/runtime/pipelines/portfolio-alpha/2026-03-25T21-57-04+0800-portfolio-alpha-833a5a/artifacts/publish/feedback_receipt.json.meta.json, research/data/runtime/pipelines/portfolio-alpha/2026-03-25T21-57-04+0800-portfolio-alpha-833a5a/artifacts/review/latest_feedback_log_entry.json",
    "large change set: 23 files"
  ]
}
