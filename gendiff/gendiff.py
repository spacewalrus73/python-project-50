import json
import yaml
from yaml.loader import SafeLoader
from operator import itemgetter


def from_yaml_to_dict(filepath: str) -> dict:
    """The function writes data from the file.yml/file.yaml to a variable.
        Input - filepath, which has a type of string
        Output - dictionary. """
    with open(filepath, 'r') as file:
        data = yaml.load(file, Loader=SafeLoader)
    return data


def from_json_to_dict(filepath: str) -> dict:
    """The function writes data from the file.json to a variable.
    Input - filepath, which has a type of string
    Output - dictionary. """
    with open(filepath, 'r') as file:
        data = json.load(file)
    return data


def to_encode(value) -> str:
    if type(value) is str:
        return value
    else:
        return json.JSONEncoder().encode(value)


'''def from_var_to_file(var) -> json:
    """The function writes data to the file.json
    Input - dictionary, Output - file.json"""
    with open('output_file.json', 'w') as file:
        json.dump(var, file, indent=2)'''


def generate_diff(file1: dict, file2: dict) -> str:
    """The function find the difference between
    two files and return the diff string"""
    set_of_keys1 = set(file1)
    set_of_keys2 = set(file2)
    intersection = set_of_keys1 & set_of_keys2
    diff_1 = set_of_keys1 - set_of_keys2
    diff_2 = set_of_keys2 - set_of_keys1
    str_lst = []

    for item in diff_1:
        str_lst.append(f'  - {to_encode(item)}: {to_encode(file1[item])}')

    for item in diff_2:
        str_lst.append(f'  + {to_encode(item)}: {to_encode(file2[item])}')

    for item in intersection:
        if file1[item] == file2[item]:
            str_lst.append(f'    {to_encode(item)}: {to_encode(file2[item])}')
        else:
            str_lst.append(f'  - {to_encode(item)}: {to_encode(file1[item])}'
                           f'\n  + {to_encode(item)}: {to_encode(file2[item])}')

    str_lst = sorted(str_lst, key=itemgetter(4))
    # 4 because of the first letter in str always has index 4
    return '{\n' + "\n".join(str_lst) + '\n}'


__all__ = ('generate_diff',
           'from_yaml_to_dict',
           'from_json_to_dict')
