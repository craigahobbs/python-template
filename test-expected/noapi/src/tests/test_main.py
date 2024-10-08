# Licensed under the MIT License
# https://github.com/johndoe/my-package/blob/main/LICENSE

from io import StringIO
import unittest
from unittest.mock import patch

import my_package.__main__
from my_package.main import main


class TestMain(unittest.TestCase):

    def test_main_submodule(self):
        self.assertTrue(my_package.__main__)


    def test_main(self):
        with patch('sys.stdout', StringIO()) as stdout, \
             patch('sys.stderr', StringIO()) as stderr:
            main(['1', '2', '3', '4'])
        self.assertEqual(stdout.getvalue(), 'The sum is 10.0\n')
        self.assertEqual(stderr.getvalue(), '')
