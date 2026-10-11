---
name: add-metric
description: Defines a new semantic metric contract preventing LLM join hallucination.
allowed-tools: Read Write
---

# Add Semantic Metric Contract

1. Create `semantic/metrics/<metric_name>.yaml`.
2. Define:
   - `name`: unique snake_case identifier
   - `label`: human-readable title
   - `type`: simple or derived
   - `measure`: underlying numeric column
   - `dimensions`: allowed group-by fields
   - `additivity`: additive, semi_additive_over_time, or non_additive
   - `description`: clear business definition
3. Add a test case in `semantic/tests/golden_queries.yaml`.
