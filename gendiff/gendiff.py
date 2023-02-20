import argparse

def argparse_help():
    parser = argparse.ArgumentParser(prog='gendiff', description='Compares two configuration files and show a difference.')
    parser.add_argument(dest='first_file')
    parser.add_argument(dest='second_file')
    return parser.parse_args(['-h'])
