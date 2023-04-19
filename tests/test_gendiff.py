import pytest
from gendiff.generate_diff import generate_diff


data = [('tests/fixtures/example_json/file1_nested.json',
         'tests/fixtures/example_json/file2_nested.json',
         'tests/fixtures/expected_results/nested_stylish.txt',
         'stylish'),
        ('tests/fixtures/example_yml/file1_flat.yml',
         'tests/fixtures/example_yml/file2_flat.yml',
         'tests/fixtures/expected_results/plain_plain.txt',
         'plain'),
        ('tests/fixtures/example_yml/nested.yaml',
         'tests/fixtures/example_json/file2_nested.json',
         'tests/fixtures/expected_results/nested_json.txt',
         'json'),
        ('tests/fixtures/example_json/file1_nested.json',
         'tests/fixtures/example_json/file2_nested.json',
         'tests/fixtures/expected_results/nested_plain.txt',
         'plain')]


@pytest.mark.parametrize("file1, file2, expected_result, style", data)
def test_generate_diff(file1, file2, expected_result, style):
    with open(expected_result, 'r') as f:
        assert f.read() == generate_diff(file1, file2, style)
