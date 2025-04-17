def test_config():
    return True

def use_a_dictionary():
    phonebook = {'555-1111':'Chris', '555-2222':'Katie', '555-3333':'Jack'}
    print(phonebook) #lazy print

    print(phonebook['555-2222']) #finds the value, outputs Katie, keys work as index's
    print(phonebook['555-1111'])
    print(phonebook['555-3333'])

    if('555-4444' in phonebook):
        print(phonebook['555-4444']) 
    else:
        print('Key does not exist')

def add_key_value_pair():
    phonebook = {'555-1111':'Chris', '555-2222':'Katie', '555-3333':'Jack'}

    key = input("Enter the key: ")
    value = input("Enter the value: ")

    if key not in phonebook:
        phonebook[key] = value
    else:
        print(key, " already exists.")

    print(phonebook)

def delete_key_value_pair():
    phonebook = {'555-1111':'Chris', '555-2222':'Katie', '555-3333':'Jack'}

    key = input("Enter the key: ")
    
    if key in phonebook:
        del phonebook[key]
    else:
        print("Key ", key, " does not exist.")

    print(phonebook)

def update_value():
    phonebook = {'555-1111':'Chris', '555-2222':'Katie', '555-3333':'Jack'}

    key = input("Enter the key: ")
    value = input("Enter new value: ")

    if key in phonebook:
        phonebook[key] = value
    else:
        print("Key ", key, " does not exist.")

    print(phonebook)