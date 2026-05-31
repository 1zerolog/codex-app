# Repository Architecture

Codex Labkit separates reusable assets by how they are consumed.

## `skills/`

Standalone skills live here. A skill is a folder with a `SKILL.md` file that explains when Codex should use it and how the workflow should run.

## `plugins/`

Plugins live here. A plugin is a folder with a `.codex-plugin/plugin.json` manifest. Plugins may contain bundled skills, scripts, docs, or MCP server configuration.

## `templates/`

Templates are starter files. They should be boring, predictable, and easy to copy.

## `docs/`

Docs explain conventions and authoring decisions. If a rule is not obvious from the file structure, document it here.

## `scripts/`

Scripts should be dependency-light and safe to run locally. The first script is `validate_repo.py`, which checks skill and plugin metadata.
