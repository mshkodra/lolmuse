---
name: add-ecc-bundle
description: Workflow command scaffold for add-ecc-bundle in lolmuse.
allowed_tools: ["Bash", "Read", "Write", "Grep", "Glob"]
---

# /add-ecc-bundle

Use this workflow when working on **add-ecc-bundle** in `lolmuse`.

## Goal

Adds a new ECC (Extensible Command/Capability) bundle to the project, including commands, agent configurations, skills, and related metadata.

## Common Files

- `.claude/commands/*.md`
- `.codex/agents/*.toml`
- `.claude/identity.json`
- `.claude/ecc-tools.json`
- `.agents/skills/lolmuse/SKILL.md`
- `.agents/skills/lolmuse/agents/openai.yaml`

## Suggested Sequence

1. Understand the current state and failure mode before editing.
2. Make the smallest coherent change that satisfies the workflow goal.
3. Run the most relevant verification for touched files.
4. Summarize what changed and what still needs review.

## Typical Commit Signals

- Add or update files in .claude/commands/ (e.g., backend-feature-addition.md, add-ecc-bundle.md, feature-development.md, project-initialization.md)
- Add or update agent configuration files in .codex/agents/ (e.g., docs-researcher.toml, reviewer.toml, explorer.toml)
- Add or update identity and tool metadata in .claude/ (e.g., identity.json, ecc-tools.json)
- Add or update skill definitions in .agents/skills/lolmuse/ and .claude/skills/lolmuse/ (e.g., SKILL.md, agents/openai.yaml)
- Optionally add or update instincts or config files (e.g., .claude/homunculus/instincts/inherited/lolmuse-instincts.yaml, .codex/AGENTS.md, .codex/config.toml)

## Notes

- Treat this as a scaffold, not a hard-coded script.
- Update the command if the workflow evolves materially.