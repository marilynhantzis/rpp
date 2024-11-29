import unittest
from discriminant import QuadraticEquation


class TestQuadraticEquation(unittest.TestCase):
    def test_discriminant(self):
        eq = QuadraticEquation(1, 2, 1)
        self.assertEqual(eq.discriminant(), 0)

    def test_discriminant_positive(self):
        eq = QuadraticEquation(1, 5, 6)
        self.assertEqual(eq.discriminant(), 1)

