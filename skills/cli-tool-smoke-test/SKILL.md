---
name: cli-tool-smoke-test
description: Use when a command-line tool needs a quick install, help, and basic command verification pass.
---

# CLI Tool Smoke Test

Validate a CLI without doing a full test campaign.

## Workflow

1. Find install and run commands.
2. Check `--help` and version output.
3. Run one safe read-only command.
4. Report failures and missing docs.

