# OpenClaw lifecycle integration

Betavibe can run as an OpenClaw hook plugin so agents get relevant insight context without relying only on manual discipline.

## What it does

- `before_prompt_build`: detects non-trivial coding/spec prompts and runs:
  - `python3 -m betavibe resolve pre_spec ...`
  - or `python3 -m betavibe resolve pre_implement ...`
- `after_tool_call`: records bounded telemetry for the active run: tool count, error-like outputs, touched file hints.
- `agent_end`: runs `should-capture` after likely hard-won debugging sessions. It never writes reviewed insights automatically; it queues next-turn context asking for human approval when capture is recommended.

## Safety / performance guarantees

- Resolver hook has a short timeout (`maxResolveMs`, default 2500 ms).
- Prompt injection is capped (`maxPromptChars`, default 3500 chars).
- Capture detector is dry-run by default and only queues a reminder; reviewed registry writes still require human approval and explicit `capture --sync-gbrain`.
- Audit events are written to `.betavibe/lifecycle-events.jsonl`.
- If Betavibe is slow or unavailable, OpenClaw continues without blocking the agent.
- The plugin reads config from hook `event.context.pluginConfig` when available and falls back to `api.pluginConfig`, because some hook surfaces do not expose plugin config on every event.

## Install locally

From the Betavibe repository:

```bash
openclaw plugins install --link --dangerously-force-unsafe-install adapters/openclaw/betavibe-lifecycle-plugin
openclaw plugins enable betavibe-lifecycle
openclaw config set plugins.entries.betavibe-lifecycle '{
  "enabled": true,
  "hooks": { "allowConversationAccess": true },
  "config": {
    "projectRoot": "/path/to/project",
    "betavibePath": "/path/to/project/Betalpha-vibe-coding-partner",
    "registry": "/path/to/project/.betavibe/registry",
    "enabled": true,
    "maxResolveMs": 2500,
    "maxPromptChars": 3500,
    "minDebugMinutes": 20,
    "maxSessionChecksMs": 3000,
    "dryRun": true
  }
}' --strict-json --merge
openclaw gateway restart
```

`--dangerously-force-unsafe-install` is required because the plugin uses `child_process` to call the fixed local Betavibe CLI. The plugin does not execute model-provided shell strings.

## Verify

```bash
openclaw plugins inspect betavibe-lifecycle --json
cat .betavibe/lifecycle-events.jsonl
```

Expected hooks:

- `before_prompt_build`
- `after_tool_call`
- `agent_end`

Expected diagnostics: none.
