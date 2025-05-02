import atm
import bank_account


def main():
    account = bank_account.BankAccount(1000) #created a variable-instance/object
    print(account.get_balance())

    auto_teller = atm.ATM(account)
    auto_teller.display_balance()

    auto_teller.make_deposit()
    auto_teller.display_balance()
    print(account.get_balance())

    auto_teller.make_withdraw()
    auto_teller.display_balance()
    print(account.get_balance())

    
main()