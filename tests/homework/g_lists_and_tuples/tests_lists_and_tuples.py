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

        self.assertEqual(False, list1[0] == list2[0])
