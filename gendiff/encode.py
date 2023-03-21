import json
import yaml
import os
from typing import Any
from yaml.loader import SafeLoader


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


def to_encode(value: Any) -> str:
    """The function encodes value to json format view
    Input - any type
    Output - json string."""
    if type(value) is str:
        return value
    else:
        return json.JSONEncoder().encode(value)


__all__ = ('from_yaml_to_dict',
           'from_json_to_dict',
           'to_encode')
