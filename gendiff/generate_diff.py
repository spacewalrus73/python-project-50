from gendiff.formatters.format_stylish import stylish
from gendiff.formatters.format_plain import plain
from gendiff.formatters.format_json import json
from gendiff.decoder import to_decode


def generate_diff(path1: str, path2: str, frmt='stylish') -> str:
    """
    The function makes internal view between two files and
    outputs them in the desired display format.
    """
    diff = make_internal_view(to_decode(path1), to_decode(path2))
    return select_format(diff, frmt)


def select_format(diff, form):

    if form.lower().strip() == 'stylish':
        return stylish(diff)
    elif form.lower().strip() == 'plain':
        return plain(diff)
    elif form.lower().strip() == 'json':
        return json(diff)
    else:
        return "Incorrect output format! Check the format name."


def make_internal_view(item1: dict, item2: dict) -> list:
    """
    The function sorts the keys and also generates an
    internal representation as {'name': key,
                                'val': value:{}/[]/Any,
                                'status': 'added'/'deleted' etc.}
    """

    diff = []
    all_keys = sorted(set(item1) | set(item2), key=str)

    for key in all_keys:
        if key not in item1:
            diff.append({'name': key, 'val': item2[key], 'status': 'added'})
        elif key not in item2:
            diff.append({'name': key, 'val': item1[key], 'status': 'deleted'})
        elif item1[key] == item2[key]:
            diff.append({'name': key, 'val': item1[key], 'status': 'unchanged'})
        elif is_dicts(item1[key], item2[key]):
            diff.append({'name': key,
                         'val': make_internal_view(item1[key], item2[key]),
                         'status': 'nested_changes'})
        else:
            diff.append({'name': key,
                         'val1': item1[key],
                         'val2': item2[key],
                         'status': 'plain_changes'})

    return diff


def is_dicts(item_1, item_2) -> bool:
    """Predicate function to check for item's type.
    Returns 'True' if both of items are dicts."""
    return all(list(map(lambda x: isinstance(x, dict), [item_1, item_2])))


__all__ = 'generate_diff'
