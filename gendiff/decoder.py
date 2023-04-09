import json
import yaml
from typing import Any
from yaml.loader import SafeLoader


def to_decode(path: str, file_format: str) -> dict:
    with open(path, 'r') as f:
        file = f.read()

    if file_format == 'json':
        return from_json_to_dict(file)
    else:
        return from_yaml_to_dict(file)


def from_yaml_to_dict(file) -> dict:
    return yaml.load(file, Loader=SafeLoader)


def from_json_to_dict(file) -> dict:
    return json.loads(file)


def to_encode(value: Any) -> str:

    if isinstance(value, str):
        return value
    else:
        return json.JSONEncoder().encode(value)
