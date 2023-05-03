class TransferRequest:
    def __init__(self, sender_account_number, receiver_account_number, amount, password):
        self.sender_account_number = sender_account_number
        self.receiver_account_number = receiver_account_number
        self.amount = amount
        self.password = password
