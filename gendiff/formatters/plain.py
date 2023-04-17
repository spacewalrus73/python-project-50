import json


def plain(diff, path_string='') -> str:

    lines = []

    for item in diff:
        path = path_string + f'.{item["name"]}'

        if item["status"] == 'nested_changes':
            lines.append(plain(item["children"], path_string=path))
            continue

        elif item["status"] == 'added':
            lines.append(f"Property '{path[1:]}' was added with value: "
                         f'{stringify_value(item["value"])}')

        elif item["status"] == 'deleted':
            lines.append(f"Property '{path[1:]}' was removed")

        elif item['status'] == 'plain_changes':
            lines.append(f"Property '{path[1:]}' was updated. From "
                         f"{stringify_value(item['old_value'])} to "
                         f"{stringify_value(item['new_value'])}")

    return '\n'.join(lines)


def stringify_value(item) -> str:

    if isinstance(item, str):
        return f"'{item}'"
    elif isinstance(item, dict):
        return '[complex value]'
    else:
        return json.JSONEncoder().encode(item)
