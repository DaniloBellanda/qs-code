import unittest
from math_samples import MathSamples

class FactorialTest(unittest.TestCase):

    def test_01(self):
        self.assertEqual(
            MathSamples.factorial(0),
            0)