import os
from gendiff.gendiff import generate_diff

file_one = os.path.abspath('tests/fixtures/filepath1.json')
file_two = os.path.abspath('tests/fixtures/filepath2.json')


def test_first_try():
    with open(os.path.abspath('tests/fixtures/expected_result.txt'), 'r') as file:
        expected_res = file.read()

    assert generate_diff(file_one, file_two) == expected_res
