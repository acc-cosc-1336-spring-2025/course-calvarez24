import lists

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
    lists.create_list()
    #lists.list_of_car_parts()

def main():
    prod_nums = ['V475', 'F987', 'Q143', 'R688']

    item = input("Enter item:")

    if(item in prod_nums):
        prod_nums.remove(item)

    else:
        print(item, "not in list")

    print(prod_nums)



main()