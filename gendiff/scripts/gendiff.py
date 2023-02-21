#!/usr/bin/env python3
import argparse
from gendiff.generate_diff import generate_diff


def main():
    description = 'Compares two configuration files and shows a difference.'
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument('-f', '--format', default='stylish',
                        help='set format of output')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    args = parser.parse_args()
    difference = generate_diff(args.first_file, args.second_file, args.format)
    print(difference)


if __name__ == '__main__':
    main()
