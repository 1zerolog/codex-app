---
name: secrets-leak-scan
description: Use when a repository or diff needs a quick scan for committed secrets and sensitive files.
---

# Secrets Leak Scan

Look for accidental sensitive data.

## Workflow

1. Scan env files, keys, tokens, and private certs.
2. Review recent diffs.
3. Check ignore rules.
4. Recommend rotation if a secret was exposed.

