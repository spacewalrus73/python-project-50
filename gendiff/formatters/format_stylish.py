from itertools import chain
from gendiff.decoder import to_encode


def stylish(value, spacer=' ', def_indent=4):
    def stringify(cur_val, depth):

        if not isinstance(cur_val, dict):
            return to_encode(cur_val)

        strings = []

        sym_idx = 2 * (2 * depth - 1)
        spacers = spacer * sym_idx
        after_str = (def_indent * (depth - 1)) * spacer

        for key, val in cur_val.items():

            if not isinstance(val, tuple):
                strings.append(
                    f'{spacers}  {key}: {stringify(val, depth + 1)}')
                continue
            if len(val) == 2:
                strings.append(
                    f'{spacers}{val[0]} {key}: {stringify(val[1], depth + 1)}')
            else:
                strings.append(
                    f'{spacers}{val[0]} {key}: {stringify(val[1], depth + 1)}')
                strings.append(
                    f'{spacers}{val[2]} {key}: {stringify(val[3], depth + 1)}')
        return '\n'.join(chain('{', strings, [after_str + '}']))
    return stringify(value, 1)
