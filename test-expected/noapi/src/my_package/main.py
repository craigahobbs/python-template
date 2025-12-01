# Licensed under the MIT License
# https://github.com/johndoe/my-package/blob/main/LICENSE

"""
my-package command-line script main module
"""

import argparse
import sys


def main(argv=None):
    """
    my-package command-line script main entry point
    """

    # Command line arguments
    argument_parser_args = {'prog': 'my-package'}
    if sys.version_info >= (3, 14): # pragma: no cover
        argument_parser_args['color'] = False
    parser = argparse.ArgumentParser(**argument_parser_args)
    parser.add_argument('numbers', metavar='N', type=float, nargs='+',
                        help='an integer for the accumulator')
    args = parser.parse_args(args=argv)

    # Report the sum
    print(f'The sum is {sum(args.numbers)}')
