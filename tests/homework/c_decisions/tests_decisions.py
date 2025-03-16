import unittest
from src.homework.c_decisions.decisions import get_options_ratio
from src.homework.c_decisions.decisions import get_faculty_rating

class Test_Config(unittest.TestCase):

    def test_get_options_ratio(self):
        self.assertEqual(0.25, get_options_ratio(5, 20))
        self.assertEqual(0.5, get_options_ratio(10, 20))
        
    def test_get_faculty_rating(self):
        self.assertEqual('Excellent', get_faculty_rating(0.91))
        self.assertEqual('Very Good', get_faculty_rating(0.85))
        self.assertEqual('Good', get_faculty_rating(0.71))
        self.assertEqual('Needs Improvement', get_faculty_rating(0.66))
        self.assertEqual('Unacceptable', get_faculty_rating(0.45))

import unittest 
from src.homework.c_decisions.decisions import sum_odd_numbers

class TestSumOddNumbers(unittest.TestCase):
    def test_sum_odd_positive(self):
        self.assertEqual(sum_odd_numbers(7), 16)
    def test_sum_odd_zero(self):
        self.assertEqual(sum_odd_numbers(9), 25)
    def test_sum_odd_one(self):
        self.assertEqual(sum_odd_numbers(10), 25)
            