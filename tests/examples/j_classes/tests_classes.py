import unittest

from src.examples.j_classes.bank_account import BankAccount

class Test_Config(unittest.TestCase):

    def test_account_begin_balance(self):
        account = BankAccount(1000)
        self.assertEqual(1000, account.get_balance())

    def test_account_deposit(self):
        account = BankAccount(1000) #created instance/object; a class variable 

        self.assertEqual(1000, account.get_balance())

        account.deposit(100)

        self.assertEqual(1100, account.get_balance())
