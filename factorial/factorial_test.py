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
        
    def test_04(self):
        self.assertEqual(
            MathSamples.factorial(3),
            6)

    def test_05(self):
        self.assertEqual(
            MathSamples.factorial(4),
            24)

    def test_06(self):
        self.assertEqual(
            MathSamples.factorial(5),
            120)

    def test_07(self):
        self.assertEqual(
            MathSamples.factorial(6),
            720)