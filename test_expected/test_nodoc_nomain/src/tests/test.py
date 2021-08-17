# Licensed under the MIT License
# https://github.com/johndoe/package-name/blob/main/LICENSE

# pylint: disable=missing-class-docstring, missing-function-docstring, missing-module-docstring

import unittest

import package_name


class Test(unittest.TestCase):

    def test_import(self):
        self.assertTrue(package_name)
