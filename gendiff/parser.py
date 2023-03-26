import argparse


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
    return args.first_file, args.second_file, args.format
