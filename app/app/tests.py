"""Ample test"""

from app import calc
from django.test import SimpleTestCase


class CalcTests(SimpleTestCase):

    def test_add_numbers(self):
        res = calc.add(5, 6)

        self.assertEqual(res, 11)

    def test_subtract_numbers(self):
        """susbtarcting numbers"""

        res = calc.subtract(10, 15)

        self.assertEqual(res, 5)
