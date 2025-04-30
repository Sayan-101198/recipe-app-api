"""Test the modules"""

from django.test import SimpleTestCase
from app import calc


class Calctest(SimpleTestCase):
    """Test the calc module"""
    def test_calc_add(self):
        """Test the add function"""
        res = calc.add(5, 6)
        self.assertEqual(res, 11)
    def test_calc_subtract(self):
        """test the substract function"""
        res = calc.substract(10, 15)
        self.assertEqual(res, 5)

