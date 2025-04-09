# Repository: https://github.com/abboak/lab10-AA-JR
# Partner 1: Jack Reinhart
# Partner 2: Abdulrahman Alkaelani

import unittest
from calculator import add, sub, div, log

class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(3, 4), 7)
        self.assertEqual(add(-2, 2), 0)
        self.assertEqual(add(0, 0), 0)

    def test_subtract(self):
        self.assertEqual(sub(10, 5), 5)
        self.assertEqual(sub(5, 10), -5)
        self.assertEqual(sub(-1, -1), 0)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            div(5, 0)

    def test_logarithm(self):
        self.assertAlmostEqual(log(2, 8), 3, places=5)
        self.assertAlmostEqual(log(10, 100), 2, places=5)

    def test_log_invalid_base(self):
        with self.assertRaises(ValueError):
            log(1, 10)
        with self.assertRaises(ValueError):
            log(-2, 10)

if __name__ == '__main__':
    unittest.main()
