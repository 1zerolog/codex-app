# Skills

This directory contains standalone Codex skills.

## Layout

```text
skills/
  example-skill/
    SKILL.md
```

## Add a Skill

```bash
mkdir -p skills/my-skill
cp templates/skill/SKILL.md skills/my-skill/SKILL.md
```

Then edit the frontmatter and workflow instructions.

## Included Skills

| Skill | Purpose |
| --- | --- |
| `ecosystem-curator` | Scan public Codex ecosystem sources and adapt one item per commit. |
| `example-repo-cartographer` | Minimal example for mapping a repository before editing. |
| `prototype-review` | Review frontend prototypes for product-quality layout, states, and UX. |
| `research-brief` | Produce sourced research briefs with uncertainty and citation discipline. |
| `repo-knowledge-graph` | Map modules, data flow, dependencies, and ownership boundaries. |
