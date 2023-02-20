import json
import yaml


def parser(file):
    with open(file) as f:
        file_extension = file.split('.')[-1]
        if file_extension == 'json':
            return json.load(f)
        if file_extension == 'yml' or file_extension == 'yaml':
            return yaml.safe_load(f)
