from services.WalletServiceInterfaceImpl import WalletServicesInterfaceImplementation


class WalletController:
    wallet_services = WalletServicesInterfaceImplementation()

    def transfer(self, receiver_account_number, sender_account_number, amount, sender_pin):
        try:
            self.wallet_services.transfer(receiver_account_number, sender_account_number, amount, sender_pin)
        except ValueError as ex:
            return ex.args[0]

    def withdraw(self, account_number, amount, sender_pin):
        try:
            self.wallet_services.withdraw(account_number, amount, sender_pin)
        except ValueError as ex:
            return ex.args[0]

    def deposit(self, amount, account_number):
        try:
            self.wallet_services.deposit(amount, account_number)
        except ValueError as ex:
            return ex.args[0]

    def check_balance(self, account_number, password):
        try:
            self.wallet_services.check_balance(account_number, password)
        except ValueError as ex:
            return ex.args[0]
