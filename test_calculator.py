# https://github.com/nj446/lab11-nj-ma
# Partner 1: Nicolas June
# Partner 2: Mario Alvarez

import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self):
        self.assertEqual(add(1, 1), 2)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)

    def test_subtract(self):
        self.assertEqual(sub(1, 1), 0)
        self.assertEqual(sub(1, -1), 2)
        self.assertEqual(sub(0, 0), 0)
    ##########################

    ######## Partner 1
    def test_multiply(self):
        self.assertEqual(mul(1, 1), 1)
        self.assertEqual(mul(2, 2), 4)
        self.assertEqual(mul(3, 3), 9)

    def test_divide(self):
        self.assertEqual(div(2, 10), 5)
        self.assertEqual(div(5, 20), 4)
        self.assertEqual(div(2, -10), -5)
    ##########################

    ######## Partner 2
    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            div(0, 5)

    def test_logarithm(self):
        self.assertAlmostEqual(log(2, 8), 3)
        self.assertAlmostEqual(log(10, 100), 2)
        self.assertAlmostEqual(log(3, 27), 3)

    def test_log_invalid_base(self):
        with self.assertRaises(ValueError):
            log(1, 10)
    ##########################

    ######## Partner 1
    def test_log_invalid_argument(self):
        with self.assertRaises(ValueError):
            log(2, -5)

    def test_hypotenuse(self):
        self.assertAlmostEqual(hypotenuse(3, 4), 5)
        self.assertAlmostEqual(hypotenuse(5, 12), 13)
        self.assertAlmostEqual(hypotenuse(-3, -4), 5)

    def test_sqrt(self):
        self.assertAlmostEqual(square_root(4), 2)
        self.assertAlmostEqual(square_root(25), 5)
        with self.assertRaises(ValueError):
            square_root(-9)
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()
