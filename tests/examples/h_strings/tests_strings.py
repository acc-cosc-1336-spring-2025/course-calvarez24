import unittest

from src.examples.h_strings.strings import test_config

class Test_Config(unittest.TestCase):

    def test_configuration(self):
        self.assertEqual(True, test_config())

    def test_substring_in_string(self): #no functions, testing built in funcntionality
        text = 'Four score and seven years ago'

        self.assertEqual(True, 'seven' in text)
        self.assertEqual(False, 'Seven' in text)

    def text_substring_not_in_string(self):
        text = 'Four score and seven years ago'

        self.assertEqual(False,'seven' not in text)
        self.assertEqual(True,'Seven' not in text)

    def test_find_substring(self):
        text = 'Four score and seven years ago'

        self.assertEqual(15, text.find('seven')) #same purpose as the last functions with no T or F
        self.assertEqual(-1, text.find("Seven'"))

    def test_replace_old_with_new(self):
        text = 'Four score and seven years ago'
        new_text = text.replace('seven', 'SEVEN') #replaces and gives us a new string

        self.assertEqual('Four score and SEVEN years ago', new_text)

    def test_strip_string(self):
        lang = "C++     "
        new_text = lang.rstrip()

        self.assertEqual('C++', new_text) #eliminates all the spaces from the end 

        lang = "C++\n\n\n\n"
        new_text = lang.rstrip('\n')
        self.assertEqual("C++", new_text)
