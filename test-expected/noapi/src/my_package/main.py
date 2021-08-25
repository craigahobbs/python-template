# Licensed under the MIT License
# https://github.com/johndoe/my-package/blob/main/LICENSE

"""
my-package command-line script main module
"""

import argparse


def main(argv=None):
    """
    my-package command-line script main entry point
    """

    # Command line arguments
    parser = argparse.ArgumentParser(prog='my-package')
    parser.add_argument('numbers', metavar='N', type=float, nargs='+',
                        help='an integer for the accumulator')
    args = parser.parse_args(args=argv)

    # Report the sum
    print(f'The sum is {sum(args.numbers)}')
