---
name: agent-roster
description: Use when a task is broad enough to benefit from specialist roles, staged execution, or explicit handoffs.
---

# Agent Roster

Use this skill to break a complex request into specialist roles before execution.

## Workflow

1. Identify the goal and expected deliverable.
2. Split the work into roles:
   - researcher
   - architect
   - implementer
   - reviewer
   - verifier
   - release preparer
3. Assign responsibilities to each role.
4. Define what evidence each role must produce.
5. Choose the smallest role set that handles the task.
6. Execute the work in order, collapsing roles when the task is small.

## Output Format

```markdown
## Roster

- Goal:
- Roles:
- Execution order:
- Validation:
- Handoff notes:
```

## Guidance

- Do not over-plan simple changes.
- Do not create artificial roles when one focused pass is enough.
- Use the roster to reduce missed work, not to add ceremony.
