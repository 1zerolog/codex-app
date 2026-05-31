---
name: pr-prep
description: Use when Codex needs help with preparing branch changes for a clean pull request.
---

# PR Prep Station Skill

## Purpose

Use this skill when Codex needs to handle preparing branch changes for a clean pull request. The goal is to create a dependable workflow that turns a broad request into inspection, action, validation, and a concise user-facing result.

## When To Use

- The user request clearly fits this plugin domain.
- The task touches repository files, workflows, tests, or documented behavior.
- There are risks or assumptions that should be named before acting.
- A structured result will make review or follow-up easier.

## When Not To Use

- The user asks for a tiny answer that does not need repository work.
- Another skill is more specific to the problem.
- Required context is missing and cannot be discovered.
- The next step would transmit sensitive data or perform a destructive action without confirmation.

## Inputs To Gather

- User goal and expected output.
- Relevant files, commands, logs, URLs, or screenshots.
- Existing repository instructions such as `AGENTS.md`, `README.md`, and contribution docs.
- Validation commands that already exist in the project.
- Constraints around security, compatibility, release timing, or data safety.

## Signals To Inspect

- diff summary.
- validation.
- risk notes.
- reviewer context.

## Preferred Commands

```bash
git diff --stat
git log --oneline origin/main..HEAD
git status --short
```

## Workflow

1. State the target outcome in one sentence.
2. Inspect local instructions and the smallest relevant file set.
3. Identify current behavior, expected behavior, and any public contract.
4. Name risks and unknowns before changing files.
5. Choose the smallest useful implementation, document, or plan.
6. Validate with the closest available command or manual check.
7. Summarize what changed, what was verified, and what remains.

## Decision Checklist

- Does this request belong to this plugin domain?
- What existing project pattern should be followed?
- What is the smallest useful artifact or code change?
- What could break if the recommendation is wrong?
- What validation would give the user real confidence?

## Output Format

```markdown
## PR Prep Station Result

Goal:

What I inspected:

Findings:

Action taken or recommended:

Validation:

Risks or follow-up:
```

## Quality Bar

The result should be actionable without being bloated. Prefer specific file paths, commands, and decision points. Avoid generic advice that could apply to any repository.

## Common Pitfalls

- Skipping repository instructions.
- Treating generated files as source of truth.
- Mixing unrelated cleanup into the requested work.
- Claiming validation when no concrete check was run.
- Producing a plan that does not name the next command or file to inspect.

## Deliverable

Produce a PR-ready summary.
