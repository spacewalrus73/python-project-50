#!/usr/bin/env python3
from gendiff.argparser import parse_args
from gendiff.generate_diff import generate_diff


def main():
    file1, file2, output_format = parse_args()
    print(generate_diff(file1, file2, output_format))


if __name__ == '__main__':
    main()
