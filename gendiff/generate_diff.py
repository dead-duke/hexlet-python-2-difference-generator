from gendiff.parser import get_data
from gendiff.compare_data import compare_data
from gendiff.formatters.get_formatted_data import get_formatted_data


def generate_diff(first_file, second_file, format='stylish'):
    print(first_file)
    first_file_data = get_data(first_file)
    second_file_data = get_data(second_file)
    compared_data = compare_data(first_file_data, second_file_data)
    formatted_data = get_formatted_data(compared_data, format)
    return formatted_data
