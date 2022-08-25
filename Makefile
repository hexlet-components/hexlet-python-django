install:
	poetry install

test:
	poetry run pytest

lint:
	poetry run flake8

check: test lint

run:
	poetry run python manage.py runserver

prod:
	env DJANGO_SETTINGS_MODULE=hello_django.settings \
	poetry run gunicorn hello_django.wsgi
