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

Follow these commit message conventions based on 39 analyzed commits.

### Commit Style: Conventional Commits

### Prefixes Used

- `feat`

### Message Guidelines

- Average message length: ~57 characters
- Keep first line concise and descriptive
- Use imperative mood ("Add feature" not "Added feature")


*Commit message example*

```text
feat: add lolmuse ECC bundle (.claude/commands/backend-feature-addition.md)
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

**Frequency**: ~29 times per month

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

Adds a new ECC (Extensible Command/Capability) bundle to the project, including commands, skills, agent definitions, and configuration files.

**Frequency**: ~3 times per month

**Steps**:
1. Add or update .claude/commands/*.md files (such as backend-feature-addition.md, add-ecc-bundle.md, feature-development.md, project-initialization.md)
2. Add or update .claude/identity.json
3. Add or update .claude/skills/lolmuse/SKILL.md
4. Add or update .claude/ecc-tools.json
5. Add or update .codex/agents/*.toml (docs-researcher.toml, reviewer.toml, explorer.toml)
6. Add or update .agents/skills/lolmuse/SKILL.md and .agents/skills/lolmuse/agents/openai.yaml
7. Optionally add or update .claude/homunculus/instincts/inherited/*.yaml
8. Optionally add or update .codex/AGENTS.md and .codex/config.toml

**Files typically involved**:
- `.claude/commands/*.md`
- `.claude/identity.json`
- `.claude/skills/lolmuse/SKILL.md`
- `.claude/ecc-tools.json`
- `.codex/agents/*.toml`
- `.agents/skills/lolmuse/SKILL.md`
- `.agents/skills/lolmuse/agents/openai.yaml`
- `.claude/homunculus/instincts/inherited/*.yaml`
- `.codex/AGENTS.md`
- `.codex/config.toml`

**Example commit sequence**:
```
Add or update .claude/commands/*.md files (such as backend-feature-addition.md, add-ecc-bundle.md, feature-development.md, project-initialization.md)
Add or update .claude/identity.json
Add or update .claude/skills/lolmuse/SKILL.md
Add or update .claude/ecc-tools.json
Add or update .codex/agents/*.toml (docs-researcher.toml, reviewer.toml, explorer.toml)
Add or update .agents/skills/lolmuse/SKILL.md and .agents/skills/lolmuse/agents/openai.yaml
Optionally add or update .claude/homunculus/instincts/inherited/*.yaml
Optionally add or update .codex/AGENTS.md and .codex/config.toml
```

### Backend Feature Addition

Implements a new backend API endpoint, including router, main application integration, and dependency updates.

**Frequency**: ~2 times per month

**Steps**:
1. Add or update a new router file in backend/app/routers/*.py
2. Update backend/app/routers/__init__.py to include the new router
3. Update backend/app/main.py to register the new router
4. Update backend/requirements.txt if new dependencies are needed

**Files typically involved**:
- `backend/app/routers/*.py`
- `backend/app/routers/__init__.py`
- `backend/app/main.py`
- `backend/requirements.txt`

**Example commit sequence**:
```
Add or update a new router file in backend/app/routers/*.py
Update backend/app/routers/__init__.py to include the new router
Update backend/app/main.py to register the new router
Update backend/requirements.txt if new dependencies are needed
```

### Project Initialization

Initializes a new project or major subcomponent (backend or frontend), including configuration, setup files, and initial code structure.

**Frequency**: ~2 times per month

**Steps**:
1. Add .gitignore and README.md
2. For backend: add backend/alembic/*, backend/app/*, backend/requirements.txt, backend/alembic.ini
3. For frontend: add web/app/*, web/next.config.ts, web/package.json, web/tsconfig.json, web/eslint.config.mjs, etc.

**Files typically involved**:
- `.gitignore`
- `README.md`
- `backend/alembic.ini`
- `backend/alembic/*`
- `backend/app/*`
- `backend/requirements.txt`
- `web/app/*`
- `web/next.config.ts`
- `web/package.json`
- `web/tsconfig.json`
- `web/eslint.config.mjs`

**Example commit sequence**:
```
Add .gitignore and README.md
For backend: add backend/alembic/*, backend/app/*, backend/requirements.txt, backend/alembic.ini
For frontend: add web/app/*, web/next.config.ts, web/package.json, web/tsconfig.json, web/eslint.config.mjs, etc.
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
