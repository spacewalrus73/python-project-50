import os
from gendiff.gendiff import generate_diff, from_json_to_dict, from_yaml_to_dict

with open(os.path.abspath('tests/fixtures/expected_result.txt'), 'r') as file:
    expected_res = file.read()


def test_plain_json():
    file_content = list(map(from_json_to_dict, [os.path.abspath('tests/fixtures/filepath1.json'),
                                                os.path.abspath('tests/fixtures/filepath2.json')]))
    assert [{'host': 'hexlet.io', 'timeout': 50, 'proxy': '123.234.53.22', 'follow': False},
            {'timeout': 20, 'verbose': True, 'host': 'hexlet.io'}] == file_content

    assert generate_diff(file_content[0], file_content[1]) == expected_res


def test_plain_yaml():
    file_content = list(map(from_yaml_to_dict, [os.path.abspath('tests/fixtures/filepath1.yml'),
                                                os.path.abspath('tests/fixtures/filepath2.yml')]))
    assert [{'host': 'hexlet.io', 'timeout': 50, 'proxy': '123.234.53.22', 'follow': False},
            {'timeout': 20, 'verbose': True, 'host': 'hexlet.io'}] == file_content

    assert generate_diff(file_content[0], file_content[1]) == expected_res
