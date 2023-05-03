class WithdrawalRequest:
    def __init__(self, account_number, amount, password):
        self.account_number = account_number
        self.amount = amount
        self.password = password
