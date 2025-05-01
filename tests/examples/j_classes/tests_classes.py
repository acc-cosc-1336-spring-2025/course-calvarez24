import unittest

from src.examples.j_classes.bank_account import BankAccount

class Test_Config(unittest.TestCase):

    def test_account_begin_balance(self):
        account = BankAccount(1000)
        self.assertEqual(1000, account.get_balance())