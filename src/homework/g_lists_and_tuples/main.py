from lists import get_p_distance , get_p_distance_matrix

def main():
    while True:
        print("\nMenu")
        print("1 - Get p distance matrix")
        print("2 - Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            print("\nEnter DNA strings one per line.")
            print("Type 'done' when finished.\n")

            dna_lists = []

            while True:
                line = input("DNA string: ").strip()
                if line.lower() == "done":
                    break
                if line:
                    dna_lists.append(list(line))

            if len(dna_lists) < 2:
                print("You need at least two DNA strings.")
            else:
                matrix = get_p_distance_matrix(dna_lists)
                print("\nP-distance Matrix:")
                for row in matrix:
                    print(" ".join(f"{value:.5f}" for value in row))

        elif choice == "2":
            print("Exiting program.")
            break
        else:
            print("Invalid choice, try again.")

main()


