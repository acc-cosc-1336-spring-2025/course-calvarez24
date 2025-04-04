import unittest

from src.examples.g_lists_and_tuples.lists import get_the_total_values_of_list_items_for_range, get_the_total_values_of_list_items_while, get_total_of_array_elements, get_total_values_of_list_items_for, list_as_return_value_no_param, list_as_return_values, list_as_return_values, test_config, use_list_as_parameter

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
        self.assertEqual(False, 'v475' in prod_nums)

    def test_list_not_in_key_word(self):
        prod_nums = prod_nums = ['V475', 'F987', 'Q143', 'R688']

        self.assertEqual(True, 'v475'not in prod_nums)
        self.assertEqual(False, 'V475'not in prod_nums)
    
    def test_list_clear_items(self):
        list1 = prod_nums = ['V475', 'F987', 'Q143', 'R688']
        prod_nums.clear() #clears the item in the list

        self.assertEqual(True, prod_nums == []) #brackets represent the empty list

    def test_list_sort_function(self):
        prod_nums = ['V475', 'F987', 'Q143', 'R688']
        prod_nums.sort()
        expected_list = ['F987', 'Q143', 'R688', 'V475']

        self.assertEqual(True, prod_nums == expected_list)

    def test_list_remove_item(self):
        prod_nums = ['V475', 'F987', 'Q143', 'R688']
        prod_nums.remove('F987')
        expected_list =  ['V475', 'Q143', 'R688']    

        self.assertEqual(True, prod_nums == expected_list)  

        #if we try to remove something that doesn't exist it gives us an error 

    def test_list_as_function_parameters(self):
        num = 1 #this num is the same as the num in use_list_as_parameter
        list1 = [5, 3, 10]

        use_list_as_parameter(list1, num) #this num is 25

        self.assertEqual(True, num == 1) #will not equal 25
        self.assertEqual(True, list1[0] == 100)

    #points to the same list, same variables 
    def test_list_as_return_value(self):
        list1 = [5, 3, 10]

        return_list = list_as_return_values(list1)

        self.assertEqual(True, list1 == return_list)
        self.assertEqual(True, list1[0] == 100)
        self.assertEqual(True, return_list[0] == 100)
        self.assertEqual(True, list1[0] == return_list[0])

    def test_list_as_return_value_no_param(self):
        return_list, list_address1 = list_as_return_value_no_param()
        list_address2 = id(return_list)


        self.assertEqual(True, list_address1 == list_address2)

    def test_get_the_total_values_of_list_items_while(self):
        result = get_the_total_values_of_list_items_while()

        self.assertEqual(result, 30)
    
    def test_get_the_total_values_of_list_items_for_range(self):
        result = get_the_total_values_of_list_items_for_range()

        self.assertEqual(result, 30)

    def get_total_values_of_list_items_for(self):
        result = get_total_values_of_list_items_for

        
        self.assertEqual(result, 30)

    def test_two_dimensional_list_indexing(self):
        list2 = [1, 2, 3]
        list3 = [4, 5, 6]
        list4 = [7, 8, 9]

        list1 = [list2, list3, list4]

        self.assertEqual(3, list1[0][2])
        self.assertEqual(8, list1[2][1])

    
    def test_tuple_w_list_element(self):
        tuple = (1, 2, [1, 2, 3])

        self.assertEqual(3, tuple[2][2])

    def test_tuple_w_list_element_update_list(self):
        tuple = (1, 2, [1, 2, 3])
        tuple[2].append(10)

        self.assertEqual(10, tuple[2][3])

    def test_convert_tuple_to_list(self):
        tuple = (4, 1, 9)
        list1 = list(tuple)
        expected_list = [4, 1, 9]

        self.assertEqual(expected_list, list1)

    def test_convert_list_to_tuple(self):
        list1 = [8, 1, 0]
        tuple1 = tuple(list1)
        expected_tuple = (8, 1, 0)

        self.assertEqual(expected_tuple, tuple1)

