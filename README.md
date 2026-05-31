# Codex Labkit

Codex Labkit is a home for practical Codex skills, plugins, templates, and notes. The repository is designed to be small enough to learn from, but structured enough to grow into a real personal toolkit.

## What This Repo Contains

- `skills/` - standalone Codex skills with clear `SKILL.md` instructions.
- `plugins/` - local Codex plugins with manifests, bundled skills, and docs.
- `templates/` - copy-ready starting points for new skills and plugins.
- `docs/` - authoring notes, conventions, and design decisions.
- `scripts/` - lightweight repository checks.

## Quick Start

Clone the repo:

```bash
git clone https://github.com/1zerolog/codex-labkit.git
cd codex-labkit
```

Validate the current layout:

```bash
python3 scripts/validate_repo.py
```

Create a new skill from the template:

```bash
mkdir -p skills/my-skill
cp templates/skill/SKILL.md skills/my-skill/SKILL.md
```

Create a new plugin from the template:

```bash
mkdir -p plugins/my-plugin
cp -R templates/plugin/. plugins/my-plugin/
```

## Repository Philosophy

This repo favors:

- clear names over clever names
- small examples over giant demos
- reusable instructions over one-off prompts
- documented structure over hidden assumptions
- local-first artifacts that can be inspected, edited, and versioned

## Current Examples

| Path | Purpose |
| --- | --- |
| `skills/example-repo-cartographer/` | A skill that helps map a repository before editing it. |
| `skills/prototype-review/` | A product-quality review workflow for UI and frontend prototypes. |
| `skills/research-brief/` | A sourced research workflow for literature scans and technical briefs. |
| `skills/repo-knowledge-graph/` | A deeper codebase mapping skill for modules, dependencies, and data flow. |
| `plugins/example-codex-note/` | A minimal plugin scaffold with a bundled note-capture skill. |

## Conventions

- Skill folders use kebab-case.
- Every skill has one `SKILL.md`.
- Every plugin has `.codex-plugin/plugin.json`.
- Examples should be safe, minimal, and easy to delete.
- Generated files, secrets, archives, and local caches do not belong in the repo.

## Status

This is an early lab repository. Expect the structure to evolve as more useful skills and plugins are added.
