---
name: add-ecc-bundle
description: Workflow command scaffold for add-ecc-bundle in lolmuse.
allowed_tools: ["Bash", "Read", "Write", "Grep", "Glob"]
---

# /add-ecc-bundle

Use this workflow when working on **add-ecc-bundle** in `lolmuse`.

## Goal

Adds a new ECC (Extensible Cognitive Component) bundle, which includes configuration, agent definitions, skills, and documentation files for the lolmuse system.

## Common Files

- `.claude/commands/project-initialization.md`
- `.claude/homunculus/instincts/inherited/*.yaml`
- `.codex/agents/*.toml`
- `.codex/AGENTS.md`
- `.codex/config.toml`
- `.claude/identity.json`

## Suggested Sequence

1. Understand the current state and failure mode before editing.
2. Make the smallest coherent change that satisfies the workflow goal.
3. Run the most relevant verification for touched files.
4. Summarize what changed and what still needs review.

## Typical Commit Signals

- Create or update .claude/commands/project-initialization.md
- Add or update .claude/homunculus/instincts/inherited/*.yaml
- Add or update .codex/agents/*.toml
- Add or update .codex/AGENTS.md
- Add or update .codex/config.toml

## Notes

- Treat this as a scaffold, not a hard-coded script.
- Update the command if the workflow evolves materially.