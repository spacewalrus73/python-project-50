from gendiff.formatters import format
from gendiff.converter import get_content


def generate_diff(path1: str, path2: str, output_style='stylish') -> str:
    """
    The function makes internal view between two files and
    outputs them in the desired display format.
    """
    parsed_first_file = get_content(path1)
    parsed_second_file = get_content(path2)
    diff = build_diff_tree(parsed_first_file, parsed_second_file)

    return format(diff, output_style)


def build_diff_tree(item1: dict, item2: dict) -> list:

    diff = []
    all_keys = sorted(set(item1) | set(item2), key=str)

    for key in all_keys:

        if key not in item1:
            diff.append({'name': key,
                         'value': item2[key],
                         'status': 'added'})
        elif key not in item2:
            diff.append({'name': key,
                         'value': item1[key],
                         'status': 'deleted'})
        elif item1[key] == item2[key]:
            diff.append({'name': key,
                         'value': item1[key],
                         'status': 'unchanged'})
        elif isinstance(item1[key], dict) and isinstance(item2[key], dict):
            diff.append({'name': key,
                         'children': build_diff_tree(item1[key], item2[key]),
                         'status': 'nested_changes'})
        else:
            diff.append({'name': key,
                         'old_value': item1[key],
                         'new_value': item2[key],
                         'status': 'plain_changes'})

    return diff
