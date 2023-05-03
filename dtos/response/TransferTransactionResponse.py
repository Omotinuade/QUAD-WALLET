class TransferTransactionResponse:
    def __init__(self, sender_name, receiver_name, amount):
        self.__transaction_type = "Transfer"
        self.__senderName = sender_name
        self.__receiver_name = receiver_name
        self.__amount = amount
        self.__status = None

    def set_status(self, status: str):
        self.__status = status

    def get_status(self):
        return self.__status

    def __str__(self) -> str:
        return f"Sender Name:{self.__senderName} \n" \
               f"Receiver Name:{self.__receiver_name} \n" \
               f"Amount:{self.__amount} " \
               f"Transaction Type:{self.__transaction_type} \n" \
               f"Transaction Status:{self.__status} "




