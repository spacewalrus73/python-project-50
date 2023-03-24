import argparse
from gendiff.gendiff_main import generate_diff
from gendiff import encode


parser = argparse.ArgumentParser(
    prog='gendiff',
    description='Compares two configuration files and show a difference.'
)

parser.add_argument('first_file', type=str)
parser.add_argument('second_file', type=str)
parser.add_argument(
    '-f', '--format',
    help='set format of output',
    default='stylish'
)


def to_parse():
    args = parser.parse_args()
    dirs = [args.first_file, args.second_file]
    if str(dirs[0]).endswith('.json') and str(dirs[1]).endswith('.json'):
        files_lst = list(map(encode.from_json_to_dict, dirs))
        print(generate_diff(files_lst[0], files_lst[1], args.format))
    elif str(dirs[0]).endswith('.json'):
        file_json = encode.from_json_to_dict(dirs[0])
        file_yaml = encode.from_yaml_to_dict(dirs[1])
        print(generate_diff(file_json, file_yaml, args.format))
    elif str(dirs[1]).endswith('.json'):
        file_json = encode.from_json_to_dict(dirs[1])
        file_yaml = encode.from_yaml_to_dict(dirs[0])
        print(generate_diff(file_json, file_yaml, args.format))
    else:
        files_lst = list(map(encode.from_yaml_to_dict, dirs))
        print(generate_diff(files_lst[0], files_lst[1], args.format))
