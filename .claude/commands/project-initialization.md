---
name: project-initialization
description: Workflow command scaffold for project-initialization in lolmuse.
allowed_tools: ["Bash", "Read", "Write", "Grep", "Glob"]
---

# /project-initialization

Use this workflow when working on **project-initialization** in `lolmuse`.

## Goal

Sets up a new project or major subproject (backend or frontend) with initial configuration, dependencies, and boilerplate files.

## Common Files

- `.gitignore`
- `README.md`
- `backend/requirements.txt`
- `backend/alembic.ini`
- `backend/app/main.py`
- `web/package.json`

## Suggested Sequence

1. Understand the current state and failure mode before editing.
2. Make the smallest coherent change that satisfies the workflow goal.
3. Run the most relevant verification for touched files.
4. Summarize what changed and what still needs review.

## Typical Commit Signals

- Create or update .gitignore and README.md
- Add configuration files (e.g., package.json, requirements.txt, tsconfig.json, alembic.ini)
- Add initial source code structure and boilerplate (e.g., main.py, layout.tsx)
- Add environment or dependency lock/config files (e.g., pnpm-lock.yaml, next-env.d.ts)

## Notes

- Treat this as a scaffold, not a hard-coded script.
- Update the command if the workflow evolves materially.