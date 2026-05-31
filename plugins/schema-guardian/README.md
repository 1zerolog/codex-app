# Schema Guardian

Schema Guardian is a Codex Labkit plugin for reviewing schemas and compatibility boundaries. It packages a focused workflow as a bundled skill so Codex can approach this category of work consistently.

## Why This Plugin Exists

Codex works best when broad requests are converted into clear investigation, action, and verification loops. This plugin gives Codex a repeatable path for reviewing schemas and compatibility boundaries, with enough structure to be useful and enough restraint to avoid ceremony.

## Bundled Skill

- `schema` - the main workflow used by this plugin.

## Good Fits

- The user asks for help with reviewing schemas and compatibility boundaries.
- The repository has existing conventions that should be respected.
- The task has review, validation, or risk considerations.
- A concise artifact would help the user or the next maintainer continue.

## Poor Fits

- The user only needs a one-line factual answer.
- The work is unrelated to this plugin's domain.
- The safest next step is to ask for missing context.
- A narrower existing skill should handle the request.

## Codex Optimization

This plugin is designed for Codex sessions where local repository context matters. It favors:

- reading existing files before inventing structure
- using `rg` and targeted commands over broad scraping
- producing compact, reviewable outputs
- naming validation explicitly
- keeping user-owned unrelated changes untouched

## Typical Flow

1. Resolve the exact goal.
2. Inspect the smallest useful repository surface.
3. Identify risks, assumptions, and likely edit targets.
4. Apply the bundled skill workflow.
5. Validate with a local command or concrete check.
6. Summarize outcome, evidence, and remaining risk.

## Safety

If the workflow can touch secrets, external systems, destructive operations, or user data, Codex should stop at a plan until the user confirms the action. Read-only analysis should still avoid exposing sensitive values in summaries.

## Validation

Run repository validation after edits:

```bash
python3 scripts/validate_repo.py
```
