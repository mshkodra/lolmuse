---
name: project-initialization
description: Workflow command scaffold for project-initialization in lolmuse.
allowed_tools: ["Bash", "Read", "Write", "Grep", "Glob"]
---

# /project-initialization

Use this workflow when working on **project-initialization** in `lolmuse`.

## Goal

Initializes a new project or major subproject, setting up core configuration, dependencies, and scaffolding for backend or frontend.

## Common Files

- `.gitignore`
- `README.md`
- `backend/alembic.ini`
- `backend/alembic/*`
- `backend/app/*`
- `backend/requirements.txt`

## Suggested Sequence

1. Understand the current state and failure mode before editing.
2. Make the smallest coherent change that satisfies the workflow goal.
3. Run the most relevant verification for touched files.
4. Summarize what changed and what still needs review.

## Typical Commit Signals

- Create or update .gitignore and README.md
- For backend: add backend/alembic, backend/app, backend/requirements.txt, backend/app/config.py, backend/app/database.py, backend/app/main.py
- For frontend: add web/README.md, web/app/*, web/package.json, web/tsconfig.json, web/next.config.ts, etc.

## Notes

- Treat this as a scaffold, not a hard-coded script.
- Update the command if the workflow evolves materially.