import bank_account

def main():
    account = bank_account.BankAccount(1000) #created a variable-instance/object
    print(account.get_balance())

    amt = int(input("Enter deposit amount: "))
    account.deposit(amt)
    
    print(account.get_balance())

    amt = int(input("Enter withdraw amount: "))
    account.withdraw(50)

    print(account.get_balance())

main()