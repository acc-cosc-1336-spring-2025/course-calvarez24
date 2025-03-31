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

