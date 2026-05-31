# Repository Instructions

This repository stores Codex skills, plugins, templates, and supporting documentation.

## Working Style

- Keep changes small and easy to review.
- Prefer plain Markdown and simple JSON.
- Do not commit secrets, local caches, generated archives, or machine-specific files.
- Preserve the structure under `skills/`, `plugins/`, `templates/`, and `docs/`.
- Run `python3 scripts/validate_repo.py` after changing skill or plugin metadata.

## Skill Rules

- Each skill must live in its own kebab-case folder under `skills/`.
- Each skill must include a `SKILL.md` file.
- The `SKILL.md` file should start with YAML frontmatter containing `name` and `description`.
- Keep skill instructions focused on when to use the skill and how to execute the workflow.

## Plugin Rules

- Each plugin must live in its own kebab-case folder under `plugins/`.
- Each plugin must include `.codex-plugin/plugin.json`.
- Plugin manifests must be valid JSON and include `name`, `version`, and `description`.

## Documentation Rules

- Put authoring guidance in `docs/`.
- Put reusable starter files in `templates/`.
- Keep examples practical and minimal.
