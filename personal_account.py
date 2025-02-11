from amount import Amount
from datetime import datetime


class PersonalAccount:

    def __init__(self, account_number=int, account_holder=str):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = 0.0
        self.transactions = []

    def deposit(self, amount):
        deposit = Amount(amount, datetime.now(), 'DEPOSIT')
        self.transactions.append(deposit)
        self.balance += amount

    def withdraw(self, amount):
        withdraw = Amount(amount, datetime.now(), 'WITHDRAWAL')
        self.transactions.append(withdraw)
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient funds on your balance")

    def print_transaction_history(self):
        for i in range(len(self.transactions)):
            print(self.transactions[i])

    def get_balance(self):
        print(f'Balance: {self.balance}')

    def get_account_number(self):
        print(f'Account number: {self.account_number}')

    def set_account_number(self, account_number):
        self.account_number = account_number
        print(f'New account number: {self.account_number}')

    def get_account_holder(self):
        print(f"The name of your account holder is {self.account_holder}")

    def set_account_holder(self, account_holder):
        self.account_holder = account_holder
        print(f"Set account holder is {self.account_holder}")

    def __str__(self):
        return (f"Account number: {self.account_number}\n"
                f"Account holder: {self.account_holder}\n"
                f"Balance: {self.balance}\n"
                f"Transactions: {self.transactions}")

    def __add__(self, amount):
        deposit = Amount(amount, datetime.now(), 'DEPOSIT')
        self.transactions.append(deposit)
        self.balance += deposit
        return self

    def __sub__(self, amount):
        withdraw = Amount(amount, datetime.now(), 'WITHDRAWAL')
        self.transactions.append(withdraw)
        self.balance -= withdraw
        return self

    






