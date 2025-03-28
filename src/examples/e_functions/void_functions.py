def local_variable_scope():
    num = 5 #accesible in the local_variable_scope
    print(num)

    if(True):
        num1 = 1 #accessible outside of the if statement but only in local_variable_scope function
        
    print(num1)


def local_variable_scope_1():
    num = 5
    print(num) #prints the first 5

    while (num > 0):
        num1 = 1
        num -= 1 #num = num - 1, 5 gets subtracted by 1 each time till it goes down to 0
        print(num)

    print(num1) #prints 1

def local_variable_scope_and_main():
    num = 5 #belongs to variable_scope_and_main

    print(num)

    