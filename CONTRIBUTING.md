# Contributing

Thanks for helping improve Codex Labkit.

## Good Contributions

- a focused Codex skill with clear trigger conditions
- a minimal plugin scaffold that demonstrates one useful pattern
- documentation that makes authoring easier
- validation improvements that catch common mistakes

## Before Opening a Pull Request

1. Keep the change scoped.
2. Run the validation script:

   ```bash
   python3 scripts/validate_repo.py
   ```

3. Explain what the skill, plugin, or document is for.

## Naming

- Use kebab-case for folders.
- Use direct names that describe the workflow.
- Avoid vague names like `helper`, `misc`, or `new-skill`.

## Safety

Do not include:

- API keys or credentials
- private user data
- large generated files
- vendored dependencies
- machine-specific configuration
