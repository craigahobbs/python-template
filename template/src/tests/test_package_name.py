# Licensed under the MIT License
# https://github.com/{{github}}/{{package}}/blob/main/LICENSE
{% if noapi is not defined or not noapi %}
# pylint: disable=missing-class-docstring, missing-function-docstring, missing-module-docstring
{% endif %}
import unittest

from {{ package | replace('-', '_') }} import sum_numbers


{% set packageClass = package.replace('-', ' ').title().replace(' ', '') -%}
class Test{{ package | replace('-', ' ') | title  | replace(' ', '') }}(unittest.TestCase):

    def test_sum_numbers(self):
        self.assertEqual(sum_numbers([1, 2, 3]), 6)

    def test_sum_numbers_empty(self):
        self.assertEqual(sum_numbers([]), 0)
