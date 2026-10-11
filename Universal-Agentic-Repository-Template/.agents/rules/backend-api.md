---
description: Scoped engineering rules for API endpoints and data transport.
globs: ["src/api/**/*.py", "src/api/**/*.ts"]
always: false
---
- All request/response schemas must be declared as Pydantic models.
- Never return raw database records directly to HTTP clients.
- Every API endpoint must have an associated integration test with expected status codes.
- Do not add business logic to route handlers; delegate to `src.core`.
