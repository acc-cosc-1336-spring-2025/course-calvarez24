from dictionary import add_inventory , remove_inventory_widget

def main():
    widgets = {}

    while True:
        print("\nInventory Menu")
        print("1- Add or Update Item")
        print("2- Delete Item")
        print("3- Exit")
        choice = input("Enter choice (1-3): ")

        if choice == "1":
            name = input("Enter widget name: ")
            try:
                quantity = int(input("Enter quantity to add or update: "))
                add_inventory(widgets, name, quantity)
                print(f"{name} updated. Current quantity: {widgets[name]}")
            except ValueError:
                print("Please enter a valid integer for a quantity: ")
        elif choice == "2":
            name = input("Enter widget name to delete: ")
            result = remove_inventory_widget(widgets, name)
            print(result)
        elif choice == "3":
            print("Exiting the program...")
            break 
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

main()
