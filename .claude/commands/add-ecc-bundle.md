---
name: add-ecc-bundle
description: Workflow command scaffold for add-ecc-bundle in lolmuse.
allowed_tools: ["Bash", "Read", "Write", "Grep", "Glob"]
---

# /add-ecc-bundle

Use this workflow when working on **add-ecc-bundle** in `lolmuse`.

## Goal

Adds a new ECC bundle to the lolmuse project, including commands, skills, identity, and agent configurations.

## Common Files

- `.claude/commands/add-ecc-bundle.md`
- `.claude/commands/feature-development.md`
- `.claude/commands/backend-feature-addition.md`
- `.claude/commands/project-initialization.md`
- `.claude/identity.json`
- `.claude/ecc-tools.json`

## Suggested Sequence

1. Understand the current state and failure mode before editing.
2. Make the smallest coherent change that satisfies the workflow goal.
3. Run the most relevant verification for touched files.
4. Summarize what changed and what still needs review.

## Typical Commit Signals

- Add or update .claude/commands/add-ecc-bundle.md
- Add or update .claude/commands/feature-development.md
- Add or update .claude/commands/backend-feature-addition.md
- Add or update .claude/commands/project-initialization.md
- Add or update .claude/identity.json

## Notes

- Treat this as a scaffold, not a hard-coded script.
- Update the command if the workflow evolves materially.