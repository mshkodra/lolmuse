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

Follow these commit message conventions based on 17 analyzed commits.

### Commit Style: Conventional Commits

### Prefixes Used

- `feat`

### Message Guidelines

- Average message length: ~50 characters
- Keep first line concise and descriptive
- Use imperative mood ("Add feature" not "Added feature")


*Commit message example*

```text
feat: add lolmuse ECC bundle (.claude/commands/project-initialization.md)
```

*Commit message example*

```text
feat: add lolmuse ECC bundle (.claude/homunculus/instincts/inherited/lolmuse-instincts.yaml)
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
feat: add lolmuse ECC bundle (.codex/AGENTS.md)
```

*Commit message example*

```text
feat: add lolmuse ECC bundle (.codex/config.toml)
```

*Commit message example*

```text
feat: add lolmuse ECC bundle (.claude/identity.json)
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

**Frequency**: ~28 times per month

**Steps**:
1. Add feature implementation
2. Add tests for feature
3. Update documentation

**Files typically involved**:
- `web/app/*`
- `web/*`
- `**/api/**`

**Example commit sequence**:
```
feat: init
feat: nextjs setup
feat: backend setup
```

### Add Ecc Bundle

Adds a new ECC (Extensible Cognitive Component) bundle, which includes configuration, agent definitions, skills, and documentation files for the lolmuse system.

**Frequency**: ~4 times per month

**Steps**:
1. Create or update .claude/commands/project-initialization.md
2. Add or update .claude/homunculus/instincts/inherited/*.yaml
3. Add or update .codex/agents/*.toml
4. Add or update .codex/AGENTS.md
5. Add or update .codex/config.toml
6. Add or update .claude/identity.json
7. Add or update .agents/skills/lolmuse/agents/*.yaml
8. Add or update .agents/skills/lolmuse/SKILL.md
9. Add or update .claude/skills/lolmuse/SKILL.md
10. Add or update .claude/ecc-tools.json

**Files typically involved**:
- `.claude/commands/project-initialization.md`
- `.claude/homunculus/instincts/inherited/*.yaml`
- `.codex/agents/*.toml`
- `.codex/AGENTS.md`
- `.codex/config.toml`
- `.claude/identity.json`
- `.agents/skills/lolmuse/agents/*.yaml`
- `.agents/skills/lolmuse/SKILL.md`
- `.claude/skills/lolmuse/SKILL.md`
- `.claude/ecc-tools.json`

**Example commit sequence**:
```
Create or update .claude/commands/project-initialization.md
Add or update .claude/homunculus/instincts/inherited/*.yaml
Add or update .codex/agents/*.toml
Add or update .codex/AGENTS.md
Add or update .codex/config.toml
Add or update .claude/identity.json
Add or update .agents/skills/lolmuse/agents/*.yaml
Add or update .agents/skills/lolmuse/SKILL.md
Add or update .claude/skills/lolmuse/SKILL.md
Add or update .claude/ecc-tools.json
```

### Project Initialization

Initializes a new project or major subproject, setting up core configuration, dependencies, and scaffolding for backend or frontend.

**Frequency**: ~2 times per month

**Steps**:
1. Create or update .gitignore and README.md
2. For backend: add backend/alembic, backend/app, backend/requirements.txt, backend/app/config.py, backend/app/database.py, backend/app/main.py
3. For frontend: add web/README.md, web/app/*, web/package.json, web/tsconfig.json, web/next.config.ts, etc.

**Files typically involved**:
- `.gitignore`
- `README.md`
- `backend/alembic.ini`
- `backend/alembic/*`
- `backend/app/*`
- `backend/requirements.txt`
- `web/README.md`
- `web/app/*`
- `web/package.json`
- `web/tsconfig.json`
- `web/next.config.ts`

**Example commit sequence**:
```
Create or update .gitignore and README.md
For backend: add backend/alembic, backend/app, backend/requirements.txt, backend/app/config.py, backend/app/database.py, backend/app/main.py
For frontend: add web/README.md, web/app/*, web/package.json, web/tsconfig.json, web/next.config.ts, etc.
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
