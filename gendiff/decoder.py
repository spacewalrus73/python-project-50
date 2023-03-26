import json
import yaml
import os
from typing import Any
from yaml.loader import SafeLoader


def to_decode(path: str) -> dict:
    return from_json_to_dict(path) if is_json(path) else from_yaml_to_dict(path)


def from_yaml_to_dict(filepath: str) -> dict:
    """The function writes data from the file.yml/file.yaml to a variable.
        Input - filepath, which has a type of string
        Output - dictionary."""
    with open(os.path.abspath(filepath), 'r') as file:
        data = yaml.load(file, Loader=SafeLoader)
    return data


def from_json_to_dict(filepath: str) -> dict:
    """The function writes data from the file.json to a variable.
    Input - filepath, which has a type of string
    Output - dictionary."""
    with open(os.path.abspath(filepath), 'r') as file:
        data = json.load(file)
    return data


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
