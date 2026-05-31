---
name: dependency-upgrade-plan
description: Use when package dependencies need upgrading without breaking the project.
---

# Dependency Upgrade Plan

Upgrade dependencies in a controlled way.

## Workflow

1. Identify package manager and lockfile.
2. Check changelogs for breaking changes.
3. Upgrade the smallest safe set.
4. Run build and tests.

