---
name: lolmuse-conventions
description: Development conventions and patterns for lolmuse. Python project with conventional commits.
---

# Lolmuse Conventions

> Generated from [mshkodra/lolmuse](https://github.com/mshkodra/lolmuse) on 2026-03-19

## Overview

This skill teaches Claude the development patterns and conventions used in lolmuse.

## Tech Stack

- **Primary Language**: Python
- **Architecture**: hybrid module organization
- **Test Location**: separate

## When to Use This Skill

Activate this skill when:
- Making changes to this repository
- Adding new features following established patterns
- Writing tests that match project conventions
- Creating commits with proper message format

## Commit Conventions

Follow these commit message conventions based on 61 analyzed commits.

### Commit Style: Conventional Commits

### Prefixes Used

- `feat`

### Message Guidelines

- Average message length: ~59 characters
- Keep first line concise and descriptive
- Use imperative mood ("Add feature" not "Added feature")


*Commit message example*

```text
feat: add lolmuse ECC bundle (.claude/commands/add-backend-api-endpoint.md)
```

*Commit message example*

```text
feat: add lolmuse ECC bundle (.claude/commands/add-ecc-bundle.md)
```

*Commit message example*

```text
feat: add lolmuse ECC bundle (.claude/commands/feature-development.md)
```

*Commit message example*

```text
feat: add lolmuse ECC bundle (.codex/agents/docs-researcher.toml)
```

*Commit message example*

```text
feat: add lolmuse ECC bundle (.codex/agents/reviewer.toml)
```

*Commit message example*

```text
feat: add lolmuse ECC bundle (.codex/agents/explorer.toml)
```

*Commit message example*

```text
feat: add lolmuse ECC bundle (.claude/identity.json)
```

*Commit message example*

```text
feat: add lolmuse ECC bundle (.agents/skills/lolmuse/agents/openai.yaml)
```

## Architecture

### Project Structure: Single Package

This project uses **hybrid** module organization.

### Configuration Files

- `web/package.json`
- `web/tsconfig.json`

### Guidelines

- This project uses a hybrid organization
- Follow existing patterns when adding new code

## Code Style

### Language: Python

### Naming Conventions

| Element | Convention |
|---------|------------|
| Files | camelCase |
| Functions | camelCase |
| Classes | PascalCase |
| Constants | SCREAMING_SNAKE_CASE |

### Import Style: Absolute Imports

### Export Style: Default Exports


*Preferred export style*

```typescript
// Use default exports for main component/function
export default function UserProfile() { ... }
```

## Common Workflows

These workflows were detected from analyzing commit patterns.

### Feature Development

Standard feature implementation workflow

**Frequency**: ~30 times per month

**Steps**:
1. Add feature implementation
2. Add tests for feature
3. Update documentation

**Files typically involved**:
- `**/api/**`

**Example commit sequence**:
```
feat: add lolmuse ECC bundle (.codex/AGENTS.md)
feat: add lolmuse ECC bundle (.codex/agents/explorer.toml)
feat: add lolmuse ECC bundle (.codex/agents/docs-researcher.toml)
```

### Add Ecc Bundle

Adds a new ECC bundle to the lolmuse project, including commands, skills, identity, and agent configurations.

**Frequency**: ~4 times per month

**Steps**:
1. Add or update .claude/commands/add-ecc-bundle.md
2. Add or update .claude/commands/feature-development.md
3. Add or update .claude/commands/backend-feature-addition.md
4. Add or update .claude/commands/project-initialization.md
5. Add or update .claude/identity.json
6. Add or update .claude/ecc-tools.json
7. Add or update .claude/skills/lolmuse/SKILL.md
8. Add or update .agents/skills/lolmuse/SKILL.md
9. Add or update .agents/skills/lolmuse/agents/openai.yaml
10. Add or update .codex/agents/docs-researcher.toml
11. Add or update .codex/agents/reviewer.toml
12. Add or update .codex/agents/explorer.toml

**Files typically involved**:
- `.claude/commands/add-ecc-bundle.md`
- `.claude/commands/feature-development.md`
- `.claude/commands/backend-feature-addition.md`
- `.claude/commands/project-initialization.md`
- `.claude/identity.json`
- `.claude/ecc-tools.json`
- `.claude/skills/lolmuse/SKILL.md`
- `.agents/skills/lolmuse/SKILL.md`
- `.agents/skills/lolmuse/agents/openai.yaml`
- `.codex/agents/docs-researcher.toml`
- `.codex/agents/reviewer.toml`
- `.codex/agents/explorer.toml`

**Example commit sequence**:
```
Add or update .claude/commands/add-ecc-bundle.md
Add or update .claude/commands/feature-development.md
Add or update .claude/commands/backend-feature-addition.md
Add or update .claude/commands/project-initialization.md
Add or update .claude/identity.json
Add or update .claude/ecc-tools.json
Add or update .claude/skills/lolmuse/SKILL.md
Add or update .agents/skills/lolmuse/SKILL.md
Add or update .agents/skills/lolmuse/agents/openai.yaml
Add or update .codex/agents/docs-researcher.toml
Add or update .codex/agents/reviewer.toml
Add or update .codex/agents/explorer.toml
```

### Add Backend Api Endpoint

Documents and implements the addition of a new backend API endpoint via command documentation.

**Frequency**: ~2 times per month

**Steps**:
1. Create or update .claude/commands/add-backend-api-endpoint.md

**Files typically involved**:
- `.claude/commands/add-backend-api-endpoint.md`

**Example commit sequence**:
```
Create or update .claude/commands/add-backend-api-endpoint.md
```

### Add Or Update Agent Config

Adds or updates agent configuration files for docs-researcher, reviewer, and explorer agents.

**Frequency**: ~4 times per month

**Steps**:
1. Add or update .codex/agents/docs-researcher.toml
2. Add or update .codex/agents/reviewer.toml
3. Add or update .codex/agents/explorer.toml

**Files typically involved**:
- `.codex/agents/docs-researcher.toml`
- `.codex/agents/reviewer.toml`
- `.codex/agents/explorer.toml`

**Example commit sequence**:
```
Add or update .codex/agents/docs-researcher.toml
Add or update .codex/agents/reviewer.toml
Add or update .codex/agents/explorer.toml
```


## Best Practices

Based on analysis of the codebase, follow these practices:

### Do

- Use conventional commit format (feat:, fix:, etc.)
- Use camelCase for file names
- Prefer default exports

### Don't

- Don't write vague commit messages
- Don't deviate from established patterns without discussion

---

*This skill was auto-generated by [ECC Tools](https://ecc.tools). Review and customize as needed for your team.*
