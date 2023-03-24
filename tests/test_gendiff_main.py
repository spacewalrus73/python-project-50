import os
from gendiff.gendiff_main import generate_diff, is_dicts
from gendiff.gendiff_main import to_form_diff, to_find_diff
from tests.fixtures.example_dict import simple_d, complex_d
from tests.fixtures.example_diff import ex_diff


def to_read_data(path):
    with open(os.path.abspath(path), 'r') as file:
        data = file.read()
        return data


def test_to_find_diff():
    expected_plain = [{'follow', 'proxy'}, {'verbose'}, {'timeout'}, {'host'}]
    expect_nest_1lvl = [{'group2'}, {'group3'}, {'group1', 'common'}, set()]
    expect_nest_2lvl = [{'setting2'}, {'setting5', 'setting4', 'follow'},
                        {'setting6', 'setting3'}, {'setting1'}]
    expect_nest_3lvl = [set(), {'ops'}, {'doge'}, {'key'}]
    expect_nest_4lvl = [set(), set(), {'wow'}, set()]

    assert expected_plain == to_find_diff(simple_d[0], simple_d[1])
    assert expect_nest_1lvl == to_find_diff(complex_d[0], complex_d[1])
    assert expect_nest_2lvl == to_find_diff(complex_d[0]['common'],
                                            complex_d[1]['common'])
    assert expect_nest_3lvl == to_find_diff(complex_d[0]['common']['setting6'],
                                            complex_d[1]['common']['setting6'])
    assert expect_nest_4lvl == to_find_diff(
        complex_d[0]['common']['setting6']['doge'],
        complex_d[1]['common']['setting6']['doge'])


def test_to_form_diff():
    expected_result_plain = {'follow': ('-', False),
                             'host': (' ', 'hexlet.io'),
                             'proxy': ('-', '123.234.53.22'),
                             'timeout': ('-', 50, '+', 20),
                             'verbose': ('+', True)}

    keys_p = [{'follow', 'proxy'}, {'verbose'}, {'timeout'}, {'host'}]
    keys_n = [{'group2'}, {'group3'}, {'group1', 'common'}, set()]

    assert expected_result_plain == to_form_diff(simple_d[0],
                                                 simple_d[1],
                                                 keys_p)
    assert ex_diff == to_form_diff(complex_d[0], complex_d[1], keys_n)


def test_is_dicts():
    test_lst = [{}, ['1'], {'k': 'v'}, {}, [], None]

    assert is_dicts(test_lst[0], test_lst[1]) is False
    assert is_dicts(test_lst[2], test_lst[3]) is True
    assert is_dicts(test_lst[4], test_lst[5]) is False


def test_generate_diff():
    plain_stylish = to_read_data('tests/fixtures/plain_stylish.txt')
    plain_plain = to_read_data('tests/fixtures/plain_plain.txt')
    nested_stylish = to_read_data('tests/fixtures/nest_stylish.txt')
    nested_plain = to_read_data('tests/fixtures/nest_plain.txt')
    json_plain = to_read_data('tests/fixtures/expected_json.txt')

    assert plain_stylish == generate_diff(simple_d[0],
                                          simple_d[1],
                                          frmt='stylish')
    assert plain_plain == generate_diff(simple_d[0],
                                        simple_d[1],
                                        frmt='plain')
    assert nested_stylish == generate_diff(complex_d[0],
                                           complex_d[1],
                                           frmt='stylish')
    assert nested_plain == generate_diff(complex_d[0],
                                         complex_d[1],
                                         frmt='plain')
    assert json_plain == generate_diff(simple_d[0],
                                       simple_d[1],
                                       frmt='json')
