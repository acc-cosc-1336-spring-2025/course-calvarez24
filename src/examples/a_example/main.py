import devprocess

def main():
    value1 = input("Enter value 1")
    value2 = input("Enter value 2")

    result = devprocess.add_numbers(int(value1), int(value2)) #create the result variable and store the return value of 5,3 in add_numbers
    print(result)

main() #run the main function which calls/uses the add_numbers functions that's in a devprocess.py file

