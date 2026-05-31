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
