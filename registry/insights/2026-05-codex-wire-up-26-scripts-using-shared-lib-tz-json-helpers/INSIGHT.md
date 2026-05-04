---
{
  "title": "codex wire-up: 26 scripts using shared lib (TZ + JSON helpers)",
  "type": "spec_guardrail",
  "tags": [
    "test"
  ],
  "tech_stack": [
    "python"
  ],
  "summary": "Git history candidate from `clawd` commit `f01184013375`: codex wire-up: 26 scripts using shared lib (TZ + JSON helpers)",
  "prevention_signal": "Before modifying `research/scripts/daily_feedback.py` or adjacent subsystem, search this registry and inspect the original fixing commit.",
  "verify_trigger": "When the touched subsystem, framework version, or deployment environment changes.",
  "concrete_evidence": "{\n  \"commit\": \"f0118401337542278a59451558040e2ca6d44f55\",\n  \"files\": [\n    \"research/scripts/acp_watchdog.py\",\n    \"research/scripts/autoresearch_enrich_testset.py\",\n    \"research/scripts/autoresearch_logger.py\",\n    \"research/scripts/corrections_tracker.py\",\n    \"research/scripts/daily_feedback.py\",\n    \"research/scripts/deep_dive_review.py\",\n    \"research/scripts/deep_dive_trigger.py\",\n    \"research/scripts/feedback_distill.py\",\n    \"research/scripts/feedback_record.py\",\n    \"research/scripts/feedback_weekly_digest.py\",\n    \"research/scripts/flash_coverage_review.py\",\n    \"research/scripts/gateway_watchdog.py\",\n    \"research/scripts/good_examples.py\",\n    \"research/scripts/handoff.py\",\n    \"research/scripts/heartbeat_proposals.py\",\n    \"research/scripts/pipeline_health.py\",\n    \"research/scripts/pipeline_observe.py\",\n    \"research/scripts/podcast_digest.py\",\n    \"research/scripts/podcast_fetch.py\",\n    \"research/scripts/podcast_nightly.py\"\n  ],\n  \"reasons\": [\n    \"touches risky subsystem: research/scripts/daily_feedback.py, research/scripts/feedback_distill.py, research/scripts/feedback_record.py, research/scripts/feedback_weekly_digest.py\",\n    \"large change set: 26 files\"\n  ]\n}",
  "transferable_pattern": "Before modifying `research/scripts/daily_feedback.py` or adjacent subsystem, search this registry and inspect the original fixing commit.",
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
    "sha": "f0118401337542278a59451558040e2ca6d44f55",
    "date": "2026-03-20T18:23:11+08:00",
    "files": [
      "research/scripts/acp_watchdog.py",
      "research/scripts/autoresearch_enrich_testset.py",
      "research/scripts/autoresearch_logger.py",
      "research/scripts/corrections_tracker.py",
      "research/scripts/daily_feedback.py",
      "research/scripts/deep_dive_review.py",
      "research/scripts/deep_dive_trigger.py",
      "research/scripts/feedback_distill.py",
      "research/scripts/feedback_record.py",
      "research/scripts/feedback_weekly_digest.py",
      "research/scripts/flash_coverage_review.py",
      "research/scripts/gateway_watchdog.py",
      "research/scripts/good_examples.py",
      "research/scripts/handoff.py",
      "research/scripts/heartbeat_proposals.py",
      "research/scripts/pipeline_health.py",
      "research/scripts/pipeline_observe.py",
      "research/scripts/podcast_digest.py",
      "research/scripts/podcast_fetch.py",
      "research/scripts/podcast_nightly.py",
      "research/scripts/portfolio_log_sync.py",
      "research/scripts/reviewer_to_strategist.py",
      "research/scripts/thread_ideas_pool.py",
      "research/scripts/tweet_feedback_loop.py",
      "research/scripts/weekly_scorecard.py",
      "research/scripts/weekly_thesis_gather.py"
    ]
  }
}
---

## Symptom

Commit message suggests a potential lesson: codex wire-up: 26 scripts using shared lib (TZ + JSON helpers)

## Root Cause

Review the commit diff / PR discussion before promotion.

## Wrong Paths

Unknown from git log alone.

## Fix

Inspect with: git show --stat --patch f0118401337542278a59451558040e2ca6d44f55

## Evidence

{
  "commit": "f0118401337542278a59451558040e2ca6d44f55",
  "files": [
    "research/scripts/acp_watchdog.py",
    "research/scripts/autoresearch_enrich_testset.py",
    "research/scripts/autoresearch_logger.py",
    "research/scripts/corrections_tracker.py",
    "research/scripts/daily_feedback.py",
    "research/scripts/deep_dive_review.py",
    "research/scripts/deep_dive_trigger.py",
    "research/scripts/feedback_distill.py",
    "research/scripts/feedback_record.py",
    "research/scripts/feedback_weekly_digest.py",
    "research/scripts/flash_coverage_review.py",
    "research/scripts/gateway_watchdog.py",
    "research/scripts/good_examples.py",
    "research/scripts/handoff.py",
    "research/scripts/heartbeat_proposals.py",
    "research/scripts/pipeline_health.py",
    "research/scripts/pipeline_observe.py",
    "research/scripts/podcast_digest.py",
    "research/scripts/podcast_fetch.py",
    "research/scripts/podcast_nightly.py"
  ],
  "reasons": [
    "touches risky subsystem: research/scripts/daily_feedback.py, research/scripts/feedback_distill.py, research/scripts/feedback_record.py, research/scripts/feedback_weekly_digest.py",
    "large change set: 26 files"
  ]
}
