.PHONY: install lint format typecheck test check

install:  ## Install everything, exactly as locked
	uv sync --locked

lint:  ## Style and bug checks
	uv run ruff check .
	uv run ruff format --check .

format:  ## Auto-fix style
	uv run ruff check --fix .
	uv run ruff format .

typecheck:  ## Static type checks
	uv run mypy src tests

test:  ## Run the test suite with coverage
	uv run pytest --cov=hybrid_rag --cov-report=term-missing --cov-fail-under=90

check: lint typecheck test  ## Everything CI runs
