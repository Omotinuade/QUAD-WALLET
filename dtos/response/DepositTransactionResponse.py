class DepositTransactionResponse:
    def __init__(self, name, amount, account_number):
        self.__transaction_type = "Deposit"
        self.__name = name
        self.__account_number = account_number
        self.__amount = amount
        self.__status = None

    def set_status(self, status: str):
        self.__status = status

    def get_status(self):
        return self.__status

    def __str__(self):
        return f"Full name:{self.__name} \n" \
               f"Account Number:{self.__account_number} \n" \
               f"Amount:{self.__amount} " \
               f"Transaction Type:{self.__transaction_type} \n" \
               f"Transaction Status:{self.__status} "


