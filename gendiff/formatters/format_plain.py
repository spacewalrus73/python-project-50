from gendiff.decoder import to_encode


def plain(diff, path_string='') -> str:

    lines = []

    for item in diff:
        path = path_string + f'.{item["name"]}'
        tail = ''

        if item["status"] == 'nested_changes':
            lines.append(plain(item["children"], path_string=path))
            continue

        elif item["status"] == 'added':
            tail = 'added with value: ' + stringify_value(item["value"])[0]

        elif item["status"] == 'deleted':
            tail = 'removed'

        elif item['status'] == 'plain_changes':
            values = stringify_value(item["old_value"], item["new_value"])
            tail = 'updated. From ' + values[0] + ' to ' + values[1]
        else:
            continue

        lines.append(f"Property '{path[1:]}' was " + tail)

    return '\n'.join(lines)


def stringify_value(*args) -> list:

    values = []

    for value in args:

        if isinstance(value, str):
            values.append(f"'{value}'")

        elif isinstance(value, dict):
            values.append('[complex value]')

        else:
            values.append(f"{to_encode(value)}")

    return values
