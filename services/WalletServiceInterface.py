from abc import ABC, abstractmethod


class WalletServiceInterface(ABC):

    @abstractmethod
    def deposit(self, accountNumber, amount):
        pass

    @abstractmethod
    def withdraw(self, account_number, amount, sender_pin):
        pass

    @abstractmethod
    def transfer(self, sender_account_number, receiver_account_number, amount, sender_pin):
        pass

    @abstractmethod
    def check_balance(self, account_number, password):
        pass