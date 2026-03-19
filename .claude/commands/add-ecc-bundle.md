---
name: add-ecc-bundle
description: Workflow command scaffold for add-ecc-bundle in lolmuse.
allowed_tools: ["Bash", "Read", "Write", "Grep", "Glob"]
---

# /add-ecc-bundle

Use this workflow when working on **add-ecc-bundle** in `lolmuse`.

## Goal

Adds a new ECC (Extensible Command/Capability) bundle to the project, including commands, skills, agent definitions, and configuration files.

## Common Files

- `.claude/commands/*.md`
- `.claude/identity.json`
- `.claude/skills/lolmuse/SKILL.md`
- `.claude/ecc-tools.json`
- `.codex/agents/*.toml`
- `.agents/skills/lolmuse/SKILL.md`

## Suggested Sequence

1. Understand the current state and failure mode before editing.
2. Make the smallest coherent change that satisfies the workflow goal.
3. Run the most relevant verification for touched files.
4. Summarize what changed and what still needs review.

## Typical Commit Signals

- Add or update .claude/commands/*.md files (such as backend-feature-addition.md, add-ecc-bundle.md, feature-development.md, project-initialization.md)
- Add or update .claude/identity.json
- Add or update .claude/skills/lolmuse/SKILL.md
- Add or update .claude/ecc-tools.json
- Add or update .codex/agents/*.toml (docs-researcher.toml, reviewer.toml, explorer.toml)

## Notes

- Treat this as a scaffold, not a hard-coded script.
- Update the command if the workflow evolves materially.