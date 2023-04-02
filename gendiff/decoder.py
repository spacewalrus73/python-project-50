import json
import yaml
import os
from typing import Any
from yaml.loader import SafeLoader


def to_decode(path: str) -> dict:
    file = reading_data(path)
    return from_json_to_dict(file) if is_json(path) else from_yaml_to_dict(file)


def reading_data(filepath: str):
    with open(os.path.abspath(filepath), 'r') as file:
        return file.read()


def from_yaml_to_dict(file) -> dict:
    return yaml.load(file, Loader=SafeLoader)


def from_json_to_dict(file) -> dict:
    return json.loads(file)


def to_encode(value: Any, quotes=None) -> str:
    """The function encodes value to json/yml format view.
    Flag quotes returns string with quotes.
    Input - any type
    Output - json/yml string."""
    if isinstance(value, str):
        if quotes:
            return f"'{value}'"
        else:
            return value
    else:
        return json.JSONEncoder().encode(value)


def is_json(path: str) -> bool:
    """Simple predicate function to check item's format
    :return True if format is .json"""
    return path.endswith('.json')
