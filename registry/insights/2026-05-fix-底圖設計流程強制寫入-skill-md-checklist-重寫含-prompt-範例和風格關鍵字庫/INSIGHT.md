---
{
  "title": "fix: 底圖設計流程強制寫入 SKILL.md + checklist 重寫含 prompt 範例和風格關鍵字庫",
  "type": "pitfall",
  "tags": [
    "test"
  ],
  "tech_stack": [
    "python"
  ],
  "summary": "Git history candidate from `clawd` commit `9cac5685f5d8`: fix: 底圖設計流程強制寫入 SKILL.md + checklist 重寫含 prompt 範例和風格關鍵字庫",
  "prevention_signal": "Before modifying `betalpha-social/AGENTS.md` or adjacent subsystem, search this registry and inspect the original fixing commit.",
  "verify_trigger": "When the touched subsystem, framework version, or deployment environment changes.",
  "concrete_evidence": "{\n  \"commit\": \"9cac5685f5d88f6a9272998bcb74d100cb7535e7\",\n  \"files\": [\n    \"betalpha-social/AGENTS.md\",\n    \"jonathan/.clawhub/lock.json\",\n    \"jonathan/AGENTS.md\",\n    \"jonathan/post_history/threads_20260330_152400_institutions-divergence.md\",\n    \"jonathan/skills/instagram-image-maker/SKILL.md\",\n    \"jonathan/skills/instagram-image-maker/references/abmedia-visual-style.md\",\n    \"\\\"jonathan/skills/instagram-image-maker/\\\\345\\\\272\\\\225\\\\345\\\\234\\\\226\\\\350\\\\250\\\\255\\\\350\\\\250\\\\210_checklist.md\\\"\",\n    \"jonathan/skills/nano-banana-pro/.clawhub/origin.json\",\n    \"jonathan/skills/nano-banana-pro/SKILL.md\",\n    \"jonathan/skills/nano-banana-pro/_meta.json\",\n    \"jonathan/skills/nano-banana-pro/scripts/generate_image.py\",\n    \"jonathan/skills/threads-scout/data/current_recommendations.md\",\n    \"jonathan/skills/threads-scout/data/keywords.md\",\n    \"jonathan/skills/threads-scout/style_memory.md\",\n    \"research/TOOLS.md\",\n    \"research/data/pipeline_events.jsonl\",\n    \"research/data/runtime/autopilot/active_work.json\",\n    \"research/data/runtime/autopilot/build_manifest.json\",\n    \"research/data/runtime/autopilot/change_ledger.jsonl\",\n    \"research/data/runtime/autopilot/context_budget_view.json\"\n  ],\n  \"reasons\": [\n    \"commit message contains failure/fix signal\",\n    \"touches risky subsystem: betalpha-social/AGENTS.md, research/data/runtime/autopilot/feedback_stream.jsonl, research/data/runtime/pipelines/alpha-distil/2026-03-30T15-55-06+0800-alpha-distil-a1cf99/artifacts/route/route_decisions.json, research/data/runtime/pipelines/alpha-distil/2026-03-30T15-55-06+0800-alpha-distil-a1cf99/artifacts/route/route_decisions.json.meta.json\",\n    \"large change set: 210 files\"\n  ]\n}",
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
    "sha": "9cac5685f5d88f6a9272998bcb74d100cb7535e7",
    "date": "2026-03-30T16:17:31+08:00",
    "files": [
      "betalpha-social/AGENTS.md",
      "jonathan/.clawhub/lock.json",
      "jonathan/AGENTS.md",
      "jonathan/post_history/threads_20260330_152400_institutions-divergence.md",
      "jonathan/skills/instagram-image-maker/SKILL.md",
      "jonathan/skills/instagram-image-maker/references/abmedia-visual-style.md",
      "\"jonathan/skills/instagram-image-maker/\\345\\272\\225\\345\\234\\226\\350\\250\\255\\350\\250\\210_checklist.md\"",
      "jonathan/skills/nano-banana-pro/.clawhub/origin.json",
      "jonathan/skills/nano-banana-pro/SKILL.md",
      "jonathan/skills/nano-banana-pro/_meta.json",
      "jonathan/skills/nano-banana-pro/scripts/generate_image.py",
      "jonathan/skills/threads-scout/data/current_recommendations.md",
      "jonathan/skills/threads-scout/data/keywords.md",
      "jonathan/skills/threads-scout/style_memory.md",
      "research/TOOLS.md",
      "research/data/pipeline_events.jsonl",
      "research/data/runtime/autopilot/active_work.json",
      "research/data/runtime/autopilot/build_manifest.json",
      "research/data/runtime/autopilot/change_ledger.jsonl",
      "research/data/runtime/autopilot/context_budget_view.json",
      "research/data/runtime/autopilot/feedback_stream.jsonl",
      "research/data/runtime/autopilot/heartbeat/20260330T153017+0800.json",
      "research/data/runtime/autopilot/heartbeat/20260330T153017+0800.md",
      "research/data/runtime/autopilot/heartbeat/20260330T153256+0800.json",
      "research/data/runtime/autopilot/heartbeat/20260330T153256+0800.md",
      "research/data/runtime/autopilot/heartbeat/20260330T160526+0800.json",
      "research/data/runtime/autopilot/heartbeat/20260330T160526+0800.md",
      "research/data/runtime/autopilot/heartbeat/20260330T160634+0800.json",
      "research/data/runtime/autopilot/heartbeat/20260330T160634+0800.md",
      "research/data/runtime/autopilot/heartbeat/latest.json"
    ]
  }
}
---

## Symptom

Commit message suggests a potential lesson: fix: 底圖設計流程強制寫入 SKILL.md + checklist 重寫含 prompt 範例和風格關鍵字庫

## Root Cause

Review the commit diff / PR discussion before promotion.

## Wrong Paths

Unknown from git log alone.

## Fix

Inspect with: git show --stat --patch 9cac5685f5d88f6a9272998bcb74d100cb7535e7

## Evidence

{
  "commit": "9cac5685f5d88f6a9272998bcb74d100cb7535e7",
  "files": [
    "betalpha-social/AGENTS.md",
    "jonathan/.clawhub/lock.json",
    "jonathan/AGENTS.md",
    "jonathan/post_history/threads_20260330_152400_institutions-divergence.md",
    "jonathan/skills/instagram-image-maker/SKILL.md",
    "jonathan/skills/instagram-image-maker/references/abmedia-visual-style.md",
    "\"jonathan/skills/instagram-image-maker/\\345\\272\\225\\345\\234\\226\\350\\250\\255\\350\\250\\210_checklist.md\"",
    "jonathan/skills/nano-banana-pro/.clawhub/origin.json",
    "jonathan/skills/nano-banana-pro/SKILL.md",
    "jonathan/skills/nano-banana-pro/_meta.json",
    "jonathan/skills/nano-banana-pro/scripts/generate_image.py",
    "jonathan/skills/threads-scout/data/current_recommendations.md",
    "jonathan/skills/threads-scout/data/keywords.md",
    "jonathan/skills/threads-scout/style_memory.md",
    "research/TOOLS.md",
    "research/data/pipeline_events.jsonl",
    "research/data/runtime/autopilot/active_work.json",
    "research/data/runtime/autopilot/build_manifest.json",
    "research/data/runtime/autopilot/change_ledger.jsonl",
    "research/data/runtime/autopilot/context_budget_view.json"
  ],
  "reasons": [
    "commit message contains failure/fix signal",
    "touches risky subsystem: betalpha-social/AGENTS.md, research/data/runtime/autopilot/feedback_stream.jsonl, research/data/runtime/pipelines/alpha-distil/2026-03-30T15-55-06+0800-alpha-distil-a1cf99/artifacts/route/route_decisions.json, research/data/runtime/pipelines/alpha-distil/2026-03-30T15-55-06+0800-alpha-distil-a1cf99/artifacts/route/route_decisions.json.meta.json",
    "large change set: 210 files"
  ]
}
