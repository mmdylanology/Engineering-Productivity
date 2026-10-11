---
status: accepted
date: 2026-10-11
decision-makers: [human:lead-architect]
---

# 0000: Use Markdown Architectural Decision Records (MADR 4.0)

## Context and Problem Statement
We need an immutable, reviewable format to document architectural choices before code is committed.

## Considered Options
- Informal Wiki pages
- MADR 4.0 in Git

## Decision Outcome
Chosen: MADR 4.0 in Git, because decisions are reviewed via Pull Request and versioned with code.

### Confirmation
Enforced by pre-commit hook `tools/guards/protect_paths.py` (INV-02).
