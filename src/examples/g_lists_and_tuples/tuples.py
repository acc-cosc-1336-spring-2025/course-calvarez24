def create_a_tuple():
    tuple = (1, 2, 3, 4, 5)

    for item in tuple:
        print(item)

    for i in range(0, len(tuple)):
        print(tuple[1])

    print('----------------')

    indx = 0 

    while(indx < len(tuple)):
        print(tuple[indx])
        indx += 1
    
def store_different_data_in_tuple():
    tuple = (1, 'a', 2.5, True)

    for item in tuple:
        print(item)