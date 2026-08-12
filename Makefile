install:
	@uv sync

test:
	@uv run pytest

lint:
	@uv run ruff check .

check: install lint test

run:
	uv run python manage.py runserver

prod:
	env DJANGO_SETTINGS_MODULE=hello_django.settings \
	uv run gunicorn hello_django.wsgi

makemigration:
	uv run python manage.py makemigrations

migrate: makemigration
	uv run python manage.py migrate

repl:
	uv run python manage.py shell
