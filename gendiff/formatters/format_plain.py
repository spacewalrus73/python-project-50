from gendiff.decoder import to_encode


def plain(diff, path_string='') -> str:

    lines = []

    for item in diff:
        path = path_string + f'.{item["name"]}'
        begin_string = f"Property '{path[1:]}' was "
        tail = ''

        if item["status"] == 'nested_changes':
            lines.append(plain(item["children"], path_string=path))

        elif item["status"] == 'added':
            tail = 'added with value: ' + stringify_value(item["value"])[0]
            lines.append(begin_string + tail)

        elif item["status"] == 'deleted':
            tail = 'removed'
            lines.append(begin_string + tail)

        elif item['status'] == 'plain_changes':
            values = stringify_value(item["old_value"], item["new_value"])
            tail = 'updated. From ' + values[0] + ' to ' + values[1]
            lines.append(begin_string + tail)

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
