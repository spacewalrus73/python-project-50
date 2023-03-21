install:
	poetry install


build:
	poetry build


publish:
	poetry publish --dry-run


package-install:
	python3 -m pip install --user dist/*.whl


package-reinstall:
	python3 -m pip install --user dist/*.whl --force-reinstall


lint:
	poetry run flake8 gendiff
	poetry run flake8 tests


test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml


test:
	poetry run pytest