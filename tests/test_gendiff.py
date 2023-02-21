import pytest
from gendiff import generate_diff


def get_test_cases():
    input_formats = ('json', 'yml')
    output_formats = ('stylish', 'plain', 'json')
    test_cases = []
    for input_format in input_formats:
        first_file = f'./tests/fixtures/test_file1.{input_format}'
        second_file = f'./tests/fixtures/test_file2.{input_format}'
        for output_format in output_formats:
            output = f'./tests/fixtures/expected_results/{output_format}.txt'
            with open(output) as f:
                result = f.read()
            test_case = (first_file, second_file, output_format, result)
            test_cases.append(test_case)
    return test_cases


@pytest.mark.parametrize(
    "first_file, second_file, format_name, output",
    get_test_cases()
)
def test_generate_diff(first_file, second_file, format_name, output):
    assert generate_diff(first_file, second_file, format_name) == output
