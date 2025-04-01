import void_functions


def main():
    num = 10 #belongs to main
    void_functions.local_variable_scope_and_main()

    print(num) #both 5 and 10 will print

main()


