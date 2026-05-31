---
name: agent-roster
description: Use when a task is broad enough to benefit from specialist roles, staged execution, or explicit handoffs.
---

# Agent Roster

Use this skill to break a complex request into specialist roles before execution. It does not need actual sub-agents to be useful; the point is to make responsibilities, evidence, and handoffs explicit before work begins.

## When To Use

- The user asks for a broad project outcome.
- The task mixes research, design, implementation, review, and release work.
- Several areas of the repository will be touched.
- A mistake would be easier to avoid with staged execution.

## When Not To Use

- The task is a single small edit.
- The user only wants a quick answer.
- The repository context is already obvious and the risk is low.
- Role planning would add ceremony without reducing uncertainty.

## Inputs To Gather

- User goal and deadline, if any.
- Repository area and likely affected systems.
- Available validation commands.
- Known constraints such as security, data migration, or public API compatibility.

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

## Role Catalog

Use only the roles needed for the current request:

- Researcher: gathers sources, existing patterns, and unknowns.
- Architect: defines boundaries, data flow, and integration points.
- Implementer: makes the smallest coherent code or document change.
- Reviewer: looks for regressions, risks, and missing tests.
- Verifier: runs tests, builds, smoke checks, or manual validation.
- Release preparer: prepares changelog, PR description, rollout, and rollback notes.

## Planning Checklist

- Every role has a concrete output.
- No role duplicates another role's work.
- Validation is assigned before implementation starts.
- Handoffs identify what the next role should trust and what it should re-check.
- The plan can be collapsed if the task turns out to be simpler than expected.

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

## Example Output

```markdown
## Roster

- Goal: Add a plugin scaffold and publish it safely.
- Roles:
  - Researcher: inspect existing plugin examples and manifest rules.
  - Implementer: add files and update docs.
  - Verifier: run repository validation.
  - Release preparer: commit, push, and summarize.
- Execution order: Researcher -> Implementer -> Verifier -> Release preparer.
- Validation: python3 scripts/validate_repo.py
- Handoff notes: keep each plugin addition in its own commit.
```
