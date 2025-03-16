import unittest

from src.examples.d_repetition.repetition import sum_of_squares_indx, test_config

class Test_Config(unittest.TestCase):

    def test_configuration(self):
        self.assertEqual(True, test_config())

def test_sum_of_squares(self):
    self.assertEqual(14, sum_of_squares(3))
    self.assertEqual(30, sum_of_squares(4))
    self.assertEqual(55, sum_of_squares(5))

def test_sum_of_squares(self):
    self.assertEqual(14, sum_of_squares_indx(3))
    self.assertEqual(30, sum_of_squares_indx(4))
    self.assertEqual(55, sum_of_squares_indx(5))
