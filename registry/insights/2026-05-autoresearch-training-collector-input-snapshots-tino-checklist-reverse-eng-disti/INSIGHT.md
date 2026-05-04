---
{
  "title": "autoresearch training: collector + input snapshots + tino checklist + reverse-eng distill ",
  "type": "pitfall",
  "tags": [
    "git-history"
  ],
  "tech_stack": [
    "python"
  ],
  "summary": "Git history candidate from `clawd` commit `8e52b0f5c512`: autoresearch training: collector + input snapshots + tino checklist + reverse-eng distill loop + dedup all pipelines + podcast RSS fix + Writer/Scout rules distill",
  "prevention_signal": "Before modifying `betalpha-social/Automation_case` or adjacent subsystem, search this registry and inspect the original fixing commit.",
  "verify_trigger": "When the touched subsystem, framework version, or deployment environment changes.",
  "concrete_evidence": "{\n  \"commit\": \"8e52b0f5c512e026f766415b306711c9ec93bc70\",\n  \"files\": [\n    \"betalpha-social/Automation_case\",\n    \"betalpha-social/memory/2026-03-20.md\",\n    \"\\\"betalpha-social/threads/260320_AI\\\\350\\\\243\\\\201\\\\345\\\\223\\\\241\\\\346\\\\275\\\\256_thread.md\\\"\",\n    \"jonathan/memory/2026-03-20.md\",\n    \"jonathan/skills/threads-scout/data/current_recommendations.md\",\n    \"jonathan/skills/threads-scout/data/keywords.md\",\n    \"jonathan/skills/threads-scout/data/recommended_history.md\",\n    \"publish/AGENTS.md\",\n    \"research-agent/reviewer-learnings.md\",\n    \"research/MagicMock/mock/4468398016\",\n    \"research/data/corrections_tracker_state.json\",\n    \"research/data/pattern_placement.jsonl\",\n    \"research/data/pattern_tracker.json\",\n    \"research/data/pending_rule_proposals.jsonl\",\n    \"research/data/pipeline_events.jsonl\",\n    \"research/data/reverse_eng_distill_state.json\",\n    \"research/data/rule_change_log.jsonl\",\n    \"research/data/rule_verdicts.jsonl\",\n    \"research/feedback/autoresearch_log/flash-writer_2026-03-20_123.json\",\n    \"research/feedback/autoresearch_log/flash-writer_2026-03-20_2514.json\"\n  ],\n  \"reasons\": [\n    \"commit message contains failure/fix signal\",\n    \"touches risky subsystem: betalpha-social/Automation_case, betalpha-social/memory/2026-03-20.md, \\\"betalpha-social/threads/260320_AI\\\\350\\\\243\\\\201\\\\345\\\\223\\\\241\\\\346\\\\275\\\\256_thread.md\\\", research/feedback/autoresearch_log/flash-writer_2026-03-20_123.json\",\n    \"large change set: 39 files\"\n  ]\n}",
  "transferable_pattern": "Before modifying `betalpha-social/Automation_case` or adjacent subsystem, search this registry and inspect the original fixing commit.",
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
    "sha": "8e52b0f5c512e026f766415b306711c9ec93bc70",
    "date": "2026-03-20T22:03:18+08:00",
    "files": [
      "betalpha-social/Automation_case",
      "betalpha-social/memory/2026-03-20.md",
      "\"betalpha-social/threads/260320_AI\\350\\243\\201\\345\\223\\241\\346\\275\\256_thread.md\"",
      "jonathan/memory/2026-03-20.md",
      "jonathan/skills/threads-scout/data/current_recommendations.md",
      "jonathan/skills/threads-scout/data/keywords.md",
      "jonathan/skills/threads-scout/data/recommended_history.md",
      "publish/AGENTS.md",
      "research-agent/reviewer-learnings.md",
      "research/MagicMock/mock/4468398016",
      "research/data/corrections_tracker_state.json",
      "research/data/pattern_placement.jsonl",
      "research/data/pattern_tracker.json",
      "research/data/pending_rule_proposals.jsonl",
      "research/data/pipeline_events.jsonl",
      "research/data/reverse_eng_distill_state.json",
      "research/data/rule_change_log.jsonl",
      "research/data/rule_verdicts.jsonl",
      "research/feedback/autoresearch_log/flash-writer_2026-03-20_123.json",
      "research/feedback/autoresearch_log/flash-writer_2026-03-20_2514.json",
      "research/feedback/autoresearch_log/flash-writer_2026-03-20_2515.json",
      "research/feedback/autoresearch_log/flash-writer_2026-03-20_2516.json",
      "research/memory/corrections.md",
      "research/scripts/feedback_inject.py",
      "research/scripts/heartbeat_proposals.py",
      "research/scripts/reverse_eng_distill.py",
      "research/scripts/training_collector.py",
      "research/skills/flash-news/flash_auto_publish.py",
      "research/skills/flash-news/flash_pipeline.py",
      "research/skills/flash-news/publish_log.json"
    ]
  }
}
---

## Symptom

Commit message suggests a potential lesson: autoresearch training: collector + input snapshots + tino checklist + reverse-eng distill loop + dedup all pipelines + podcast RSS fix + Writer/Scout rules distill

## Root Cause

Review the commit diff / PR discussion before promotion.

## Wrong Paths

Unknown from git log alone.

## Fix

Inspect with: git show --stat --patch 8e52b0f5c512e026f766415b306711c9ec93bc70

## Evidence

{
  "commit": "8e52b0f5c512e026f766415b306711c9ec93bc70",
  "files": [
    "betalpha-social/Automation_case",
    "betalpha-social/memory/2026-03-20.md",
    "\"betalpha-social/threads/260320_AI\\350\\243\\201\\345\\223\\241\\346\\275\\256_thread.md\"",
    "jonathan/memory/2026-03-20.md",
    "jonathan/skills/threads-scout/data/current_recommendations.md",
    "jonathan/skills/threads-scout/data/keywords.md",
    "jonathan/skills/threads-scout/data/recommended_history.md",
    "publish/AGENTS.md",
    "research-agent/reviewer-learnings.md",
    "research/MagicMock/mock/4468398016",
    "research/data/corrections_tracker_state.json",
    "research/data/pattern_placement.jsonl",
    "research/data/pattern_tracker.json",
    "research/data/pending_rule_proposals.jsonl",
    "research/data/pipeline_events.jsonl",
    "research/data/reverse_eng_distill_state.json",
    "research/data/rule_change_log.jsonl",
    "research/data/rule_verdicts.jsonl",
    "research/feedback/autoresearch_log/flash-writer_2026-03-20_123.json",
    "research/feedback/autoresearch_log/flash-writer_2026-03-20_2514.json"
  ],
  "reasons": [
    "commit message contains failure/fix signal",
    "touches risky subsystem: betalpha-social/Automation_case, betalpha-social/memory/2026-03-20.md, \"betalpha-social/threads/260320_AI\\350\\243\\201\\345\\223\\241\\346\\275\\256_thread.md\", research/feedback/autoresearch_log/flash-writer_2026-03-20_123.json",
    "large change set: 39 files"
  ]
}
