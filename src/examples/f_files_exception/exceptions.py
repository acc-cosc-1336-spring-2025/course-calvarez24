def test_config():
    return True

def divide_two_numbers(num1, num2):
    result = 0
    if(num2 != 0):
        result = num1 / num2 
    else:
        return "Division by 0 not allowed"
    return result

def multiply_two_numbers():
    num1 = int(input('Enter number 1: '))
    num2 = float(input('Enter number 2: '))

    result = num1 * num2
    print(result)

def multiply_two_numbers_book_way_exception():
    try:
        num1 = int(input('Enter num1: '))
        num2 = float(input('Enter num2: '))

        result = num1 * num2
    except ValueError:
        print('Values must be numeric.')

def multiply_two_numbers_validate():
    num1 = input('Enter num1: ')
    while(not num1.isdigit()):
        num1 = input('Enter num1: ')
    

    num2 = input('Enter num2: ')
    while(not num2.isdigit()):
        num2 = input('Enter num2: ')

    result = int(num1) * int(num2)

    print(result)

def 



