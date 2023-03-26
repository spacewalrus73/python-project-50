from gendiff.decoder import to_encode


def plain(diff: dict, path_str='', depth=1) -> str:

    lines = []
    for key, item in diff.items():
        path = path_str + f'.{key}'
        if not isinstance(item, tuple):
            lines.append(plain(item, path_str=path, depth=depth + 1))
        elif item[0] == '+':
            lines.append(
                craft_ad(path, item, flag=isinstance(item[1], dict)))
        elif item[0] == '-' and len(item) != 4:
            lines.append(craft_rm(path))
        elif len(item) == 4:
            lines.append(craft_ch(path, item))
        else:
            continue
    return '\n'.join(lines)


def craft_ch(path, val):
    if isinstance(val[1], dict) and isinstance(val[3], dict):
        return f"Property '{path[1:]}' was updated. " \
               f'From [complex value] to [complex value]'
    elif isinstance(val[1], dict):
        return f"Property '{path[1:]}' was updated. " \
               f'From [complex value] to {to_encode(val[3], True)}'
    elif isinstance(val[3], dict):
        return f"Property '{path[1:]}' was updated. " \
               f'From {to_encode(val[1], True)} to [complex value]'
    else:
        return f"Property '{path[1:]}' was updated. " \
               f"From {to_encode(val[1], True)} to {to_encode(val[3], True)}"


def craft_rm(path: str) -> str:
    return f"Property '{path[1:]}' was removed"


def craft_ad(path: str, val, flag: bool) -> str:
    if not flag:
        return f"Property '{path[1:]}' was added with value: " \
               f"{to_encode(val[1], True)}"
    else:
        return f"Property '{path[1:]}' was added with value: [complex value]"
