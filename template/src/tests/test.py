# Licensed under the MIT License
# https://github.com/{{github}}/{{package}}/blob/main/LICENSE

import unittest

import {{package | replace("-", "_")}}


class Test(unittest.TestCase):

    def test_import(self):
        self.assertTrue({{package | replace("-", "_")}})
