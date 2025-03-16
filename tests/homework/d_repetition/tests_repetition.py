import unittest
from src.homework.d_repetition.repetition import get_factorial

class TestGetFactorial(unittest.TestCase):
    def test_factorial_positive(self):
        self.assertEqual(get_factorial(4), 24)
    def test_factorial_zero(self):
        self.assertEqual(get_factorial(5), 120)
    def test_factorial_one(self):
        self.assertEqual(get_factorial(6), 720)
    
                         