---
name: wrapup
description: Universal end-of-session audit and wrapup protocol. Call before completing work.
allowed-tools: Bash Read Write
---

# Universal Session Wrap-Up Runbook

When ending a work session or handing off work to another human or agent:

1. **Check Git Status:** Run `git status` to identify all changed files.
2. **Draft Changelog Fragment:** Create `changes/unreleased/<branch>-<issue>.yaml` logging your changes, subsystems touched, and impact.
3. **Draft Session Note:** Create `.agents/sessions/<date>-<topic>.md` summarizing:
   - What was accomplished
   - Any dead ends or abandoned ideas
   - Immediate next action
4. **Update Tasks:** Mark closed tasks in `.beads/issues.jsonl` using `bd close <id>`.
5. **Run Verification:** Execute `make lint` and `make check` to ensure zero adapter drift.
