# AGENTS.md: Universal Repository Instructions

Welcome to the repository. This project is maintained by human engineers and AI coding assistants.
Follow these operational guidelines strictly.

## Repository Map
- `src/`           Core application and pipeline code. Pure business logic in `src/core/`.
- `config/`        Central parameter store (`params.yaml`). All tunable numbers live here.
- `semantic/`      Metric and entity contracts. LLMs query metrics here, never raw SQL.
- `knowledge/`     Curated domain knowledge (OKF v0.2). Read `knowledge/index.md` first.
- `docs/decisions/` Architectural Decision Records (MADR 4.0). Accepted records are immutable.
- `changes/`       Changelog fragments. Every PR must add a fragment in `changes/unreleased/`.
- `.agents/skills/` On-demand procedural runbooks (wrapup, write-adr, add-metric).

## Developer Commands
- Setup:     `make setup`         (Installs dependencies, pre-commit, and git hooks)
- Test:      `make test`          (Runs unit tests, property tests, and markdown doc-tests)
- Lint:      `make lint`          (Runs ruff, mypy, semgrep, and frontmatter linters)
- Generate:  `make generate`      (Compiles tool adapters, indexes, and reference docs)
- Tasks:     `bd ready`           (Lists unblocked tasks from the git-native task graph)

## Non-Negotiable System Invariants
1. **INV-01 (Zero Hardcoded Config):** Never hardcode magic numbers, business rates, or thresholds in source code. All parameters must be declared in `config/params.yaml` and validated via Pydantic.
2. **INV-02 (ADR Immutability):** Never edit or delete accepted ADRs in `docs/decisions/`. If a decision changes, create a new ADR that supersedes the previous one.
3. **INV-03 (Purity):** Modules inside `src/core/` must never import network or IO libraries (`requests`, `httpx`).
4. **INV-04 (Branch Isolation):** Agents never push to `main`. All work must be staged on a feature branch.
5. **INV-05 (Generated Files):** Never manually edit files under `_generated/` or files marked `GENERATED`. Edit the source and run `make generate`.

## Ending a Session
Always execute the `/wrapup` skill before concluding. It creates your changelog fragment, writes your session handoff note, and updates task statuses.
