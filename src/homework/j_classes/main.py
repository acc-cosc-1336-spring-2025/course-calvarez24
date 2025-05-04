from class_a import Die

def main():
    die = Die()

    while True:
        user_input = input("Roll the dice? yes or no: ").lower()

        if user_input == "yes":
            die.roll()
            print(die)
        elif user_input == "no":
            print("Goodbye")
            break 
        else:
            print("Please type yes or no")

main()
