
# Hexlet: "Difference Generator"

[![Actions Status](https://github.com/dead-duke/hexlet-python-2-difference-generator/actions/workflows/hexlet-check.yml/badge.svg?branch=main)](https://github.com/dead-duke/hexlet-python-2-difference-generator/actions/workflows/hexlet-check.yml)
[![Python CI](https://github.com/dead-duke/hexlet-python-2-difference-generator/actions/workflows/pyci.yml/badge.svg?branch=main)](https://github.com/dead-duke/hexlet-python-2-difference-generator/actions/workflows/pyci.yml)
[![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=dead-duke_hexlet-python-2-difference-generator&metric=sqale_rating)](https://sonarcloud.io/summary/new_code?id=dead-duke_hexlet-python-2-difference-generator)

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

* [Flat files, result formatted as 'stylish'](https://asciinema.org/a/561540)
* [Nest files, result formatted as 'stylish'](https://asciinema.org/a/561541)
* [Nest files, result formatted as 'plain'](https://asciinema.org/a/561542)
* [Nest files, result formatted as 'json'](https://asciinema.org/a/561543)
