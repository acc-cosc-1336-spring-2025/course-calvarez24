import unittest

from src.homework.g_lists_and_tuples.lists import get_lowest_list_value , get_highest_list_value , get_p_distance , get_p_distance_matrix

class Test_Config(unittest.TestCase):

    def test_get_lowest_value(self):
        test_list = [8, 10, 1, 50, 20]
        result = get_lowest_list_value(test_list)

        self.assertEqual(result, 1)

    def test_get_highest_list_value(self):
        test_list = [8, 10, 1, 50, 20]
        result = get_highest_list_value(test_list)

        self.assertEqual(result, 50)

    def test_p_distance(self):
        list1 = ['T','T','T','C','C','A','T','T','T','A']
        list2 = ['G','A','T','T','C','A','T','T','T','C']
        self.assertAlmostEqual(get_p_distance(list1, list2), 0.4, places=5)

    def test_get_p_distance_matrix(self):
        dna_lists = [
            ['T','T','T','C','C','A','T','T','T','A'],
            ['G','A','T','T','C','A','T','T','T','C'],
            ['T','T','T','C','C','A','T','T','T','T'],
            ['G','T','T','C','C','A','T','T','T','A']
        ]
        expected = [
            [0.0, 0.4, 0.1, 0.1],
            [0.4, 0.0, 0.4, 0.3],
            [0.1, 0.4, 0.0, 0.2],
            [0.1, 0.3, 0.2, 0.0]
        ]
        result = get_p_distance_matrix(dna_lists)
        for row1, row2 in zip(result, expected):
            for val1, val2 in zip(row1, row2):
                self.assertAlmostEqual(val1, val2, places=3)