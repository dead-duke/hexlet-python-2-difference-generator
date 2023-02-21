
# Hexlet: "Difference Generator"

[![Actions Status](https://github.com/deus-ex-m/python-project-50/workflows/hexlet-check/badge.svg)](https://github.com/deus-ex-m/python-project-50/actions)
[![Python CI](https://github.com/deus-ex-m/python-project-50/actions/workflows/pyci.yml/badge.svg?branch=main)](https://github.com/deus-ex-m/python-project-50/actions/workflows/pyci.yml)
[![Maintainability](https://api.codeclimate.com/v1/badges/6a9d29688f4ed9d1a02b/maintainability)](https://codeclimate.com/github/deus-ex-m/python-project-50/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/6a9d29688f4ed9d1a02b/test_coverage)](https://codeclimate.com/github/deus-ex-m/python-project-50/test_coverage)


CLI applications to compare two files. The result of the work is a report of differences in files. Work with JSON, YML, YAML files, result formats 'stylish', 'plain', 'json'.

## Requirements

* Python >=3.8.1
* Make

## Installation and launch

* `make install` install
* `make help` information about application
* `gendiff [file1] [file2]` default launch
* `gendiff -f <format> [file1] [file2]` launch with user format

## Work examples

* Flat files, result formatted as 'stylish': https://asciinema.org/a/561540
* Nest files, result formatted as 'stylish': https://asciinema.org/a/561541
* Nest files, result formatted as 'plain': https://asciinema.org/a/561542
* Nest files, result formatted as 'json': https://asciinema.org/a/561543