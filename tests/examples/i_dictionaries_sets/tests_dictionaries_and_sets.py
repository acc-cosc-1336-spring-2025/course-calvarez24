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

    def test_update_value_dictionary(self):
        phonebook = {'555-1111':'Chris', '555-2222':'Katie', '555-3333':'Jack'}
        expected_phonebook = {'555-1111':'Crisis', '555-2222':'Katie', '555-3333':'Jack'}

        key = '555-1111'
        value = 'Crisis'

        if key in phonebook:
            phonebook[key] = value

        self.assertEqual(phonebook, expected_phonebook)

    def test_get_number_of_elements_dictionary(self):
        phonebook = {'555-1111':'Chris', '555-2222':'Katie', '555-3333':'Jack'}
        key_value_count = len(phonebook)

        self.assertEqual(3, key_value_count)

    def test_different_data_type_values(self):
        test_scores = {'123':[88,92,100], '456':95, '789':'dropped'}        
        expected_list = [88,92,100]
        list1 = test_scores['123']

        self.assertEqual(list1, expected_list)

    def test_create_empty_dictionary(self):
        expected_phonebook = {'555-1111':'Chris'}
        phonebook = {} #empty dictionary 
        self.assertEqual(phonebook, {})

        key = '555-1111'
        value = 'Chris'

        phonebook[key] = value

        self.assertEqual(phonebook, expected_phonebook)

    def test_union_of_a_set_(self):
        set1 = set([1,2,3,4])
        set2 = set([3,4,5,6])
        expected_set = set([1,2,3,4,5,6])
        union_set = set1.union(set2)

        self.assertEqual(expected_set,union_set)

    def test_intersection_of_a_set(self):
        set1 = set() #empty set
        set1.add(1)
        set1.add(2)
        set1.add(3)
        set1.add(4)
        set2 = set([3,4,5,6])
        expected_set = set([3,4]) #numbers common in both sets
        intersection_set = set1.intersection(set2) #operators ; set set1 & set2

        self.assertEqual(expected_set, intersection_set)

    def test_difference_of_sets(self): #numbers in one set that aren't in the other
        set1 = set([1,2,3,4])
        set2 = set([3,4,5,6])
        expected_set = set([1,2]) #operators ; set - set2 

        difference_set = set1.difference(set2) 

        self.assertEqual(expected_set, difference_set)

    def test_symmetric_difference_sets(self):
        set1 = set([1,2,3,4])
        set2 = set([3,4,5,6])
        expected_set = ({1,2,5,6})

        symm_diff_set = set1.symmetric_difference(set2) #set1 ^ set2

        self.assertEqual(expected_set, symm_diff_set)


