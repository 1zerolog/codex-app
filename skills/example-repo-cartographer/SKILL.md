---
name: repo-cartographer
description: Use when you need to understand a repository before making changes, especially when ownership boundaries, test commands, or file layout are unclear.
---

# Repo Cartographer

Use this skill to build a quick map of a repository before editing it.

## Workflow

1. List top-level files and directories.
2. Read the main README and any repository instruction files.
3. Identify the project type, package manager, and test entry points.
4. Locate the files most likely related to the user's request.
5. Summarize the map before making broad edits.

## Preferred Commands

```bash
rg --files
git status --short --branch
find . -maxdepth 2 -type f
```

## Output

Return a short repository map with:

- purpose
- key directories
- likely edit targets
- validation commands
- open questions, if any
