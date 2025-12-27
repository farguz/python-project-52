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

message-make:
	uv run django-admin makemessages -l ru

message-compile:
	uv run django-admin compilemessages

collect-static:
	uv run manage.py collectstatic

lint:
	uv run ruff check

lint-with-fix:
	uv run ruff check --fix

test:
	uv run manage.py test

test-pytest:
	uv run pytest

test-pytest-coverage:
	uv run pytest --cov=gendiff --cov-report xml

check: test lint