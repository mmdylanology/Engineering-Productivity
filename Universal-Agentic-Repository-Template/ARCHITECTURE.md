# Architecture Specification & Operating Principles

This document defines the architectural mechanics and invariant enforcement rules of the Universal Agentic Repository Template.

## 1. Context Hierarchy & Progressive Disclosure

Every LLM coding session pays for context tokens. Pushing long documents into system prompts degrades instruction following. This template enforces **Three-Tier Progressive Disclosure**:

```
+--------------------------------------------------------------------------+
| TIER 1: ROOT INSTRUCTIONS (Always Loaded, < 150 lines)                   |
| Location: AGENTS.md                                                      |
| Content: Mission, directory map, setup commands, core invariants,        |
|          and pointer to wrap-up. Nothing task-specific.                  |
+--------------------------------------------------------------------------+
                                     |
                                     v (Loaded when touching matched paths)
+--------------------------------------------------------------------------+
| TIER 2: SCOPED CONDITIONAL RULES                                         |
| Location: .agents/rules/*.md (rendered to .cursor/rules/*.mdc)           |
| Content: Path-specific rules (e.g. backend API standards, data schemas). |
+--------------------------------------------------------------------------+
                                     |
                                     v (Disclosed on demand by task description)
+--------------------------------------------------------------------------+
| TIER 3: ON-DEMAND AGENT SKILLS                                           |
| Location: .agents/skills/<skill>/SKILL.md (agentskills.io open spec)     |
| Content: Step-by-step executable runbooks (wrapup, write-adr, add-metric)|
+--------------------------------------------------------------------------+
```

## 2. Invariant Enforcement: Defense in Depth

Prose rules are advisory; LLMs frequently violate them. Invariants in this template are enforced at the earliest mechanical layer:

| Level | Layer | Tool | Enforcement Action |
| :--- | :--- | :--- | :--- |
| **L0** | Prompt Instructions | `AGENTS.md` | Advisory context to the LLM |
| **L1** | Scoped Rules | `.agents/rules/*.md` | Targeted instructions based on file paths |
| **L2** | Local Hooks | `.claude/settings.json`, `tools/guards/` | Intercepts tool calls; exits code 2 to **block execution** |
| **L3** | Pre-Commit | `pre-commit`, `semgrep`, `ruff` | Blocks `git commit` on invariant violations |
| **L4** | Continuous Integration | GitHub Actions / GitLab CI | Blocks merge on doc drift, schema breaks, or missing fragments |
| **L5** | Runtime Attestation | Python Attesters (`tools/attesters/`) | Deterministically verifies run receipts before serving outputs |

## 3. The Epistemic Triad of Memory

Memory is split into three isolated categories to prevent context decay:

1. **Episodic Memory (`.agents/sessions/`, PR bodies):**
   - *What happened:* Work logs, dead ends, debug transcripts.
   - *Lifespan:* 30–90 days; compacted periodically into monthly digests.
2. **Semantic Memory (`knowledge/`, `semantic/`, `docs/decisions/`):**
   - *What is true:* Verified business facts, domain terms, metric formulas, accepted ADRs.
   - *Lifespan:* Permanent; updated via pull request with trust tiers (`status: draft` vs `status: stable`).
3. **Procedural Memory (`.agents/skills/`, `docs/runbooks/`):**
   - *How to do things:* Executable runbooks, release procedures, session wrap-up protocols.
   - *Lifespan:* Version-controlled alongside source code.
