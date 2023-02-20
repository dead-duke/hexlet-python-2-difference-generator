from gendiff.generate_diff import generate_diff
from tests.fixtures.results import flat_json_result


def test_generate_diff():
    first_file = './tests/fixtures/file1.json'
    second_file = './tests/fixtures/file2.json'
    difference = generate_diff(first_file, second_file)
    assert difference == flat_json_result
