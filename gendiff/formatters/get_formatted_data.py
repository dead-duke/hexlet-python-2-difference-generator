from gendiff.formatters.stylish import get_stylish_format


def get_formatted_data(data, data_format):
    print(data_format)
    if data_format == 'stylish':
        return get_stylish_format(data)
