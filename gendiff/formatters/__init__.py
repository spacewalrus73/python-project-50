from gendiff.formatters.stylish import stylish
from gendiff.formatters.plain import plain
from gendiff.formatters.json import json


def format(diff, output_style):

    if output_style.lower().strip() == 'stylish':
        return stylish(diff)

    elif output_style.lower().strip() == 'plain':
        return plain(diff)

    elif output_style.lower().strip() == 'json':
        return json(diff)

    else:
        return "Incorrect output format! Check the format name."
