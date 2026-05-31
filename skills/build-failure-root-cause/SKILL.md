---
name: build-failure-root-cause
description: Use when a build fails and the first actionable compiler or bundler error must be found.
---

# Build Failure Root Cause

Reduce build output to the real failure.

## Workflow

1. Run the build command.
2. Find the first non-cascading error.
3. Map it to source files.
4. Patch and rerun the smallest validation.

