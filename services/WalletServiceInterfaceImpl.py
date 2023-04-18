from abc import ABC

from data.repositories.WalletRepositoryImpl import WalletRepositoryImpl
from data.repositories.WalletRepositoryInterface import WalletRepositoryInterface
from services.WalletServiceInterface import WalletServiceInterface


class WalletServicesInterfaceImplementation(WalletServiceInterface, ABC):
    wallet_Repository = WalletRepositoryImpl()

    def deposit(self, account_number, amount):
        user = self.wallet_Repository.find_user_by_account_number(account_number)
        user.deposit(amount)

    def withdraw(self, account_number, amount, sender_pin):
        sender = self.wallet_Repository.find_user_by_account_number(account_number)
        if sender_pin != sender.get_password():
            raise Exception("Invalid pin")
        if sender.get_balance() < amount:
            raise ValueError("Insufficient Fund")
        else:
            sender.withdraw(amount)

    def transfer(self, sender_account_number, receiver_account_number, amount, sender_pin):
        self.withdraw(sender_account_number, amount, sender_pin)
        self.deposit(receiver_account_number, amount)

    def check_balance(self, account_number, password):
        user = self.wallet_Repository.find_user_by_account_number(account_number)
        if password != user.get_password():
            raise Exception("Invalid pin")
        return user.get_balance()
