import unittest
from math_samples import MathSamples

class FactorialTest(unittest.TestCase):

    def test_01(self):
        self.assertEqual(
            MathSamples.factorial(0),
            0)
        
    def test_02(self):
        self.assertEqual(
            MathSamples.factorial(1),
            1)

    def test_03(self):
        self.assertEqual(
            MathSamples.factorial(2),
            2)