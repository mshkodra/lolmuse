---
name: add-backend-api-endpoint
description: Workflow command scaffold for add-backend-api-endpoint in lolmuse.
allowed_tools: ["Bash", "Read", "Write", "Grep", "Glob"]
---

# /add-backend-api-endpoint

Use this workflow when working on **add-backend-api-endpoint** in `lolmuse`.

## Goal

Adds a new API endpoint to the backend, including implementation, router registration, and dependency updates.

## Common Files

- `backend/app/routers/*.py`
- `backend/app/routers/__init__.py`
- `backend/app/main.py`
- `backend/requirements.txt`

## Suggested Sequence

1. Understand the current state and failure mode before editing.
2. Make the smallest coherent change that satisfies the workflow goal.
3. Run the most relevant verification for touched files.
4. Summarize what changed and what still needs review.

## Typical Commit Signals

- Create or update the endpoint implementation in backend/app/routers/*.py
- Update backend/app/routers/__init__.py to register the new router
- Update backend/app/main.py to ensure the new route is included
- Update backend/requirements.txt if new dependencies are needed

## Notes

- Treat this as a scaffold, not a hard-coded script.
- Update the command if the workflow evolves materially.