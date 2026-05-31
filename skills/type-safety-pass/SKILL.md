---
name: type-safety-pass
description: Use when TypeScript, Python typing, or schema types need a stricter safety pass.
---

# Type Safety Pass

Tighten types where they protect behavior.

## Workflow

1. Find `any`, ignored errors, and loose dicts.
2. Identify boundary types.
3. Add precise types incrementally.
4. Run type checks.

