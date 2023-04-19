from gendiff.formatters.stylish import stylish
from gendiff.formatters.plain import plain
from gendiff.formatters.json import json


def format(diff, output_style):

    match output_style.lower().strip():
        case 'stylish':
            return stylish(diff)
        case 'plain':
            return plain(diff)
        case 'json':
            return json(diff)
        case _:
            raise Exception("FileFormatError: Incorrect output format!")
