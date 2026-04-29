---
{
  "title": "argparse REMAINDER can swallow run-exec options",
  "type": "pitfall",
  "tags": [
    "betavibe",
    "runtime-capture",
    "argparse",
    "cli"
  ],
  "tech_stack": [
    "python"
  ],
  "summary": "Betavibe runtime capture initially defined run-exec command with argparse.REMAINDER immediately after run_id, causing --cwd/--no-fail to be captured as the child command instead of parsed as Betavibe options.",
  "prevention_signal": "When adding wrapper CLI commands that forward arbitrary child commands, test option parsing with parent options plus '--' and child flags like python -c before shipping.",
  "verify_trigger": "When changing Betavibe run-exec, capture wrappers, or argparse forwarding behavior.",
  "created_at": "2026-04-29",
  "last_verified_at": "2026-04-29",
  "source": {
    "kind": "manual",
    "created_by": "betalpha"
  }
}
---

## Symptom

run-exec tried to execute '--cwd' and failed with FileNotFoundError instead of running the intended child command.

## Root Cause

argparse positional REMAINDER starts consuming arguments as soon as it is reached; placing it after run_id meant later options were no longer parsed by the parent CLI.

## Wrong Paths

Keeping command as argparse.REMAINDER after run_id and expecting --cwd/--no-fail after run_id to parse normally.

## Fix

Define --cwd/--no-fail before the command positional and use nargs='+' with '--' for child command flags; strip leading '--' before subprocess execution.

## Evidence

failed: pytest test_runtime_capture_records_failed_then_passing_command with FileNotFoundError '--cwd'; passed: python3 -m pytest -q => 15 passed
