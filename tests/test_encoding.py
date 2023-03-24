from gendiff.encode import to_encode, from_json_to_dict, from_yaml_to_dict
from tests.fixtures.example_dict import simple_d, complex_d


def test_to_encode():
    test_list = ['text', True, False, None, 123]
    some_str = str(5)
    assert to_encode(some_str, True) == "'5'"
    assert to_encode(some_str) == "5"
    assert to_encode(test_list) == '["text", true, false, null, 123]'


def test_from_json_to_dict():
    result_plain = list(map(from_json_to_dict, [
        'tests/fixtures/filepath1.json',
        'tests/fixtures/filepath2.json']))
    result_nested = list(map(from_json_to_dict, [
        'tests/fixtures/file1.json',
        'tests/fixtures/file2.json']))
    assert result_plain == simple_d
    assert result_nested == complex_d


def test_from_yaml_to_dict():
    result_plain = list(map(from_yaml_to_dict, [
        'tests/fixtures/filepath1.yml',
        'tests/fixtures/filepath2.yml']))
    result_nested = list(map(from_yaml_to_dict, [
        'tests/fixtures/file1.yaml',
        'tests/fixtures/file2.yaml']))
    assert result_plain == simple_d
    assert result_nested == complex_d
