from gendiff.decoder import to_encode


def plain(diff, path_str='') -> str:

    lines = []

    for item in diff:
        path = path_str + f'.{item["name"]}'
        if item["status"] == 'nested_changes':
            lines.append(plain(item["val"], path))
        elif item["status"] == 'added':
            lines.append(add_str(item["val"],
                                 path,
                                 isinstance(item['val'], dict)))
        elif item["status"] == 'deleted':
            lines.append(del_str(path))
        elif item["status"] == 'plain_changes':
            lines.append(chang_str(path, item["val1"], item["val2"]))

    return '\n'.join(lines)


def add_str(value, path: str, flag: bool):

    if not flag:
        return f"Property '{path[1:]}' was added with value: " \
               f"{to_encode(value, quotes=True)}"
    else:
        return f"Property '{path[1:]}' was added with value: [complex value]"


def del_str(path):
    return f"Property '{path[1:]}' was removed"


def chang_str(path, val1, val2):

    if isinstance(val1, dict) and isinstance(val2, dict):
        return f"Property '{path[1:]}' was updated. " \
               f"From [complex value] to [complex value]"
    elif isinstance(val1, dict):
        return f"Property '{path[1:]}' was updated. " \
               f"From [complex value] to {to_encode(val2, quotes=True)}"
    elif isinstance(val2, dict):
        return f"Property '{path[1:]}' was updated. " \
               f"From {to_encode(val1, quotes=True)} to [complex value]"
    else:
        return f"Property '{path[1:]}' was updated. " \
               f"From {to_encode(val1, quotes=True)} to " \
               f"{to_encode(val2, quotes=True)}"
