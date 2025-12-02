install:
	uv sync
	
build:
	./build.sh

local-start:
	uv run manage.py runserver

render-start:
	gunicorn task_manager.wsgi

migrations:
	uv run manage.py makemigrations
	uv run manage.py migrate

lint:
	uv run ruff check

lint-with-fix:
	uv run ruff check --fix

test:
	uv run pytest

test-coverage:
	uv run pytest --cov=gendiff --cov-report xml

check: test lint