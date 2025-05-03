class ATM:

    def __init__(self, customer):
        self.__account = customer.get_bank_account()
    
    def display_balance(self):
        print(self.__account.get_balance())

    def make_deposit(self):
        amt = int(input("Enter deposit amount: "))
        self.__account.deposit(amt)

    def make_withdraw(self):
        amt = int(input("Enter withdraw amount: "))
        self.__account.withdraw(amt)

#not part of ATM class, free function
def display_menu():
    print('ACC Example')
    print('1- Display Balance')
    print('2- Deposit')
    print('3- Withdraw')
    print('4- Exit')

def run_menu(atm):

    choice = 0
    while(choice != 4):
        display_menu()
        choice = int(input('Enter menu choice: '))

        handle_user_choice(atm, choice)

def handle_user_choice(atm, choice):
    if(choice == 1):
        atm.display_balance()
    elif(choice == 2):
        atm.make_deposit()
    elif(choice == 3):
        atm.make_withdraw()
    elif(choice == 4):
        print('Exiting...')
    else:
        print('Invalid Entry.')
