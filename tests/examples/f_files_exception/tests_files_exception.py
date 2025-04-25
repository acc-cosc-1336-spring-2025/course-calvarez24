import unittest

from src.examples.f_files_exception.exceptions import test_config

class Test_Config(unittest.TestCase):

    def test_configuration(self):
        self.assertEqual(True, test_config())

    def test_divide_by_zero(self):
        num1 = 4
        num2 = 0

        with self.assertRaises(ZeroDivisionError):
            num1 / num2
            

