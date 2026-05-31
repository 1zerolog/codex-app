# Skill Authoring Guide

A good Codex skill answers three questions:

1. When should this skill be used?
2. What exact workflow should Codex follow?
3. What files, scripts, or references should Codex prefer?

## Required Shape

Every skill should include:

```markdown
---
name: useful-skill-name
description: Use when ...
---

# Useful Skill Name

Instructions go here.
```

## Writing Tips

- Start the description with a clear trigger.
- Keep workflows ordered and actionable.
- Prefer local scripts over long copied commands.
- Mention safety constraints near the action that needs them.
- Avoid broad claims like "always do everything perfectly."

## Folder Naming

Use kebab-case:

- `repo-cartographer`
- `release-notes`
- `browser-smoke-test`

Avoid:

- `RepoCartographer`
- `new_skill`
- `misc`
