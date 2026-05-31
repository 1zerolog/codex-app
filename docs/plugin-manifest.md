# Plugin Manifest Notes

Each plugin must include:

```text
.codex-plugin/plugin.json
```

The manifest should be valid JSON and include at least:

```json
{
  "name": "example-plugin",
  "version": "0.1.0",
  "description": "A short description."
}
```

## Suggested Fields

- `name` - stable plugin identifier
- `version` - semantic version
- `description` - one-sentence summary
- `author` - maintainer name or handle
- `skills` - optional list of bundled skill folders

## Practical Advice

- Keep plugin names lowercase and hyphenated.
- Keep manifests small until the plugin needs more metadata.
- Document each plugin in its own `README.md`.
