# Licensed under the MIT License
# https://github.com/johndoe/package-name/blob/main/LICENSE

# pylint: disable=missing-class-docstring, missing-function-docstring, missing-module-docstring

import unittest

from package_name import sum_numbers


class TestPackageName(unittest.TestCase):

    def test_sum_numbers(self):
        self.assertEqual(sum_numbers([1, 2, 3]), 6)

    def test_sum_numbers_empty(self):
        self.assertEqual(sum_numbers([]), 0)
