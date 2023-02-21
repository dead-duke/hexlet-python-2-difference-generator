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
	poetry run pytest -svv

test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml tests/

help:
	poetry run gendiff -h

flat-stylish-run:
	poetry run gendiff ./tests/fixtures/flat1.json ./tests/fixtures/flat2.json

nested-stylish-run:
	poetry run gendiff ./tests/fixtures/nested1.json ./tests/fixtures/nested2.json

nested-plain-run:
	poetry run gendiff -f plain ./tests/fixtures/nested1.json ./tests/fixtures/nested2.json

nested-json-run:
	poetry run gendiff -f json ./tests/fixtures/nested1.json ./tests/fixtures/nested2.json