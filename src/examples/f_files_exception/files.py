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

def write_employee_records(file_name):
    file = open(file_name, 'w')

    choice = '1'

    while choice == '1':
        id = input('Enter ID: ')
        name = input('Enter name: ')
        department = input('Enter department: ')

        file.write(id + '\t')
        file.write(name + '\t')
        file.write(department + '\n')

        choice = input('Enter 1 to continue')

    file.close()

def read_employee_record(file_name):
    file = open(file_name, 'r')

    for line in file:
        record = line.split('\t') #['3', 'C++', 'Prog']
        id = record[0]
        name = record[1]
        department = record[2].rstrip('\n')

        print(id, name, department)

    file.close()

def write_list_of_lists(file_name):
    file = open(file_name, 'w')

    prog_langs = [['1', 'C++', 'Prog'], ['2', 'Python', 'Prog'], ['3', 'Java', 'Prog']]

    for lang in prog_langs:
        file.write(lang[0] + '\t')
        file.write(lang[1] + '\t')
        file.write(lang[2] + '\n')

    file.close()

def read_list_of_lists_file(file_name):
    file = open(file_name, 'r')

    list_langs = []

    for line in file:
        record = line.split('\t')
        id = record[0]
        name = record[1]
        department = record[2].rstrip('\n')

        employee_list = [id, name, department]

        list_langs.append(employee_list)

    file.close()

    for employee in list_langs:
        print(employee[0], employee[1], employee[2])











