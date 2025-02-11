The Amount class is created to represent the anount of transaction. __init__ magic method initializes its attributes and __str__ magic method retrurns the overall data such as the amount, date and 
transaction type.

The PersonalAccount class is created to represent personal bank account. __init__ initializes its attributes. deposit is a method to deposit money into the account. 
withdraw is a method to withdraw money from the account.
print_transaction_historyis a method to print the transaction history of the account.
get_balance is a method to retrieve the current balance of the account.
get_account_number is a method to retrieve the account number.
set_account_number is a method to set the account number.
get_account_holder is a method to retrieve the account holder's name.
set_account_holder is a method to set the account holder's name.
__str__ magic method provides a string representation of the object for easier readability when printed or converted to a string.
__add__ is a magic method that performs the same operation as the deposit(self, amount) method, allowing for addition of the specified amount to the object.
__sub__ magic method performs the same operation as the withdraw(self, amount) method, allowing for subtraction of the specified amount to the object.

In order to compile my code, in main file create your personal account object with your account number and account holder, then select the method you want to perform.

