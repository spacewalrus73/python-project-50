import json
import yaml
from pathlib import Path
from yaml.loader import SafeLoader


def get_content(path: str) -> dict:
    with open(path, 'r') as f:
        file = f.read()

    return convert(file, get_format(path))


def convert(file, file_format):

    match file_format:
        case '.json':
            return json.loads(file)
        case '.yml' | '.yaml':
            return yaml.load(file, Loader=SafeLoader)
        case _:
            raise Exception("FileFormatError: Incorrect input file format!")


def get_format(filepath: str):
    return Path(filepath).suffix
