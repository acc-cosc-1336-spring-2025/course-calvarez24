def test_config():
    return True

import unittest
from src.homework import get_options_ratio
from src.homework.c_decisions.decisions import get_faculty_rating

class Test_Config(unittest.TestCase):
    
    def get_options_ratio(self):
        self.assertEqual(5, get_options_ratio(5, 20))