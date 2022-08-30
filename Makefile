install:
	poetry install

test:
	poetry run pytest

lint:
	poetry run flake8

check: test lint

run:
	poetry run python manage.py runserver

<<<<<<< HEAD
migrations:
	poetry run python manage.py makemigrations

migrate:
	poetry run python manage.py migrate

shell:
	poetry run python manage.py shell
=======
prod:
	env DJANGO_SETTINGS_MODULE=hello_django.settings \
	poetry run gunicorn hello_django.wsgi

makemigration:
	poetry run python manage.py makemigrations

migrate: makemigration
	poetry run python manage.py migrate

repl:
	poetry run python manage.py shell
>>>>>>> 800-models
