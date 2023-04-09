from itertools import chain
from gendiff.decoder import to_encode


def stylish(value, depth: int = 1):

    lines = []
    spacers, post_spacers = create_indents(depth)

    for item in value:

        sample = f'{spacers}? {item["name"]}: '
        begin_string = ''

        if item['status'] == 'plain_changes':
            begin_string = sample.replace('?', '-', 1)
            tail = stringify_value(item["old_value"], depth)
            lines.append(begin_string + tail)
            begin_string = sample.replace('?', '+', 1)
            tail = stringify_value(item["new_value"], depth)
            lines.append(begin_string + tail)
            continue

        elif item['status'] == 'nested_changes':
            begin_string = sample.replace('?', ' ', 1)
            tail = stylish(item["children"], depth=depth + 1)
            lines.append(begin_string + tail)
            continue

        elif item['status'] == 'added':
            begin_string = sample.replace('?', '+', 1)

        elif item['status'] == 'deleted':
            begin_string = sample.replace('?', '-', 1)

        else:
            begin_string = sample.replace('?', ' ', 1)

        lines.append(begin_string + stringify_value(item["value"], depth))

    return '\n'.join(chain('{', lines, [post_spacers + '}']))


def stringify_value(item, depth: int) -> str:

    if isinstance(item, dict):

        strings = []
        spacers, post_spacers = create_indents(depth + 1)

        for key, value in item.items():
            strings.append(f'{spacers}  {key}: '
                           f'{stringify_value(value, depth + 1)}')

        return '\n'.join(chain('{', strings, [post_spacers + '}']))

    else:
        return to_encode(item)


def create_indents(depth: int, div=' ', indent: int = 4):

    special_char_index = 2 * (2 * depth - 1)
    spacers = div * special_char_index
    post_spacers = div * ((depth - 1) * indent)

    return spacers, post_spacers
