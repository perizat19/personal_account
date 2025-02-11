from datetime import datetime


class Amount:

    def __init__(self, amount=float, timestamp=datetime.now(), transaction_type=str):
        self.amount = amount
        self.timestamp = timestamp
        self.transaction_type = transaction_type

    def __str__(self):
        return (f'Amount: {self.amount}\n'
                f'Date: {self.timestamp}\n'
                f'Transaction type: {self.transaction_type}')


