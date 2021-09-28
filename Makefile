lint:
	poetry run flake8 task_manager
	poetry run flake8 tests

test:
	poetry run pytest -v --cov=task_manager tests/ --cov-report xml

.PHONY: lint test