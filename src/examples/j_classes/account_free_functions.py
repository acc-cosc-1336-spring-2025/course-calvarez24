def make_deposit(account):
    amt = 100
    account.deposit(amt)

def get_account_object(account):
   
    print(id(account))
    return account
    
