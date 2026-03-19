---
name: add-ecc-bundle
description: Workflow command scaffold for add-ecc-bundle in lolmuse.
allowed_tools: ["Bash", "Read", "Write", "Grep", "Glob"]
---

# /add-ecc-bundle

Use this workflow when working on **add-ecc-bundle** in `lolmuse`.

## Goal

Adds a new ECC (Extended Cognitive Component) bundle to the project, including commands, agent configs, skills, and tool definitions.

## Common Files

- `.claude/commands/*.md`
- `.codex/agents/*.toml`
- `.agents/skills/lolmuse/*`
- `.claude/skills/lolmuse/SKILL.md`
- `.claude/ecc-tools.json`
- `.claude/identity.json`

## Suggested Sequence

1. Understand the current state and failure mode before editing.
2. Make the smallest coherent change that satisfies the workflow goal.
3. Run the most relevant verification for touched files.
4. Summarize what changed and what still needs review.

## Typical Commit Signals

- Add or update .claude/commands/*.md files for new commands.
- Add or update .codex/agents/*.toml files for agent configurations.
- Add or update .agents/skills/lolmuse/* for skill definitions.
- Add or update .claude/skills/lolmuse/SKILL.md for skill documentation.
- Add or update .claude/ecc-tools.json for tool definitions.

## Notes

- Treat this as a scaffold, not a hard-coded script.
- Update the command if the workflow evolves materially.