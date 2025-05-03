import atm
import bank_account
import bank_account_db
import customer


def main():
    accountDB = bank_account_db.BankAccountDB()
    balance = accountDB.get_current_balance()

    account = bank_account.BankAccount(balance) #created a variable-instance/object
    bank_customer = customer.Customer(account)
    print(account.get_balance())

    auto_teller = atm.ATM(bank_customer)

    atm.run_menu(auto_teller)

    print(account.get_balance())

main()