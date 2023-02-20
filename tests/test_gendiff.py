from gendiff.generate_diff import generate_diff
from tests.fixtures.expected_results import flat_stylish_result


def test_generate_diff():
    first_file = './tests/fixtures/file1.json'
    second_file = './tests/fixtures/file2.json'
    flat_json_difference = generate_diff(first_file, second_file)
    assert flat_json_difference == flat_stylish_result
    flat_yml_difference = generate_diff(first_file, second_file)
    assert flat_yml_difference == flat_stylish_result
