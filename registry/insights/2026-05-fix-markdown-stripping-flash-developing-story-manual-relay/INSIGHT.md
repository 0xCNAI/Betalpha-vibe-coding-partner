---
{
  "title": "fix: markdown stripping + flash developing story + manual relay",
  "type": "pitfall",
  "tags": [
    "token"
  ],
  "tech_stack": [
    "python"
  ],
  "summary": "Git history candidate from `clawd` commit `4dc2b1fa3ac3`: fix: markdown stripping + flash developing story + manual relay",
  "prevention_signal": "Before modifying `betalpha-social/learning/LESSONS.md` or adjacent subsystem, search this registry and inspect the original fixing commit.",
  "verify_trigger": "When the touched subsystem, framework version, or deployment environment changes.",
  "concrete_evidence": "{\n  \"commit\": \"4dc2b1fa3ac335f10257850f9efe20bc40d7a34b\",\n  \"files\": [\n    \"betalpha-social/learning/LESSONS.md\",\n    \"betalpha-social/learning/jc_activity_tracking.md\",\n    \"betalpha-social/memory/2026-03-22.md\",\n    \"\\\"betalpha-social/post_history/2026-03-21_threads_Aave_Morpho_\\\\346\\\\262\\\\273\\\\347\\\\220\\\\206\\\\345\\\\233\\\\260\\\\345\\\\242\\\\203.md\\\"\",\n    \"\\\"betalpha-social/threads/260322_\\\\346\\\\232\\\\264\\\\350\\\\267\\\\214\\\\350\\\\250\\\\212\\\\350\\\\231\\\\237\\\\345\\\\210\\\\206\\\\346\\\\255\\\\247_thread.md\\\"\",\n    \"jonathan/content/drafts/PUBLISH_GUIDE.md\",\n    \"jonathan/content/drafts/ai_chooses_bitcoin_2026-03-05.md\",\n    \"jonathan/content/drafts/bitcoin_73k_bull_trap_warning.md\",\n    \"jonathan/content/drafts/bitcoin_73k_bull_trap_warning_v2.md\",\n    \"jonathan/content/drafts/hype_ig_draft.md\",\n    \"jonathan/content/drafts/japan_crypto_tax_reform_2026.md\",\n    \"jonathan/content/drafts/korea_stock_crypto_rotation_2026-03-05.md\",\n    \"jonathan/content/drafts/korea_thread_final.md\",\n    \"jonathan/content/drafts/korea_visual_sources.md\",\n    \"jonathan/content/drafts/screenshot_instructions.md\",\n    \"jonathan/content/drafts/sec_token_taxonomy_march2026.md\",\n    \"jonathan/content/drafts/sec_token_taxonomy_march2026_v2.md\",\n    \"jonathan/data/daily_kol_digest.md\",\n    \"jonathan/skills/threads-scout/data/current_recommendations.md\",\n    \"jonathan/skills/threads-scout/data/keywords.md\"\n  ],\n  \"reasons\": [\n    \"commit message contains failure/fix signal\",\n    \"touches risky subsystem: betalpha-social/learning/LESSONS.md, betalpha-social/learning/jc_activity_tracking.md, betalpha-social/memory/2026-03-22.md, \\\"betalpha-social/post_history/2026-03-21_threads_Aave_Morpho_\\\\346\\\\262\\\\273\\\\347\\\\220\\\\206\\\\345\\\\233\\\\260\\\\345\\\\242\\\\203.md\\\"\",\n    \"large change set: 68 files\"\n  ]\n}",
  "transferable_pattern": "Before modifying `betalpha-social/learning/LESSONS.md` or adjacent subsystem, search this registry and inspect the original fixing commit.",
  "domain_metadata": {
    "tags": [
      "token"
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
    "sha": "4dc2b1fa3ac335f10257850f9efe20bc40d7a34b",
    "date": "2026-03-22T16:11:18+08:00",
    "files": [
      "betalpha-social/learning/LESSONS.md",
      "betalpha-social/learning/jc_activity_tracking.md",
      "betalpha-social/memory/2026-03-22.md",
      "\"betalpha-social/post_history/2026-03-21_threads_Aave_Morpho_\\346\\262\\273\\347\\220\\206\\345\\233\\260\\345\\242\\203.md\"",
      "\"betalpha-social/threads/260322_\\346\\232\\264\\350\\267\\214\\350\\250\\212\\350\\231\\237\\345\\210\\206\\346\\255\\247_thread.md\"",
      "jonathan/content/drafts/PUBLISH_GUIDE.md",
      "jonathan/content/drafts/ai_chooses_bitcoin_2026-03-05.md",
      "jonathan/content/drafts/bitcoin_73k_bull_trap_warning.md",
      "jonathan/content/drafts/bitcoin_73k_bull_trap_warning_v2.md",
      "jonathan/content/drafts/hype_ig_draft.md",
      "jonathan/content/drafts/japan_crypto_tax_reform_2026.md",
      "jonathan/content/drafts/korea_stock_crypto_rotation_2026-03-05.md",
      "jonathan/content/drafts/korea_thread_final.md",
      "jonathan/content/drafts/korea_visual_sources.md",
      "jonathan/content/drafts/screenshot_instructions.md",
      "jonathan/content/drafts/sec_token_taxonomy_march2026.md",
      "jonathan/content/drafts/sec_token_taxonomy_march2026_v2.md",
      "jonathan/data/daily_kol_digest.md",
      "jonathan/skills/threads-scout/data/current_recommendations.md",
      "jonathan/skills/threads-scout/data/keywords.md",
      "jonathan/skills/threads-scout/data/recommended_history.md",
      "publish/AGENTS.md",
      "publish/drafts/resolv-usr-exploit-user-guide.md",
      "publish/handoffs/resolv-usr-exploit-user-guide.md",
      "research/AGENTS.md",
      "research/TOOLS.md",
      "research/data/pipeline_events.jsonl",
      "research/data/training/flash-news.jsonl",
      "research/data/training/inputs/flash_2026-03-22_09.json",
      "research/data/training/inputs/flash_2026-03-22_10.json"
    ]
  }
}
---

## Symptom

Commit message suggests a potential lesson: fix: markdown stripping + flash developing story + manual relay

## Root Cause

Review the commit diff / PR discussion before promotion.

## Wrong Paths

Unknown from git log alone.

## Fix

Inspect with: git show --stat --patch 4dc2b1fa3ac335f10257850f9efe20bc40d7a34b

## Evidence

{
  "commit": "4dc2b1fa3ac335f10257850f9efe20bc40d7a34b",
  "files": [
    "betalpha-social/learning/LESSONS.md",
    "betalpha-social/learning/jc_activity_tracking.md",
    "betalpha-social/memory/2026-03-22.md",
    "\"betalpha-social/post_history/2026-03-21_threads_Aave_Morpho_\\346\\262\\273\\347\\220\\206\\345\\233\\260\\345\\242\\203.md\"",
    "\"betalpha-social/threads/260322_\\346\\232\\264\\350\\267\\214\\350\\250\\212\\350\\231\\237\\345\\210\\206\\346\\255\\247_thread.md\"",
    "jonathan/content/drafts/PUBLISH_GUIDE.md",
    "jonathan/content/drafts/ai_chooses_bitcoin_2026-03-05.md",
    "jonathan/content/drafts/bitcoin_73k_bull_trap_warning.md",
    "jonathan/content/drafts/bitcoin_73k_bull_trap_warning_v2.md",
    "jonathan/content/drafts/hype_ig_draft.md",
    "jonathan/content/drafts/japan_crypto_tax_reform_2026.md",
    "jonathan/content/drafts/korea_stock_crypto_rotation_2026-03-05.md",
    "jonathan/content/drafts/korea_thread_final.md",
    "jonathan/content/drafts/korea_visual_sources.md",
    "jonathan/content/drafts/screenshot_instructions.md",
    "jonathan/content/drafts/sec_token_taxonomy_march2026.md",
    "jonathan/content/drafts/sec_token_taxonomy_march2026_v2.md",
    "jonathan/data/daily_kol_digest.md",
    "jonathan/skills/threads-scout/data/current_recommendations.md",
    "jonathan/skills/threads-scout/data/keywords.md"
  ],
  "reasons": [
    "commit message contains failure/fix signal",
    "touches risky subsystem: betalpha-social/learning/LESSONS.md, betalpha-social/learning/jc_activity_tracking.md, betalpha-social/memory/2026-03-22.md, \"betalpha-social/post_history/2026-03-21_threads_Aave_Morpho_\\346\\262\\273\\347\\220\\206\\345\\233\\260\\345\\242\\203.md\"",
    "large change set: 68 files"
  ]
}
