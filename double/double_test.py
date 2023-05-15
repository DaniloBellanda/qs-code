import unittest
from math_samples import MathSamples

class DoubleTest(unittest.TestCase):

    def test_double01(self):
        self.assertEqual(
            MathSamples.double(0),
            0)

    def test_double02(self):
        self.assertEqual(
            MathSamples.double(1),
            1)