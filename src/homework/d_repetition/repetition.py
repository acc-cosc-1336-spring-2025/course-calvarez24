def get_factorial(num):
    
    if num < 0:
        return "Factorial is not defined for negative numbers."
    elif num == 0:
        return 1
    else:
        factorial = 1
        for i in range(1, num + 1):
            factorial *= i
        return factorial
