import math

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def sum_odd_numbers(n):
    sum_odds = 0
    for i in range(1, n + 1, 2):
        sum_odds += i
    return sum_odds

continue_program = True
while continue_program:
    print("Homework 3 Menu")
    print("1-Factorial")
    print("2-Sum odd numbers")
    print("3-Exit")

    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue

    if choice == 1:
        while True:
            try:
                num = int(input("Enter a number between 1 and 9: "))
                if 1 <= num <= 9:
                    break
                else:
                    print("Invalid input. Number must be between 1 and 9.")
            except ValueError:
                print("Invalid input. Please enter a number.")
        result = factorial(num)
        print(f"Factorial of {num} is {result}")
    elif choice == 2:
        while True:
            try:
                num = int(input("Enter a number between 1 and 99: "))
                if 1 <= num <= 99:
                    break
                else:
                    print("Invalid input. Number must be between 1 and 99.")
            except ValueError:
                print("Invalid input. Please enter a number.")
        result = sum_odd_numbers(num)
        print(f"Sum of odd numbers up to {num} is {result}")
    elif choice == 3:
        exit_choice = input("Are you sure you want to exit? (yes/no): ")
        if exit_choice.lower() == "yes":
            continue_program = False
    else:
        print("Invalid choice. Please try again.")
    
    if choice != 3:
        exit_choice = input("Do you want to exit? (yes/no): ")
        if exit_choice.lower() == "yes":
            continue_program = False