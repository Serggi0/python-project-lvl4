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
	poetry run flake8 task_manager tests labels statuses tasks users

test:
	poetry run coverage run manage.py test

check:
	poetry check


.PHONY: install lint test translate compiletranslate check build