# Licensed under the MIT License
# https://github.com/{{github}}/{{package}}/blob/main/LICENSE

# pylint: disable=missing-class-docstring, missing-function-docstring, missing-module-docstring

import unittest

import {{package | replace("-", "_")}}


class Test(unittest.TestCase):

    def test_import(self):
        self.assertTrue({{package | replace("-", "_")}})
