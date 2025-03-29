import unittest

from src.examples.h_strings.strings import test_config, validate_password

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

    def test_string_repetition_operator(self):
        str = 'w' * 5

        self.assertEqual('wwwww', str)


    def test_split_string(self):
        text = 'Four score and seven years ago'
        list1 = text.split()

        self.assertEqual(['Four', 'score', 'and', 'seven', 'years', 'ago'], list1)

    def test_split_string_date(self):
        date1 = '10/08/2024'
        list1 = date1.split('/')
        expected_list = ['10' , '08' , '2024'] #these results are called tokens
                            
        self.assertEqual(expected_list, list1)

    def test_validate_password1(self):
        password = '1234ABCd'

        self.assertEqual(True, validate_password(password))

    def test_validate_password2(self):
        password = '1234Ab'

        self.assertEqual(False, validate_password(password))



