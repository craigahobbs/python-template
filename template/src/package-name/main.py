# Licensed under the MIT License
# https://github.com/{{github}}/{{package}}/blob/main/LICENSE

import argparse


def main(argv=None):

    # Command line parsing
    parser = argparse.ArgumentParser(prog='{{package}}')
    parser.add_argument('numbers', metavar='N', type=float, nargs='+',
                        help='an integer for the accumulator')
    args = parser.parse_args(args=argv)

    # Report the sum
    print(f'The sum is {sum(args.numbers)}')
