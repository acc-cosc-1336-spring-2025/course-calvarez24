import decisions    

def main():
    x = float(input("Enter value 1:"))
    y = float(input("Enter totals:"))
    result = decisions.get_options_ratio(x , y)

    print(decisions.get_faculty_rating(result))
main()
