# Licensed under the MIT License
# https://github.com/johndoe/package-name/blob/main/LICENSE

from io import StringIO
import unittest
from unittest.mock import patch

import package_name.__main__
from package_name.main import main


class TestMain(unittest.TestCase):

    def test_main_submodule(self):
        self.assertTrue(package_name.__main__)

    def test_main(self):
        with patch('sys.stdout', StringIO()) as stdout, \
             patch('sys.stderr', StringIO()) as stderr:
            main(['1', '2', '3', '4'])
        self.assertEqual(stdout.getvalue(), 'The sum is 10.0\n')
        self.assertEqual(stderr.getvalue(), '')
