install:
	poetry install

runserver:
	poetry run python manage.py runserver

lint:
	poetry run flake8 task_manager tests labels statuses tasks users


translate:
	poetry run python manage.py makemessages -l ru

compiletranslate:
	poetry run python manage.py compilemessages


test:
	poetry run pytest -v --cov=task_manager tests/ --cov-report xml

.PHONY: install lint test translate compiletranslate