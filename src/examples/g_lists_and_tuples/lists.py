import array #python library, not in the core python language 

def test_config():
    return True

def create_array1():
    nums = array.array('i' , [1,2,3,4,5])  #creates an array list of integers, hence the 'i'
    print(nums)  #

def create_array2():
    nums = array.array('i' , [1,2,3,4,5])

    for num in nums:
        print(num)

def access_array_elements():
    nums = array.array('i' , [1,2,3,4,5])

    print(nums[0])
    print(nums[1])
    print(nums[2])
    print(nums[3])

def loop_array_elements_while():
    nums = array.array('i' , [1,2,3,4,5])
    indx = 0

    while(indx < len(nums)): #while indx is less than the length of numbers
        print(nums[indx])
        indx += 1 #need to make the loop end 

def loop_array_elements_for_range():
    nums = array.array('i' , [1,2,3,4,5])

    for indx in range(0, len(nums)):
        print(nums[indx])

def modify_array_element1():
    nums = array.array('i' , [1,2,3,4,5])

    nums[0] = 10 #replaces indx 0 with 10
    print(nums[0])

def modify_array_element2():
    nums = array.array('i' , [1,2,3,4,5])

    print(nums[0]) #prints out indx 0 = 1

    nums[0] = 10 #replaces indx 0 with 10
    print(nums[0])
     
def add_array_elements():
    nums = array.array('i' , [1,2,3,4,5])
    nums.append(6) #adds value 6 to the end of the array/list

    for num in nums:
        print(num)

def delete_array_elements():
    nums = array.array('i' , [1,2,3,4,5])

    nums.remove(3)
    nums.remove(4) #in order to remove 2 numbers, we need to add another remove line 

    for num in nums:
        print(num)

def get_total_of_array_elements():
    nums = array.array('i' , [1,2,3,4,5])
    total = 0

    for num in nums:
        total += num
        
    return total

def create_list():
    list = [1, 'bb' , 5.5, True]

    print(list)

    for item in list:
        print(item)

def use_list_as_parameter(list1, num):

    list1[0] = 100
    num = 25

def list_as_return_values(list1):
    list1[0] = 100

    return list1 #because we're modifying the list, this return list1 is unnecessary 

def list_as_return_value_no_param():
    list1 = [5, 3, 10]


    return list1, id(list1) #return list and address of where its located at
    
def get_the_total_values_of_list_items_while():
    total = 0
    indx = 0
    list1 = [2, 4, 6, 8, 10]

    while(indx < len(list1)):
        total += list1[indx] #same as total = total + list1[indx]

        indx += 1

    return total
    
def get_the_total_values_of_list_items_for_range():
    total = 0
    list1 = [2, 4, 6, 8, 10]

    for i in range(0, len(list1)):
            total += list1[i]

    return total

def get_total_values_of_list_items_for():
    total = 0
    list1 = [2, 4, 6, 8, 10]

    for item in list1: #for every item in list1
        total += item

    return total

def get_multiplication_table(rows, cols):
    list =[]

    for i in range(0, rows): #loop all rows
        row_list = []

        for j in range(0, cols): #loop all columns 
            row_list.append((i + 1) * (j + 1))
  
        list.append(row_list) #adds each row (row_list) to the master list (list)

    return list

def display_multiplication_table(list): #takes a list, u iterate thru the elements and display one element at a time

    for row_list in list:
        for product in row_list:
            print(str(product).rjust(3, " "), end = " ")

        print(" ")