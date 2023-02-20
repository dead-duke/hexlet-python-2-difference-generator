import json


def parser(file):
    with open(file) as f:
        return json.load(f)
