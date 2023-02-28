#!/usr/bin/env python3
import argparse
from gendiff import gendiff

parser = argparse.ArgumentParser(prog='gendiff', description='Compares two configuration files and show a difference.')  # noqa: E501
parser.add_argument('first_file', type=str)
parser.add_argument('second_file', type=str)
parser.add_argument('-f', '--format', help='set format of output')
args = parser.parse_args()
dir1 = args.first_file
dir2 = args.second_file

def parse():
    parser.parse_args()
    if dir1 and dir2:
        print(gendiff.generate_diff(dir1, dir2))


if __name__ == '__main__':
    parse()
