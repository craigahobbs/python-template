# Licensed under the MIT License
# https://github.com/johndoe/my-package/blob/main/LICENSE

import unittest

import my_package


class Test(unittest.TestCase):

    def test_import(self):
        self.assertTrue(my_package)
