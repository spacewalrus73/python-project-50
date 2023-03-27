#!/usr/bin/env python3
from gendiff.parser import to_parse
from gendiff.generate_diff import generate_diff
from gendiff.decoder import to_decode


def main():
    file1, file2, frmt = to_parse()
    print(generate_diff(to_decode(file1), to_decode(file2), frmt))


if __name__ == '__main__':
    main()
