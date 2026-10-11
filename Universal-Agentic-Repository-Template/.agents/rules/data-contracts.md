---
description: Scoped engineering rules for semantic metric contracts and pipeline data.
globs: ["semantic/**/*.yaml", "src/pipeline/**/*.py"]
always: false
---
- Every metric must declare an explicit `additivity` (additive, semi_additive_over_time, non_additive).
- Every entity join must be anchored on declared primary and foreign keys.
- Never write ad-hoc raw SQL inside application endpoints; route all metrics through semantic contracts.
