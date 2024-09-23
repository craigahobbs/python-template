# Licensed under the MIT License
# https://github.com/{{github}}/{{package}}/blob/main/LICENSE
{% if noapi is not defined or not noapi %}
# pylint: disable=missing-class-docstring, missing-function-docstring, missing-module-docstring
{% endif %}
from io import StringIO
import unittest
from unittest.mock import patch

import {{package | replace("-", "_")}}.__main__
from {{package | replace("-", "_")}}.main import main


class TestMain(unittest.TestCase):

    def test_main_submodule(self):
        self.assertTrue({{package | replace("-", "_")}}.__main__)


    def test_main(self):
        with patch('sys.stdout', StringIO()) as stdout, \
             patch('sys.stderr', StringIO()) as stderr:
            main(['1', '2', '3', '4'])
        self.assertEqual(stdout.getvalue(), 'The sum is 10.0\n')
        self.assertEqual(stderr.getvalue(), '')
