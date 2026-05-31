---
name: repo-knowledge-graph
description: Use when a codebase needs to be mapped into modules, data flow, dependencies, and ownership boundaries before planning or editing.
---

# Repo Knowledge Graph

Use this skill to turn a repository into a practical mental graph before making changes. It is inspired by popular agent-skill projects that convert codebases into queryable knowledge maps, but this version stays dependency-light and Codex-native.

## Workflow

1. Read repository instructions first: `AGENTS.md`, `README.md`, `CONTRIBUTING.md`, and package manifests.
2. List files with `rg --files`, excluding build outputs, caches, dependencies, and generated artifacts.
3. Identify nodes:
   - packages
   - applications
   - entry points
   - shared libraries
   - tests
   - configuration
   - external integrations
4. Identify edges:
   - imports and package dependencies
   - API calls
   - CLI entry points
   - data files read or written
   - environment variables
   - test coverage relationships
5. Produce a compact map before editing.

## Suggested Commands

```bash
rg --files
find . -maxdepth 3 -type f
rg "from |import |require\\(|process\\.env|os\\.environ|fetch\\(|axios|requests\\."
rg "def |class |function |export |module\\.exports"
```

## Output Format

```markdown
## Repository Map

- Purpose:
- Entry points:
- Core modules:
- Data flow:
- External systems:
- Tests:
- Risk areas:
- Best edit targets:
```

## Safety Notes

- Do not index secrets or private data into summaries.
- Treat generated files as implementation output, not source of truth.
- If the repository is large, map the area relevant to the user's request first.
