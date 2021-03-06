# Licensed under the MIT License
# https://github.com/{{github}}/{{package}}/blob/main/LICENSE
{% if noapi is not defined or not noapi %}
# pylint: disable=missing-class-docstring, missing-function-docstring, missing-module-docstring
{% endif %}
import unittest

import {{package | replace("-", "_")}}


class Test(unittest.TestCase):

    def test_import(self):
        self.assertTrue({{package | replace("-", "_")}})
