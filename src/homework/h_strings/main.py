
from homework.h_strings.strings import get_dna_complement, get_hamming_distance


def main():
        while True:
            print("\n1-Hamming Distance")
            print("2-DNA Complement")
            print("3-Exit")
            choice = input("Enter your choice: ")

            if choice == '1':
                dna1 = input("Enter the first DNA string: ")
                dna2 = input("Enter the second DNA string: ")
                print(f"Hamming Distance: {get_hamming_distance(dna1, dna2)}")
            elif choice == '2':
                dna = input("Enter the DNA string: ")
                print(f"DNA Complement: {get_dna_complement(dna)}")
            elif choice == '3':
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
        main()