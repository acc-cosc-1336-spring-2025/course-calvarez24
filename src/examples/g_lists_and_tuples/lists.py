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


def list_of_car_parts():
    car_parts = ["brake pads", "oil filter", "air filter"]

    print("Here are the car parts that need to be checked:", car_parts)
    
    #accessing the first item in the list
    print("The first part to check is:", car_parts[0])
    
    #update the 'air filter' part to 'cabin air filter'
    car_parts[2] = "cabin air filter"
    print("Update list of car parts:", car_parts)
    
    #adding a new part to the list
    car_parts.append("battery")

    #removing an item from the list
    car_parts.remove("oil filter")
    print("Update list of car parts:", car_parts)

    #loop through the list of parts 
    print("Parts to check during service:")
    for part in car_parts:
        print(part)

    
