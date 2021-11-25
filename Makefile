install:
	poetry install

runserver:
	poetry run python manage.py runserver

translate:
	poetry run python manage.py makemessages -l ru

compiletranslate:
	poetry run python manage.py compilemessages

build:
	poetry build

package-install:
	pip install --user dist/*.whl

lint:
	poetry run flake8 tests
	poetry run flake8 task_manager
	poetry run flake8 labels
	poetry run flake8 statuses
	poetry run flake8 tasks
	poetry run flake8 users

test:
	# poetry run pytest -v --cov=python-project-lvl4 tests/ --cov-report xml
	poetry run coverage run manage.py test

poetry_check:
	poetry check

check:
	make test lint poetry_check


.PHONY: install lint test translate compiletranslate check build