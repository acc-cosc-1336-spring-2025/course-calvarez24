import unittest

from src.examples.i_dictionaries_sets.dictionaries import test_config

class Test_Config(unittest.TestCase):

    def test_configuration(self):
        self.assertEqual(True, test_config())

    def test_add_key_value_pair_dictionary(self):
        phonebook = {'555-1111':'Chris', '555-2222':'Katie', '555-3333':'Jack'}
        expected_phonebook = {'555-1111':'Chris', '555-2222':'Katie', '555-3333':'Jack', '555-4444':'Python'}\
        
        key = '555-4444'
        value = 'Python'

        if key not in phonebook:
            phonebook[key] = value

        self.assertEqual(phonebook, expected_phonebook)

    def test_delete_key_value_pair_dictionary(self):
        phonebook = {'555-1111':'Chris', '555-2222':'Katie', '555-3333':'Jack'}
        expected_phonebook = {'555-1111':'Chris', '555-3333':'Jack'}

        key = '555-2222'

        if key in phonebook:
            del phonebook[key]

        self.assertEqual(phonebook, expected_phonebook)

