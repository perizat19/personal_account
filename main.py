from personal_account import PersonalAccount

if __name__ == '__main__':
    print('Hello')

personal_account1 = PersonalAccount(12345678, 'Peri')
personal_account1.deposit(1000)
personal_account1.withdraw(10)
personal_account1.get_balance()
personal_account1.print_transaction_history()


