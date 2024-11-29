import unittest  
from discriminant import calculate_discriminant 

class TestDiscriminant(unittest.TestCase):  
    def test_positive_discriminant(self):  
        self.assertGreaterEqual(calculate_discriminant(1, -3, 2), 0) 

    def test_negative_discriminant(self):
        self.assertLess(calculate_discriminant(1, 2, 3), 0)

    def test_zero_discriminant(self):
        self.assertEqual(calculate_discriminant(1, 2, 1), 0)  
