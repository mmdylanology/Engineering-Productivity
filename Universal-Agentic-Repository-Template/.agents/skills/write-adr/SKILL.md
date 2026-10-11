---
name: write-adr
description: Authors an immutable Architecture Decision Record (MADR 4.0 format).
allowed-tools: Read Write
---

# Write Architecture Decision Record (ADR)

1. Review existing decisions in `docs/decisions/index.md`.
2. Create a new file `docs/decisions/<date>-<short-slug>.md` with `status: proposed`.
3. Include:
   - Context and Problem Statement
   - Considered Options
   - Decision Outcome & Rationale
   - Confirmation: Exact test or linter path that will enforce compliance
4. Never modify existing accepted ADRs; if changing a decision, set `supersedes: ADR-XXXX`.
