import pytest
from gendiff.generate_diff import generate_diff, is_dicts
from tests import test_data


def test_is_dicts():
    test_lst = [{}, ['1'], {'k': 'v'}, {}, [], None]

    assert is_dicts(test_lst[0], test_lst[1]) is False
    assert is_dicts(test_lst[2], test_lst[3]) is True
    assert is_dicts(test_lst[4], test_lst[5]) is False


@pytest.mark.parametrize("file1, file2, expected, style", test_data.data_json)
def test_generate_diff_json(file1, file2, expected, style):
    with open(expected, 'r') as f:
        assert f.read() == generate_diff(file1, file2, style)


@pytest.mark.parametrize("file1, file2, expected, style", test_data.data_yml)
def test_generate_diff_yml(file1, file2, expected, style):
    with open(expected, 'r') as f:
        assert f.read() == generate_diff(file1, file2, style)


@pytest.mark.parametrize("file1, file2, expected, style", test_data.data_mixed)
def test_generate_diff_mixed(file1, file2, expected, style):
    with open(expected, 'r') as f:
        assert f.read() == generate_diff(file1, file2, style)
