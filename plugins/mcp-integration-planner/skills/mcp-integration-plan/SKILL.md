---
name: mcp-integration-plan
description: Use when designing a new MCP-style connector, local tool wrapper, or Codex plugin integration.
---

# MCP Integration Plan

Use this skill to design a tool integration before implementation.

## When To Use

- A new tool, connector, or plugin capability is being considered.
- The integration may read or mutate external state.
- Permissions, schemas, or side effects are not yet clear.
- The user wants an implementation plan before code is written.

## When Not To Use

- The integration already exists and only needs a small bug fix.
- The user asks for a simple local script with no external boundary.
- Required credentials, APIs, or permissions are unknown and cannot be discovered.
- A safer read-only prototype should be built before planning writes.

## Inputs To Gather

- Target system and available API or CLI documentation.
- Operations the user expects.
- Authentication and permission model.
- Data that will cross the boundary.
- Expected failure modes and retry behavior.

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

## Capability Matrix

Separate capabilities by risk:

| Capability | Risk | Confirmation Needed |
| --- | --- | --- |
| Read metadata | Low | Usually no |
| Read private data | Medium | Sometimes |
| Create or update records | High | Yes |
| Delete or revoke access | Very high | Yes |

## Schema Checklist

- Inputs have required and optional fields.
- Outputs are small enough for Codex to inspect.
- Errors are structured and actionable.
- Long-running operations expose progress or status.
- Dry-run mode exists for risky writes when possible.

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

## Verification

Before implementation is considered ready, define:

- unit tests for schema validation
- fixture-based tests for API responses
- a dry-run or read-only smoke test
- logging that does not expose secrets
- rollback instructions for write operations
