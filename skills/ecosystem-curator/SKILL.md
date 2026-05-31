---
name: ecosystem-curator
description: Use when updating Codex Labkit from public Codex skill, plugin, MCP, or agent ecosystem sources.
---

# Ecosystem Curator

Use this skill to scan public Codex-related repositories and turn useful patterns into original Labkit entries.

## Workflow

1. Search public sources:
   - official Codex skill catalogs
   - awesome lists
   - popular skill libraries
   - plugin marketplaces
   - MCP integration examples
2. Record source links and metadata:
   - repository
   - license
   - popularity signal
   - relevant category
3. Choose one candidate at a time.
4. Decide whether it should become:
   - a standalone skill
   - a plugin
   - a template
   - a documentation note
5. Write original Codex Labkit instructions.
6. Validate the repository.
7. Commit that single addition before moving to the next candidate.

## Adaptation Checklist

- The entry has a clear trigger.
- The workflow is Codex-native.
- The source is linked when it influenced the category.
- No upstream files are copied wholesale.
- The entry is small enough to maintain.
- The validation script passes.

## Commit Pattern

Use one commit per adapted item:

```text
Add <name> skill
Add <name> plugin
Document <name> source pattern
```

## Safety Notes

- Check licenses before copying any text or code.
- Prefer original summaries and workflows.
- Do not import large third-party dependencies without a strong reason.
- Do not add tools that require secrets unless the setup path is documented.
