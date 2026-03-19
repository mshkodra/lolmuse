---
name: backend-feature-addition
description: Workflow command scaffold for backend-feature-addition in lolmuse.
allowed_tools: ["Bash", "Read", "Write", "Grep", "Glob"]
---

# /backend-feature-addition

Use this workflow when working on **backend-feature-addition** in `lolmuse`.

## Goal

Adds a new backend API endpoint or feature, including router, main app registration, and dependency updates.

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

- Create or update backend/app/routers/<feature>.py for the new endpoint logic.
- Update backend/app/routers/__init__.py to include the new router.
- Update backend/app/main.py to register the router or modify main logic.
- Update backend/requirements.txt if new dependencies are needed.

## Notes

- Treat this as a scaffold, not a hard-coded script.
- Update the command if the workflow evolves materially.