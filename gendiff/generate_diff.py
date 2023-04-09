from gendiff.formatters.format_stylish import stylish
from gendiff.formatters.format_plain import plain
from gendiff.formatters.format_json import json
from gendiff.decoder import to_decode


def generate_diff(path1: str, path2: str, output_style='stylish') -> str:
    """
    The function makes internal view between two files and
    outputs them in the desired display format.
    """
    parsed_first_file = to_decode(path1, path1.split('.')[1])
    parsed_second_file = to_decode(path2, path2.split('.')[1])

    diff = make_internal_view(parsed_first_file, parsed_second_file)

    return execute_format(diff, output_style)


def execute_format(diff, output_style):

    if output_style.lower().strip() == 'stylish':
        return stylish(diff)

    elif output_style.lower().strip() == 'plain':
        return plain(diff)

    elif output_style.lower().strip() == 'json':
        return json(diff)

    else:
        return "Incorrect output format! Check the format name."


def make_internal_view(item1: dict, item2: dict) -> list:
    """
    The function sorts the keys and also generates an
    internal representation as
    {'name': key, 'val': value:Any, 'status': 'added'/'deleted' etc.}
    """

    diff = []
    all_keys = sorted(set(item1) | set(item2), key=str)

    for key in all_keys:

        if key not in item1:
            diff.append({'name': key, 'value': item2[key], 'status': 'added'})

        elif key not in item2:
            diff.append({'name': key, 'value': item1[key], 'status': 'deleted'})

        elif item1[key] == item2[key]:
            diff.append({'name': key,
                         'value': item1[key],
                         'status': 'unchanged'})

        elif isinstance(item1[key], dict) and isinstance(item2[key], dict):
            diff.append({'name': key,
                         'children': make_internal_view(item1[key], item2[key]),
                         'status': 'nested_changes'})

        else:
            diff.append({'name': key,
                         'old_value': item1[key],
                         'new_value': item2[key],
                         'status': 'plain_changes'})

    return diff
