import lists
#import tuples

def main():
    #lists.create_array1() 
    #lists.create_array2()
    #lists.access_array_elements()
    #lists.loop_array_elements_while()
    #lists.loop_array_elements_for_range()
    #lists.modify_array_element1()
    #lists.modify_array_element2()
    #lists.add_array_elements()
    #lists.delete_array_elements()
    #lists.get_total_of_array_elements()
    #lists.array_of_characters()
    #lists.create_list()
    #lists.list_of_car_parts()

#def main():
    prod_nums = ['V475', 'F987', 'Q143', 'R688']

    item = input("Enter item:")

    if(item in prod_nums):
        prod_nums.remove(item)

    else:
        print(item, "not in list")

    print(prod_nums)

#def main():
    table = lists.get_multiplication_table(10, 10)

    lists.display_multiplication_table(table)

#def main():
    tuples.create_a_tuple()

#def main():
    tuples.store_different_data_in_tuple()


#def main():
    payroll_list = [
        ['C++', 40, 20, 0],
        ['Java', 35, 25, 0],
        ['C#', 40, 30, 0]
                    
    ]
    lists.display_employee_payroll_list(payroll_list)
    print('------------------')
    lists.calculate_employee_gross_pay(payroll_list)

    lists.display_employee_payroll_list(payroll_list)

def main():
    class_list = [
        ['C++', [100, 80, 90, 70, 100], 0], 
        ['Java', [90, 80, 50, 70, 60], 0],
        ['C#', [100, 50, 95, 0, 80], 0]
    ]

    print(class_list)
    print('------------------')
    lists.calculate_student_grades(class_list)

    print(class_list) 


main()