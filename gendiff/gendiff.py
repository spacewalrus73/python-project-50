import json
from operator import itemgetter


def from_file_to_var(filepath: str) -> dict:
    """The function writes data from the file to a variable.
    Input - filepath, which has a type of string
    Output - dictionary. """
    with open(filepath, 'r') as file:
        data = json.load(file)
    return data


def from_var_to_file(var: dict) -> json:
    """The function writes data to the file.json
    Input - dictionary, Output - file.json"""
    with open('output_file.json', 'w') as file:
        json.dump(var, file, indent=2)


def generate_diff(file_path1: str, file_path2: str):
    """The function find the difference between
    two files and return the diff string"""
    file_content1 = from_file_to_var(file_path1)
    file_content2 = from_file_to_var(file_path2)
    set_of_keys1 = set(file_content1)
    set_of_keys2 = set(file_content2)
    intersection = set_of_keys1 & set_of_keys2
    diff_1 = set_of_keys1 - set_of_keys2
    diff_2 = set_of_keys2 - set_of_keys1
    str_lst = []

    for value in diff_1:
        str = f'- {value}: {file_content1[value]}'
        str_lst.append(str)

    for value in diff_2:
        str_lst.append(f'+ {value}: {file_content2[value]}')

    for value in intersection:
        if file_content1[value] == file_content2[value]:
            str_lst.append(f'  {value}: {file_content2[value]}')
        else:
            str_lst.append(f'- {value}: {file_content1[value]}\n'
                           f'+ {value}: {file_content2[value]}')

    str_lst = sorted(str_lst, key=itemgetter(2))
    result = '{\n' + " \n".join(str_lst) + '\n}'
    return result
