from itertools import chain
from gendiff.decoder import to_encode


def stylish(value, spacer=' ', def_indent=4, dep=1):

    lines = []

    sym_idx = 2 * (2 * dep - 1)
    spacers = spacer * sym_idx
    after_str = (def_indent * (dep - 1)) * spacer

    if isinstance(value, dict):
        for k, v in value.items():
            lines.append(f'{spacers}  {k}: {stylish(v, dep=dep + 1)}')
    elif isinstance(value, list):
        lines.append(mk_string(value, spacers, dep))
    else:
        return to_encode(value)

    return '\n'.join(chain('{', lines, [after_str + '}']))


def mk_string(value, _, d):

    lines = []

    for i in value:
        if i['status'] == 'nested_changes':
            lines.append(
                f'{_}  {i["name"]}: {stylish(i["val"], dep=d + 1)}')
        elif i['status'] == 'plain_changes':
            lines.append(
                f'{_}- {i["name"]}: {stylish(i["val1"], dep=d + 1)}\n'
                f'{_}+ {i["name"]}: {stylish(i["val2"])}')
        elif i['status'] == 'added':
            lines.append(f'{_}+ {i["name"]}: {stylish(i["val"], dep=d + 1)}')
        elif i['status'] == 'deleted':
            lines.append(f'{_}- {i["name"]}: {stylish(i["val"], dep=d + 1)}')
        else:
            lines.append(f'{_}  {i["name"]}: {stylish(i["val"], dep=d + 1)}')
    return '\n'.join(chain(lines))
