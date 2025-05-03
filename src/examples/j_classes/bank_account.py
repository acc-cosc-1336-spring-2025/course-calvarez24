import random

class BankAccount:

    __balance = 0 #class variable-attributes-class data __ means its private, needs to be protected
    __cust_id = 123456

    #constructor -- special function -- executes instance/object/variable creation 1 time
    def __init__(self, balance):
        
        if(balance == 0):
            self.__get_balance_from_db()
        else:
            self.__balance = balance

    def get_balance(self):
        return self.__balance 
    
    def deposit(self, amt):
        if(amt > 0):
            self.__balance += amt

    def withdraw(self, amt):
        if(amt > 0 and amt <= self.__balance):
            self.__balance -= amt
            

    def __get_balance_from_db(self): #private function
        self.__balance = random.randint(1, 10000)
