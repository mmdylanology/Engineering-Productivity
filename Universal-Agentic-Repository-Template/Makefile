.PHONY: setup test lint generate check wrapup help

help:
	@echo "Available commands:"
	@echo "  make graph     - Generate interactive visual knowledge graph (Cytoscape)"
	@echo "  make setup     - Install dependencies, pre-commit hooks, and tools"
	@echo "  make test      - Run all unit tests and Markdown doc-tests"
	@echo "  make lint      - Run linters (ruff, semgrep, mypy, frontmatter)"
	@echo "  make generate  - Compile adapters, ADR indexes, and reference docs"
	@echo "  make check     - Verify that all generated files match source truth"
	@echo "  make wrapup    - Run session wrap-up protocol"

setup:
	pip install -e .
	pre-commit install

test:
	pytest tests/ --markdown-docs

lint:
	ruff check .
	semgrep --config .semgrep/ --error
	python tools/lint_frontmatter.py

generate:
	python tools/agentsync.py
	python tools/build_indexes.py

check:
	python tools/agentsync.py --check
	git diff --exit-code

wrapup:
	python tools/wrapup.py

graph:
	python tools/viz/build_graph.py . docs/graph.html
