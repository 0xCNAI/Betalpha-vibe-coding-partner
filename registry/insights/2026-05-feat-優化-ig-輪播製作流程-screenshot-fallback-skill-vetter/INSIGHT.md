---
{
  "title": "feat: 優化 IG 輪播製作流程 + screenshot fallback + skill vetter",
  "type": "spec_guardrail",
  "tags": [
    "cron",
    "test"
  ],
  "tech_stack": [
    "python"
  ],
  "summary": "Git history candidate from `clawd` commit `2aa28d494eee`: feat: 優化 IG 輪播製作流程 + screenshot fallback + skill vetter",
  "prevention_signal": "Before modifying `betalpha-social/learning/jc_activity_tracking.md` or adjacent subsystem, search this registry and inspect the original fixing commit.",
  "verify_trigger": "When the touched subsystem, framework version, or deployment environment changes.",
  "concrete_evidence": "{\n  \"commit\": \"2aa28d494eee2ff62c2355bd17fbda3dde5aaeeb\",\n  \"files\": [\n    \"betalpha-social/learning/jc_activity_tracking.md\",\n    \"betalpha-social/memory/2026-03-24.md\",\n    \"\\\"betalpha-social/post_history/2026-03-23_instagram_Resolv_USR\\\\351\\\\221\\\\204\\\\345\\\\271\\\\243\\\\346\\\\224\\\\273\\\\346\\\\223\\\\212_Fluid\\\\346\\\\223\\\\240\\\\345\\\\205\\\\214.md\\\"\",\n    \"\\\"betalpha-social/post_history/2026-03-23_threads_Resolv_USR_Morpho_curator\\\\351\\\\242\\\\250\\\\346\\\\216\\\\247.md\\\"\",\n    \"\\\"betalpha-social/threads/260324_Automation\\\\346\\\\234\\\\215\\\\345\\\\213\\\\231\\\\346\\\\226\\\\207\\\\344\\\\273\\\\266_thread.md\\\"\",\n    \"\\\"betalpha-social/threads/260324_PDF\\\\345\\\\267\\\\245\\\\345\\\\226\\\\256\\\\350\\\\247\\\\243\\\\346\\\\236\\\\220\\\\345\\\\231\\\\250_thread.md\\\"\",\n    \"jonathan/TOOLS.md\",\n    \"jonathan/data/daily_kol_digest.md\",\n    \"jonathan/memory/2026-03-24.md\",\n    \"jonathan/post_history/threads_20260324_150012_balancer_shutdown.md\",\n    \"jonathan/scripts/morning_briefing.py\",\n    \"jonathan/skills/.clawhub/lock.json\",\n    \"jonathan/skills/betalpha-content/SKILL.md\",\n    \"jonathan/skills/betalpha-images/SKILL.md\",\n    \"jonathan/skills/betalpha-screenshot/SKILL.md\",\n    \"jonathan/skills/betalpha-screenshot/learning_log.md\",\n    \"jonathan/skills/image-highlight-cropper/SKILL.md\",\n    \"jonathan/skills/instagram-image-maker/SKILL.md\",\n    \"jonathan/skills/instagram-image-maker/learning_log.md\",\n    \"jonathan/skills/instagram-writer/SKILL.md\"\n  ],\n  \"reasons\": [\n    \"touches risky subsystem: betalpha-social/learning/jc_activity_tracking.md, betalpha-social/memory/2026-03-24.md, \\\"betalpha-social/post_history/2026-03-23_instagram_Resolv_USR\\\\351\\\\221\\\\204\\\\345\\\\271\\\\243\\\\346\\\\224\\\\273\\\\346\\\\223\\\\212_Fluid\\\\346\\\\223\\\\240\\\\345\\\\205\\\\214.md\\\", \\\"betalpha-social/post_history/2026-03-23_threads_Resolv_USR_Morpho_curator\\\\351\\\\242\\\\250\\\\346\\\\216\\\\247.md\\\"\",\n    \"large change set: 106 files\"\n  ]\n}",
  "transferable_pattern": "Before modifying `betalpha-social/learning/jc_activity_tracking.md` or adjacent subsystem, search this registry and inspect the original fixing commit.",
  "domain_metadata": {
    "tags": [
      "cron",
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
    "sha": "2aa28d494eee2ff62c2355bd17fbda3dde5aaeeb",
    "date": "2026-03-24T16:21:43+08:00",
    "files": [
      "betalpha-social/learning/jc_activity_tracking.md",
      "betalpha-social/memory/2026-03-24.md",
      "\"betalpha-social/post_history/2026-03-23_instagram_Resolv_USR\\351\\221\\204\\345\\271\\243\\346\\224\\273\\346\\223\\212_Fluid\\346\\223\\240\\345\\205\\214.md\"",
      "\"betalpha-social/post_history/2026-03-23_threads_Resolv_USR_Morpho_curator\\351\\242\\250\\346\\216\\247.md\"",
      "\"betalpha-social/threads/260324_Automation\\346\\234\\215\\345\\213\\231\\346\\226\\207\\344\\273\\266_thread.md\"",
      "\"betalpha-social/threads/260324_PDF\\345\\267\\245\\345\\226\\256\\350\\247\\243\\346\\236\\220\\345\\231\\250_thread.md\"",
      "jonathan/TOOLS.md",
      "jonathan/data/daily_kol_digest.md",
      "jonathan/memory/2026-03-24.md",
      "jonathan/post_history/threads_20260324_150012_balancer_shutdown.md",
      "jonathan/scripts/morning_briefing.py",
      "jonathan/skills/.clawhub/lock.json",
      "jonathan/skills/betalpha-content/SKILL.md",
      "jonathan/skills/betalpha-images/SKILL.md",
      "jonathan/skills/betalpha-screenshot/SKILL.md",
      "jonathan/skills/betalpha-screenshot/learning_log.md",
      "jonathan/skills/image-highlight-cropper/SKILL.md",
      "jonathan/skills/instagram-image-maker/SKILL.md",
      "jonathan/skills/instagram-image-maker/learning_log.md",
      "jonathan/skills/instagram-writer/SKILL.md",
      "jonathan/skills/instagram-writer/references/instagram_style_guide.md",
      "jonathan/skills/skills/playwright/.clawhub/origin.json",
      "jonathan/skills/skills/playwright/SKILL.md",
      "jonathan/skills/skills/playwright/_meta.json",
      "jonathan/skills/skills/playwright/ci-cd.md",
      "jonathan/skills/skills/playwright/debugging.md",
      "jonathan/skills/skills/playwright/scraping.md",
      "jonathan/skills/skills/playwright/selectors.md",
      "jonathan/skills/skills/playwright/testing.md",
      "jonathan/skills/skills/screenshot/.clawhub/origin.json"
    ]
  }
}
---

## Symptom

Commit message suggests a potential lesson: feat: 優化 IG 輪播製作流程 + screenshot fallback + skill vetter

## Root Cause

Review the commit diff / PR discussion before promotion.

## Wrong Paths

Unknown from git log alone.

## Fix

Inspect with: git show --stat --patch 2aa28d494eee2ff62c2355bd17fbda3dde5aaeeb

## Evidence

{
  "commit": "2aa28d494eee2ff62c2355bd17fbda3dde5aaeeb",
  "files": [
    "betalpha-social/learning/jc_activity_tracking.md",
    "betalpha-social/memory/2026-03-24.md",
    "\"betalpha-social/post_history/2026-03-23_instagram_Resolv_USR\\351\\221\\204\\345\\271\\243\\346\\224\\273\\346\\223\\212_Fluid\\346\\223\\240\\345\\205\\214.md\"",
    "\"betalpha-social/post_history/2026-03-23_threads_Resolv_USR_Morpho_curator\\351\\242\\250\\346\\216\\247.md\"",
    "\"betalpha-social/threads/260324_Automation\\346\\234\\215\\345\\213\\231\\346\\226\\207\\344\\273\\266_thread.md\"",
    "\"betalpha-social/threads/260324_PDF\\345\\267\\245\\345\\226\\256\\350\\247\\243\\346\\236\\220\\345\\231\\250_thread.md\"",
    "jonathan/TOOLS.md",
    "jonathan/data/daily_kol_digest.md",
    "jonathan/memory/2026-03-24.md",
    "jonathan/post_history/threads_20260324_150012_balancer_shutdown.md",
    "jonathan/scripts/morning_briefing.py",
    "jonathan/skills/.clawhub/lock.json",
    "jonathan/skills/betalpha-content/SKILL.md",
    "jonathan/skills/betalpha-images/SKILL.md",
    "jonathan/skills/betalpha-screenshot/SKILL.md",
    "jonathan/skills/betalpha-screenshot/learning_log.md",
    "jonathan/skills/image-highlight-cropper/SKILL.md",
    "jonathan/skills/instagram-image-maker/SKILL.md",
    "jonathan/skills/instagram-image-maker/learning_log.md",
    "jonathan/skills/instagram-writer/SKILL.md"
  ],
  "reasons": [
    "touches risky subsystem: betalpha-social/learning/jc_activity_tracking.md, betalpha-social/memory/2026-03-24.md, \"betalpha-social/post_history/2026-03-23_instagram_Resolv_USR\\351\\221\\204\\345\\271\\243\\346\\224\\273\\346\\223\\212_Fluid\\346\\223\\240\\345\\205\\214.md\", \"betalpha-social/post_history/2026-03-23_threads_Resolv_USR_Morpho_curator\\351\\242\\250\\346\\216\\247.md\"",
    "large change set: 106 files"
  ]
}
