

class Customer:

    def __init__(self, bank_account):
        self.__bank_account = bank_account

    def get_bank_account(self):
        return self.__bank_account
    
    