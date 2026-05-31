# Security Policy

Codex Labkit is a public collection of local tools, templates, and instructions.

## Reporting Security Issues

If you find a security issue, open a private communication channel with the maintainer instead of publishing exploit details in an issue.

## Sensitive Data

Never commit:

- API keys
- tokens
- private certificates
- browser cookies
- local app data
- personal documents

## Plugin and Skill Safety

Skills and plugins should make external side effects explicit. If a workflow can modify files, call APIs, publish data, or change accounts, document that behavior clearly in the relevant `SKILL.md` or plugin README.
