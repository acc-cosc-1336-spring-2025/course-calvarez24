import atm
import bank_account


def main():
    account = bank_account.BankAccount(1000) #created a variable-instance/object
    print(account.get_balance())

    auto_teller = atm.ATM(account)

    atm.run_menu(auto_teller)

    print(account.get_balance())

main()