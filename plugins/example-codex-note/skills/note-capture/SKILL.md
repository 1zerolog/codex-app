---
name: note-capture
description: Use when the user wants a concise project note, decision record, or handoff summary saved as Markdown.
---

# Note Capture

Use this skill to turn a conversation, implementation decision, or handoff into a compact Markdown note. The note should help future work continue without forcing someone to reread an entire thread.

## When To Use

- The user asks to save a note, decision, or handoff.
- A useful decision happened during implementation.
- A project needs a short record of context and next steps.
- A future agent or maintainer will need the reasoning.

## When Not To Use

- The user only wants a chat summary.
- The information is sensitive and should not be written to disk.
- The note would duplicate an existing document without adding clarity.
- The decision is still unresolved and needs discussion first.

## Inputs To Gather

- The decision or event being captured.
- Relevant files, commands, or links.
- Follow-up tasks and owners, if known.
- Any caveats or open questions.

## Workflow

1. Identify the note purpose.
2. Capture decisions, context, and follow-up work.
3. Keep the note short and skimmable.
4. Save it only when the user asks for a file.
5. Use a filename that reflects the topic and date if the user did not specify one.

## Suggested Sections

- Context
- Decision
- Details
- Follow-up

## Output Format

```markdown
# Short Note Title

## Context

## Decision

## Details

## Follow-up
```

## Quality Bar

- A reader can understand the decision in under one minute.
- The note says what changed and why.
- Follow-up work is concrete.
- Sensitive data is omitted or redacted.
