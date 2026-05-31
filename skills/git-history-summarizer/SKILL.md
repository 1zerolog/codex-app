---
name: git-history-summarizer
description: Use when recent commits need to be summarized for context, release notes, or handoff.
---

# Git History Summarizer

## Purpose

Use this skill when recent commits need to be summarized for context, release notes, or handoff. It turns the request into a repeatable workflow with clear checks, outputs, and validation.

## When To Use

- The user request matches this skill's description.
- The work has enough risk that a checklist is useful.
- The repository already has files, tests, or conventions that should guide the answer.
- A concise plan or review artifact would make the next step clearer.

## When Not To Use

- The task is a one-line factual answer with no repository impact.
- The user explicitly asks for a quick command only.
- A narrower skill fits better and would avoid unnecessary process.
- The required information is unavailable and cannot be discovered locally or from trusted sources.

## Inputs To Gather

- User goal and expected deliverable.
- Relevant files, commands, logs, or links.
- Existing repository conventions and instruction files.
- Risk constraints such as security, data loss, compatibility, or release timing.

## Signals To Inspect

- Commit themes.
- Risk changes.
- Breaking changes.
- Release notes.

## Preferred Commands

```bash
git log --oneline --decorate -50
git diff --stat <base>..HEAD
```

## Workflow

1. Restate the target outcome in one sentence.
2. Inspect the smallest relevant part of the repository first.
3. Identify the current behavior, contract, or state before suggesting changes.
4. Find the most important risk or uncertainty.
5. Propose or implement the smallest useful action.
6. Validate with the most relevant local command, test, or manual check.
7. Summarize what changed, what was verified, and what remains.

## Checklist

- Scope is clear and not broader than the user asked for.
- Existing project conventions were checked before inventing new structure.
- Risks are named directly.
- Validation is specific, not hand-wavy.
- Output is short enough to be useful but detailed enough to act on.

## Output Format

```markdown
## Git History Summarizer Result

Goal:

Findings:

Recommended action:

Validation:

Risks or follow-up:
```

## Quality Bar

The result should be practical enough that another engineer can continue from it without rereading the whole repository. Prefer concrete file paths, commands, examples, and decision points over generic advice.

## Common Pitfalls

- Starting with a broad refactor before understanding the local pattern.
- Treating generated files, caches, or vendored dependencies as source of truth.
- Reporting every observation instead of the few that change the decision.
- Claiming validation happened when no command or concrete check was run.

## Deliverable

Produce a grouped history summary.
