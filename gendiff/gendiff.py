import argparse


def parse_help():
    parser = argparse.ArgumentParser(prog='gendiff',
                                     description='Compares two configuration files and show a difference.')
    parser.add_argument('first_file', type=str)
    parser.add_argument('second_file', type=str)
    parser.add_argument('-f', '--format', help='set format of output')
    args = parser.parse_args()

