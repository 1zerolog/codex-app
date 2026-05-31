# Plugins

This directory contains local Codex plugin examples and experiments.

## Layout

```text
plugins/
  example-plugin/
    .codex-plugin/
      plugin.json
    README.md
```

## Add a Plugin

```bash
mkdir -p plugins/my-plugin
cp -R templates/plugin/. plugins/my-plugin/
```

Then update `.codex-plugin/plugin.json` and the plugin README.

## Included Plugins

| Plugin | Purpose |
| --- | --- |
| `agent-workbench` | Plan specialist roles and handoffs for complex Codex work. |
| `example-codex-note` | Minimal plugin scaffold with one bundled note skill. |
| `mcp-integration-planner` | Plan MCP-style tool integrations, schemas, permissions, and validation. |
