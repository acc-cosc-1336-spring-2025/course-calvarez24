import lists 

def show_low_high_values(lst):
    if lst:
        print(f"Low value: {min(lst)}")
        print(f"High value: {max(lst)}")
    else:
        print("The list is empty.")

def main():
    while True:
        print("\nMenu:")
        print("1- Show the list low/high values")
        print("2- Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            values_list = []  
            
            while True:
                value = input("Enter a list value: ")
            
                try:
                    values_list.append(float(value))
                except ValueError:
                    print("Invalid value, please enter a valid number.")
                    continue
                
                if len(values_list) >= 3:
                    continue_input = input("Do you want to enter another value? (yes/no): ").lower()
                    if continue_input != 'yes':
                        break  
                
            show_low_high_values(values_list)
        
        elif choice == '2':
            print("Exiting program.")
            break  
        
        else:
            print("Invalid choice, please select a valid option.")


main()