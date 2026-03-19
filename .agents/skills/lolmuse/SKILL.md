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

Follow these commit message conventions based on 28 analyzed commits.

### Commit Style: Conventional Commits

### Prefixes Used

- `feat`

### Message Guidelines

- Average message length: ~55 characters
- Keep first line concise and descriptive
- Use imperative mood ("Add feature" not "Added feature")


*Commit message example*

```text
feat: add lolmuse ECC bundle (.claude/commands/project-initialization.md)
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

Adds a new ECC (Extended Cognitive Component) bundle to the project, including commands, agent configs, skills, and tool definitions.

**Frequency**: ~4 times per month

**Steps**:
1. Add or update .claude/commands/*.md files for new commands.
2. Add or update .codex/agents/*.toml files for agent configurations.
3. Add or update .agents/skills/lolmuse/* for skill definitions.
4. Add or update .claude/skills/lolmuse/SKILL.md for skill documentation.
5. Add or update .claude/ecc-tools.json for tool definitions.
6. Add or update .claude/identity.json for identity configuration.
7. Optionally add/update .claude/homunculus/instincts/inherited/*.yaml for instincts.

**Files typically involved**:
- `.claude/commands/*.md`
- `.codex/agents/*.toml`
- `.agents/skills/lolmuse/*`
- `.claude/skills/lolmuse/SKILL.md`
- `.claude/ecc-tools.json`
- `.claude/identity.json`
- `.claude/homunculus/instincts/inherited/*.yaml`

**Example commit sequence**:
```
Add or update .claude/commands/*.md files for new commands.
Add or update .codex/agents/*.toml files for agent configurations.
Add or update .agents/skills/lolmuse/* for skill definitions.
Add or update .claude/skills/lolmuse/SKILL.md for skill documentation.
Add or update .claude/ecc-tools.json for tool definitions.
Add or update .claude/identity.json for identity configuration.
Optionally add/update .claude/homunculus/instincts/inherited/*.yaml for instincts.
```

### Backend Feature Addition

Adds a new backend API endpoint or feature, including router, main app registration, and dependency updates.

**Frequency**: ~2 times per month

**Steps**:
1. Create or update backend/app/routers/<feature>.py for the new endpoint logic.
2. Update backend/app/routers/__init__.py to include the new router.
3. Update backend/app/main.py to register the router or modify main logic.
4. Update backend/requirements.txt if new dependencies are needed.

**Files typically involved**:
- `backend/app/routers/*.py`
- `backend/app/routers/__init__.py`
- `backend/app/main.py`
- `backend/requirements.txt`

**Example commit sequence**:
```
Create or update backend/app/routers/<feature>.py for the new endpoint logic.
Update backend/app/routers/__init__.py to include the new router.
Update backend/app/main.py to register the router or modify main logic.
Update backend/requirements.txt if new dependencies are needed.
```

### Project Initialization

Initializes a new project or major subproject (backend or frontend), setting up config, dependencies, and boilerplate.

**Frequency**: ~2 times per month

**Steps**:
1. Add .gitignore and README.md.
2. Add backend or frontend (web) configuration and boilerplate files.
3. Add package/dependency management files (e.g., requirements.txt, package.json, pnpm-lock.yaml).
4. Add initial source code and config files (e.g., backend/app/main.py, web/app/page.tsx).

**Files typically involved**:
- `.gitignore`
- `README.md`
- `backend/**`
- `web/**`

**Example commit sequence**:
```
Add .gitignore and README.md.
Add backend or frontend (web) configuration and boilerplate files.
Add package/dependency management files (e.g., requirements.txt, package.json, pnpm-lock.yaml).
Add initial source code and config files (e.g., backend/app/main.py, web/app/page.tsx).
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
