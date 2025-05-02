class ATM:

    def __init__(self, account):
        self.__account = account
    
    def display_balance(self):
        print(self.__account.get_balance())

    def make_deposit(self):
        amount = int(input("Enter deposit amount: "))
        self.__account.deposit(amount)

    def make_withdraw(self):
        amt = int(input("Enter withdraw amount: "))
        self.__account.withdraw(amt)