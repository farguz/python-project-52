install:
	uv sync
	
build:
	./build.sh

render-start:
	gunicorn task_manager.wsgi

lint:
	uv run ruff check

lint-with-fix:
	uv run ruff check --fix

test:
	uv run pytest

test-coverage:
	uv run pytest --cov=gendiff --cov-report xml

check: test lint