from gendiff.generate_diff import generate_diff
import json


def test_generate_diff_flat():
    with open('./tests/fixtures/expected_results/stylish_flat.txt') as f:
        flat_stylish_result = f.read()
    first_file = './tests/fixtures/flat1.json'
    second_file = './tests/fixtures/flat2.json'
    flat_json_difference = generate_diff(first_file, second_file)
    assert flat_json_difference == flat_stylish_result
    first_file = './tests/fixtures/flat1.yml'
    second_file = './tests/fixtures/flat2.yaml'
    flat_yml_difference = generate_diff(first_file, second_file)
    assert flat_yml_difference == flat_stylish_result


def test_generate_diff_nested():
    with open('./tests/fixtures/expected_results/stylish_nested.txt') as f:
        nested_result = f.read()
    first_file = './tests/fixtures/nested1.json'
    second_file = './tests/fixtures/nested2.json'
    stylish_nested_difference = generate_diff(first_file, second_file)
    assert stylish_nested_difference == nested_result
    first_file = './tests/fixtures/nested1.yml'
    second_file = './tests/fixtures/nested2.yaml'
    stylish_nested_difference = generate_diff(first_file, second_file)
    assert stylish_nested_difference == nested_result

    with open('./tests/fixtures/expected_results/json_nested.json') as f:
        nested_result = json.dumps(json.load(f), indent=4)
    first_file = './tests/fixtures/nested1.json'
    second_file = './tests/fixtures/nested2.json'
    json_nested_difference = generate_diff(first_file, second_file, 'json')
    assert json_nested_difference == nested_result
    first_file = './tests/fixtures/nested1.yml'
    second_file = './tests/fixtures/nested2.yaml'
    json_nested_difference = generate_diff(first_file, second_file, 'json')
    assert json_nested_difference == nested_result

    with open('./tests/fixtures/expected_results/plain_nested.txt') as f:
        nested_result = f.read()
    first_file = './tests/fixtures/nested1.json'
    second_file = './tests/fixtures/nested2.json'
    flat_json_difference = generate_diff(first_file, second_file, 'plain')
    assert flat_json_difference == nested_result
    first_file = './tests/fixtures/nested1.yml'
    second_file = './tests/fixtures/nested2.yaml'
    flat_yml_difference = generate_diff(first_file, second_file, 'plain')
    assert flat_yml_difference == nested_result
