from dtos.request.DepositRequest import DepositRequest
from dtos.request.TransferRequest import TransferRequest
from dtos.request.WithdrawalRequest import WithdrawalRequest
from dtos.response.DepositTransactionResponse import DepositTransactionResponse
from dtos.response.TransferTransactionResponse import TransferTransactionResponse
from dtos.response.WithdrawalTransactionResponse import WithdrawalTransactionResponse
from services.WalletServiceInterfaceImpl import WalletServicesInterfaceImplementation


class WalletController:
    wallet_services = WalletServicesInterfaceImplementation()

    def transfer(self, transfer_request: TransferRequest) -> TransferTransactionResponse:
        try:
            return self.wallet_services.transfer(transfer_request)
        except ValueError as ex:
            return ex.args[0]

    def withdraw(self, withdrawal_request: WithdrawalRequest) -> WithdrawalTransactionResponse:
        try:
            return self.wallet_services.withdraw(withdrawal_request)
        except ValueError as ex:
            return ex.args[0]

    def deposit(self, deposit_request: DepositRequest) -> DepositTransactionResponse:
        try:
            return self.wallet_services.deposit(deposit_request)
        except Exception as ex:
            return ex.args[0]

    def check_balance(self, account_number, password):
        try:
            return self.wallet_services.check_balance(account_number, password)
        except ValueError as ex:
            return ex.args[0]
