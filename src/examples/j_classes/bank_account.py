class BankAccount:

    __balance = 100 #class variable-attributes-class data

    #constructor 
    def __init__(self, balance):
        self.__balance = balance

    def get_balance(self):
        return self.__balance 