---
name: mcp-integration-plan
description: Use when designing a new MCP-style connector, local tool wrapper, or Codex plugin integration.
---

# MCP Integration Plan

Use this skill to design a tool integration before implementation.

## Workflow

1. Define the user-facing capability.
2. Identify the backing system:
   - local CLI
   - local app
   - web API
   - database
   - repository automation
3. List required operations:
   - read-only
   - write
   - destructive
   - long-running
4. Define permissions and confirmation points.
5. Define input and output schemas.
6. Plan validation:
   - unit tests
   - dry-run mode
   - fixture data
   - manual smoke test
7. Document failure modes and rollback behavior.

## Output Format

```markdown
## Integration Plan

- Capability:
- Backing system:
- Operations:
- Permissions:
- Schemas:
- Validation:
- Risks:
- Rollback:
```

## Safety Notes

- Treat write and destructive operations as separate capabilities.
- Never hide external side effects.
- Avoid requiring broad tokens when scoped credentials would work.
- Prefer dry-run support before real mutation.
