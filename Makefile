install:
	poetry install
	poetry build
	python3 -m pip install --user dist/*.whl

uninstall:
	python3 -m pip uninstall hexlet-code

install-dep:
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

test:
	poetry run pytest -s

test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml tests/

help:
	poetry run gendiff -h

json-run:
	poetry run gendiff ./tests/fixtures/file1.json ./tests/fixtures/file2.json

yml-run:
	poetry run gendiff ./tests/fixtures/file1.yml ./tests/fixtures/file2.yml