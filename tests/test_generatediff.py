import os
from gendiff.gendiff_main import generate_diff
from gendiff.encode import to_encode, from_json_to_dict, from_yaml_to_dict
from tests.fixtures.pydict_from_nested_json import example_dict


def to_read_result(path):
    with open(os.path.abspath(path), 'r') as file:
        expected_res = file.read()
        return expected_res


def test_plain_json():
    file_content = list(map(from_json_to_dict, [
        'tests/fixtures/filepath1.json',
        'tests/fixtures/filepath2.json']))

    assert file_content == [
        {
            'host': 'hexlet.io',
            'timeout': 50,
            'proxy': '123.234.53.22',
            'follow': False,
        },
        {
            'timeout': 20,
            'verbose': True,
            'host': 'hexlet.io',
        }
    ]

    assert generate_diff(file_content[0], file_content[1]) == \
           to_read_result('tests/fixtures/expected_result_plain.txt')


def test_plain_yaml():
    file_content = list(map(from_yaml_to_dict, [
        'tests/fixtures/filepath1.yml',
        'tests/fixtures/filepath2.yml']))

    assert file_content == [
        {
            'host': 'hexlet.io',
            'timeout': 50,
            'proxy': '123.234.53.22',
            'follow': False,
        },
        {
            'timeout': 20,
            'verbose': True,
            'host': 'hexlet.io',
        }
    ]

    assert generate_diff(file_content[0], file_content[1]) == \
           to_read_result('tests/fixtures/expected_result_plain.txt')


def test_to_encode():
    test_list = ['text', True, False, None, 123]

    assert to_encode(test_list) == '["text", true, false, null, 123]'


def test_nested_json():
    file_content = list(map(from_json_to_dict, ['tests/fixtures/file1.json',
                                                'tests/fixtures/file2.json']))

    assert example_dict == file_content

    assert generate_diff(file_content[0], file_content[1]) == \
           to_read_result('tests/fixtures/expected_result_nested.txt')


def test_nested_yaml():
    file_content = list(map(from_yaml_to_dict, ['tests/fixtures/file1.yaml',
                                                'tests/fixtures/file2.yaml']))

    assert file_content == example_dict

    assert generate_diff(file_content[0], file_content[1]) == \
        to_read_result('tests/fixtures/expected_result_nested.txt')
