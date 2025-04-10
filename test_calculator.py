# Repository: https://github.com/abboak/lab10-AA-JR
# Partner 1: Jack Reinhart
# Partner 2: Abdulrahman Alkaelani

import unittest
from calculator import *

class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(3, 4), 7)
        self.assertEqual(add(-2, 2), 0)
        self.assertEqual(add(0, 0), 0)

    def test_subtract(self):
        self.assertEqual(subtract(10, 5), 5)
        self.assertEqual(subtract(5, 10), -5)
        self.assertEqual(subtract(-1, -1), 0)

    def test_multiply(self):
        self.assertEqual(mul(3, 4), 12)
        self.assertEqual(mul(-2, 5), -10)
        self.assertEqual(mul(0, 100), 0)

    def test_divide(self):
        self.assertAlmostEqual(div(10, 2), 5.0)
        self.assertAlmostEqual(div(3, 2), 1.5)
        self.assertAlmostEqual(div(-6, 3), -2.0)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            div(5, 0)

    def test_logarithm(self):
        self.assertAlmostEqual(logarithm(2, 8), 3, places=5)
        self.assertAlmostEqual(logarithm(10, 100), 2, places=5)


    def test_log_invalid_argument(self):
        with self.assertRaises(ValueError):
            logarithm(2, -10)
        with self.assertRaises(ValueError):
            logarithm(2, 0)

    def test_log_invalid_base(self):
        with self.assertRaises(ValueError):
            logarithm(1, 10)
        with self.assertRaises(ValueError):
            logarithm(-2, 10)

    def test_sqrt(self):
        self.assertAlmostEqual(square_root(4), 2.0, places=5)
        self.assertAlmostEqual(square_root(9), 3.0, places=5)
        with self.assertRaises(ValueError):
            square_root(-1)

    def test_hypotenuse(self):
        self.assertAlmostEqual(hypotenuse(3, 4), 5.0, places=5)
        self.assertAlmostEqual(hypotenuse(5, 12), 13.0, places=5)


if __name__ == '__main__':
    unittest.main() 
