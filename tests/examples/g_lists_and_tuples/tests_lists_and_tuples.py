import unittest

from src.examples.g_lists_and_tuples.lists import get_total_of_array_elements, test_config

class Test_Config(unittest.TestCase):

    def test_configuration(self):
        self.assertEqual(True, test_config())

    def test_get_total_of_array_elements(self):
        total = get_total_of_array_elements()

        self.assertEqual(total, 15)

    def test_list_copy_memory(self):
        list1 = [5, 4, 10]
        list2 = list1 #no copy created. 2 different variables referencing the same list

        self.assertEqual(True, list1 == list2)
        list1[0] = 20

        #self.assertEqual(True, list1 != list2)

        self.assertEqual(True, list1[0] == list2[0])

    def test_list_copy_w_loop(self):
        list1 = [5, 4, 10]
        list2 = []
    
        for item in list1:
            list2.append(item) #append adds a single element to the list

        self.assertEqual(True, list1 == list2) #is it comparing values or memory location

        list1[0] = 20

        self.assertEqual(False, list1 == list2)

    def test_list_concatenate(self):
        list1 = [5, 4, 10]
        list2 = []
        list3 = list1 + list2 #creates a completely new list

        self.assertEqual(True, list1 == list3) #true because both lists have values 5,4,10

        list1[0] = 20

        self.assertEqual(False, list1 == list3)

        self.assertEqual(False, list1[0] == list3[0])

    def test_list_repetition_operator(self):
        list1 = [0] * 5
        expected_list = [0,0,0,0,0]

        self.assertEqual(True, list1 == expected_list)

        list1 = [1,2,3] * 2
        expected_list = [1,2,3,1,2,3]

        self.assertEqual(True, list1 == expected_list)

    def test_list_in_key_word(self):
        prod_nums = ['V475', 'F987', 'Q143', 'R688']

        self.assertEqual(True, 'V475' in prod_nums)