---
{
  "title": "fix: 內頁漸層改為一體式全幅底圖+黑色漸層覆蓋",
  "type": "pitfall",
  "tags": [
    "test"
  ],
  "tech_stack": [
    "python"
  ],
  "summary": "Git history candidate from `clawd` commit `8ecac37bb092`: fix: 內頁漸層改為一體式全幅底圖+黑色漸層覆蓋",
  "prevention_signal": "Before modifying `betalpha-social/AGENTS.md` or adjacent subsystem, search this registry and inspect the original fixing commit.",
  "verify_trigger": "When the touched subsystem, framework version, or deployment environment changes.",
  "concrete_evidence": "{\n  \"commit\": \"8ecac37bb092dcae7562bdc19f43b19d89f00f26\",\n  \"files\": [\n    \"betalpha-social/AGENTS.md\",\n    \"betalpha-social/TOOLS.md\",\n    \"jonathan/AGENTS.md\",\n    \"jonathan/TOOLS.md\",\n    \"jonathan/memory/2026-03-30.md\",\n    \"jonathan/skills/instagram-image-maker/SKILL.md\",\n    \"jonathan/skills/instagram-image-maker/compose.py\",\n    \"jonathan/skills/instagram-image-maker/learning_log.md\",\n    \"research/data/feedback_compiler.json\",\n    \"research/data/feedback_compiler.md\",\n    \"research/data/pipeline_events.jsonl\",\n    \"research/data/runtime/autopilot/active_work.json\",\n    \"research/data/runtime/autopilot/build_manifest.json\",\n    \"research/data/runtime/autopilot/change_ledger.jsonl\",\n    \"research/data/runtime/autopilot/context_budget_view.json\",\n    \"research/data/runtime/autopilot/feedback_stream.jsonl\",\n    \"research/data/runtime/autopilot/heartbeat/20260330T140131+0800.json\",\n    \"research/data/runtime/autopilot/heartbeat/20260330T140131+0800.md\",\n    \"research/data/runtime/autopilot/heartbeat/20260330T143030+0800.json\",\n    \"research/data/runtime/autopilot/heartbeat/20260330T143030+0800.md\"\n  ],\n  \"reasons\": [\n    \"commit message contains failure/fix signal\",\n    \"touches risky subsystem: betalpha-social/AGENTS.md, betalpha-social/TOOLS.md, jonathan/skills/instagram-image-maker/compose.py, research/data/feedback_compiler.json\",\n    \"large change set: 234 files\"\n  ]\n}",
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
    "sha": "8ecac37bb092dcae7562bdc19f43b19d89f00f26",
    "date": "2026-03-30T15:13:22+08:00",
    "files": [
      "betalpha-social/AGENTS.md",
      "betalpha-social/TOOLS.md",
      "jonathan/AGENTS.md",
      "jonathan/TOOLS.md",
      "jonathan/memory/2026-03-30.md",
      "jonathan/skills/instagram-image-maker/SKILL.md",
      "jonathan/skills/instagram-image-maker/compose.py",
      "jonathan/skills/instagram-image-maker/learning_log.md",
      "research/data/feedback_compiler.json",
      "research/data/feedback_compiler.md",
      "research/data/pipeline_events.jsonl",
      "research/data/runtime/autopilot/active_work.json",
      "research/data/runtime/autopilot/build_manifest.json",
      "research/data/runtime/autopilot/change_ledger.jsonl",
      "research/data/runtime/autopilot/context_budget_view.json",
      "research/data/runtime/autopilot/feedback_stream.jsonl",
      "research/data/runtime/autopilot/heartbeat/20260330T140131+0800.json",
      "research/data/runtime/autopilot/heartbeat/20260330T140131+0800.md",
      "research/data/runtime/autopilot/heartbeat/20260330T143030+0800.json",
      "research/data/runtime/autopilot/heartbeat/20260330T143030+0800.md",
      "research/data/runtime/autopilot/heartbeat/20260330T143205+0800.json",
      "research/data/runtime/autopilot/heartbeat/20260330T143205+0800.md",
      "research/data/runtime/autopilot/heartbeat/20260330T150026+0800.json",
      "research/data/runtime/autopilot/heartbeat/20260330T150026+0800.md",
      "research/data/runtime/autopilot/heartbeat/latest.json",
      "research/data/runtime/autopilot/heartbeat/latest.md",
      "research/data/runtime/autopilot/overview/20260330T140223+0800.json",
      "research/data/runtime/autopilot/overview/20260330T140223+0800.md",
      "research/data/runtime/autopilot/overview/20260330T150442+0800.json",
      "research/data/runtime/autopilot/overview/20260330T150442+0800.md"
    ]
  }
}
---

## Symptom

Commit message suggests a potential lesson: fix: 內頁漸層改為一體式全幅底圖+黑色漸層覆蓋

## Root Cause

Review the commit diff / PR discussion before promotion.

## Wrong Paths

Unknown from git log alone.

## Fix

Inspect with: git show --stat --patch 8ecac37bb092dcae7562bdc19f43b19d89f00f26

## Evidence

{
  "commit": "8ecac37bb092dcae7562bdc19f43b19d89f00f26",
  "files": [
    "betalpha-social/AGENTS.md",
    "betalpha-social/TOOLS.md",
    "jonathan/AGENTS.md",
    "jonathan/TOOLS.md",
    "jonathan/memory/2026-03-30.md",
    "jonathan/skills/instagram-image-maker/SKILL.md",
    "jonathan/skills/instagram-image-maker/compose.py",
    "jonathan/skills/instagram-image-maker/learning_log.md",
    "research/data/feedback_compiler.json",
    "research/data/feedback_compiler.md",
    "research/data/pipeline_events.jsonl",
    "research/data/runtime/autopilot/active_work.json",
    "research/data/runtime/autopilot/build_manifest.json",
    "research/data/runtime/autopilot/change_ledger.jsonl",
    "research/data/runtime/autopilot/context_budget_view.json",
    "research/data/runtime/autopilot/feedback_stream.jsonl",
    "research/data/runtime/autopilot/heartbeat/20260330T140131+0800.json",
    "research/data/runtime/autopilot/heartbeat/20260330T140131+0800.md",
    "research/data/runtime/autopilot/heartbeat/20260330T143030+0800.json",
    "research/data/runtime/autopilot/heartbeat/20260330T143030+0800.md"
  ],
  "reasons": [
    "commit message contains failure/fix signal",
    "touches risky subsystem: betalpha-social/AGENTS.md, betalpha-social/TOOLS.md, jonathan/skills/instagram-image-maker/compose.py, research/data/feedback_compiler.json",
    "large change set: 234 files"
  ]
}
