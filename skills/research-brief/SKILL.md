---
name: research-brief
description: Use when the user needs a sourced research brief, literature scan, or technical topic summary with clear uncertainty and citations.
---

# Research Brief

Use this skill to create a concise, sourced research brief. It is inspired by popular scientific agent-skill libraries, but this version is intentionally general, citation-first, and careful about uncertainty.

## Workflow

1. Restate the research question in one sentence.
2. Identify the domain and risk level:
   - software or engineering
   - scientific or academic
   - medical, legal, or financial
   - product or market
3. Prefer primary sources:
   - official documentation
   - standards
   - papers
   - repository docs
   - regulatory pages
4. Collect 3 to 7 strong sources.
5. Separate facts from interpretation.
6. Produce a brief with citations and dated context.

## Output Format

```markdown
## Research Brief

Question:

Key takeaways:

Evidence:

Uncertainty:

Recommended next step:
```

## Source Rules

- Use current sources when the topic may have changed.
- Prefer primary sources over blog summaries.
- Link every source used.
- Note when a claim is an inference.
- Avoid quoting long copyrighted passages.

## High-Stakes Topics

For medical, legal, financial, safety, or regulatory topics:

- verify current information
- avoid overconfident advice
- include jurisdiction or date when relevant
- recommend expert review when decisions have real-world consequences
