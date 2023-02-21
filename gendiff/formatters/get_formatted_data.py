from gendiff.formatters.stylish_formatter import get_stylish_format
from gendiff.formatters.plain_formatter import get_plain_format
from gendiff.formatters.json_formatter import get_json_format


def get_formatted_data(data, format_name):
    if format_name == 'stylish':
        return get_stylish_format(data)
    if format_name == 'plain':
        return get_plain_format(data)
    if format_name == 'json':
        return get_json_format(data)
