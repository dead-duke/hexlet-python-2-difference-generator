from gendiff.generate_diff import generate_diff


def test_generate_diff_flat():
    with open('./tests/fixtures/flat_expected_result.txt') as f:
        flat_stylish_result = f.read()
    first_file = './tests/fixtures/file1.json'
    second_file = './tests/fixtures/file2.json'
    flat_json_difference = generate_diff(first_file, second_file)
    assert flat_json_difference == flat_stylish_result
    first_file = './tests/fixtures/file1.yml'
    second_file = './tests/fixtures/file2.yaml'
    flat_yml_difference = generate_diff(first_file, second_file)
    assert flat_yml_difference == flat_stylish_result


def test_generate_diff_nested():
    with open('./tests/fixtures/nested_expected_result.txt') as f:
        nested_stylish_result = f.read()
    first_file = './tests/fixtures/file3.json'
    second_file = './tests/fixtures/file4.json'
    flat_json_difference = generate_diff(first_file, second_file)
    assert flat_json_difference == nested_stylish_result
    first_file = './tests/fixtures/file3.yml'
    second_file = './tests/fixtures/file4.yaml'
    flat_yml_difference = generate_diff(first_file, second_file)
    assert flat_yml_difference == nested_stylish_result
