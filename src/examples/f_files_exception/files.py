def write_to_file(file_name):
    file = open(file_name, 'w') #write in file

    file.write('John Locke\n')
    file.write('David Hume\n')
    file.write('Edmund Burke\n')

    file.close()

def read_from_file(file_name):
    file = open(file_name, 'r') #read file

    file_lines = file.read()
    file.close()

    print(file_lines)

def read_from_file_one_line_at_a_time(file_name):
    file = open(file_name, 'r')

    line1 = file.readline().rstrip('\n')
    line2 = file.readline().rstrip('\n')
    line3 = file.readline().rstrip('\n')

    file.close()

    print(line1)
    print(line2)
    print(line3)

def read_from_file_w_a_loop(file_name):
    file = open(file_name, 'r')

    for line in file:
        print(line.rstrip('\n'))

    file.close()

def write_sales_data(file_name):
    file = open(file_name, 'w')

    num1 = 0

    while num1 != 'n':
        num1 = input("Enter sales data: ")

        if(num1 != 'n'):
            file.write(num1 + '\n')

    file.close()

def read_sales_data(file_name):
    file = open(file_name, 'r')
    line = file.readline()

    total = 0

    while line != '':
        amount = int(line)
        total += amount 
        print(amount)

        line = file.readline()

    file.close()
    print()
    print(total)







