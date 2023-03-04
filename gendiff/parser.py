import argparse
from os import path
from gendiff import gendiff

parser = argparse.ArgumentParser(prog='gendiff', description='Compares two configuration files and show a difference.')  # noqa: E501

parser.add_argument('first_file', type=str)
parser.add_argument('second_file', type=str)
parser.add_argument('-f', '--format', help='set format of output')


def to_parse():
    args = parser.parse_args()
    dirs = [args.first_file, args.second_file]
    input_format = path.splitext(dirs[0])[1]
    if input_format == '.json':
        files_lst = list(map(gendiff.from_json_to_dict, dirs))
        print(gendiff.generate_diff(files_lst[0], files_lst[1]))
    else:
        files_lst = list(map(gendiff.from_yaml_to_dict, dirs))
        print(gendiff.generate_diff(files_lst[0], files_lst[1]))
