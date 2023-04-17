import json
from itertools import chain


def stylish(value, depth: int = 1):

    lines = []
    spacers, post_spacers = create_indents(depth)

    for item in value:

        if item['status'] == 'plain_changes':
            old_value_str = f'{spacers}- {item["name"]}: ' \
                            f'{stringify_value(item["old_value"], depth)}\n'
            new_value_str = f'{spacers}+ {item["name"]}: ' \
                            f'{stringify_value(item["new_value"], depth)}'
            lines.append(old_value_str + new_value_str)

        elif item['status'] == 'nested_changes':
            lines.append(f'{spacers}  {item["name"]}: '
                         f'{stylish(item["children"], depth=depth + 1)}')

        elif item['status'] == 'added':
            lines.append(f'{spacers}+ {item["name"]}: '
                         f'{stringify_value(item["value"], depth)}')

        elif item['status'] == 'deleted':
            lines.append(f'{spacers}- {item["name"]}: '
                         f'{stringify_value(item["value"], depth)}')

        else:
            lines.append(f'{spacers}  {item["name"]}: '
                         f'{stringify_value(item["value"], depth)}')

    return '\n'.join(chain('{', lines, [post_spacers + '}']))


def stringify_value(item, depth: int) -> str:

    if isinstance(item, dict):

        strings = []
        spacers, post_spacers = create_indents(depth + 1)

        for key, value in item.items():
            strings.append(f'{spacers}  {key}: '
                           f'{stringify_value(value, depth + 1)}')

        return '\n'.join(chain('{', strings, [post_spacers + '}']))

    elif isinstance(item, str):
        return item

    else:
        return json.JSONEncoder().encode(item)


def create_indents(depth: int, div=' ', indent: int = 4):

    special_char_index = 2 * (2 * depth - 1)
    spacers = div * special_char_index
    post_spacers = div * ((depth - 1) * indent)

    return spacers, post_spacers
