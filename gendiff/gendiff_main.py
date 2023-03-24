from gendiff.formatters.format_stylish import stylish
from gendiff.formatters.format_plain import plain


def generate_diff(file1: dict, file2: dict, frmt='stylish') -> str:
    """
    The function makes internal view between two files and
    outputs them in the desired display format.
    """
    diff = to_form_diff(file1, file2, to_find_diff(file1, file2))
    if frmt == 'stylish':
        return stylish(diff)
    else:
        return plain(diff)


def to_find_diff(item_1: dict, item_2: dict) -> list:
    """The function distributes keys to collections, thus finding the
    differences between the files. Returns list of sets."""

    # Find remoted keys that exist in the first dict, but not in the second
    deleted = set.difference(set(item_1), set(item_2))
    # Find added keys that exist in the second dict, but not in the first
    added = set.difference(set(item_2), set(item_1))
    # Find intersect keys that exist in both files and fill the empty sets
    changed = set()
    unchanged = set()

    for key in set.intersection(set(item_1), set(item_2)):
        if item_1[key] == item_2[key]:
            unchanged.add(key)
        else:
            changed.add(key)
    return [deleted, added, changed, unchanged]


def to_form_diff(item1: dict, item2: dict, sets: list) -> dict:
    """
    The function generates an internal diff view using a loop
    that populates the dictionary and also sorts the keys.
    """
    # Assign empty dict to be filled by cycle that sort keys
    diff = {}
    deleted, added, changed, unchanged = sets
    for key in sorted(set(item1) | set(item2), key=str):

        if key in deleted:
            diff[key] = ('-', item1[key])
        elif key in added:
            diff[key] = ('+', item2[key])
        elif key in unchanged:
            diff[key] = (' ', item1[key])
        elif is_dicts(item1[key], item2[key]):
            diff[key] = to_form_diff(item1[key], item2[key],
                                     to_find_diff(item1[key], item2[key]))
        else:
            diff[key] = ('-', item1[key], '+', item2[key])
    return diff


def is_dicts(item_1, item_2) -> bool:
    """Predicate function to check for item's type.
    Returns 'True' if both of items are dicts."""
    return all(list(map(lambda x: isinstance(x, dict), [item_1, item_2])))


__all__ = ('generate_diff',
           'is_dicts',
           'to_find_diff',
           'to_form_diff')
