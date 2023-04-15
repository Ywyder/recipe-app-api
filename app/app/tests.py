"""
sample tests
"""

from django.test import SimpleTestCase

from app import calc


class CalcTests(SimpleTestCase):
    """Test the calc module."""

    def test_add_numbers(self):
        """test adding numbers together."""
        res = calc.add_numbers(5, 6)

        self.assertEqual(res, 11)

    def test_substract_numbers(self):
        """test substraction of numbers """
        res = calc.substract_numbers(10,15)

        self.assertEqual(res, 5)
