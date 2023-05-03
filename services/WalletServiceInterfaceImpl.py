from abc import ABC

from data.repositories.WalletRepositoryImpl import WalletRepositoryImpl
from data.repositories.WalletRepositoryInterface import WalletRepositoryInterface
from dtos.request.DepositRequest import DepositRequest
from dtos.request.TransferRequest import TransferRequest
from dtos.request.WithdrawalRequest import WithdrawalRequest
from dtos.response.DepositTransactionResponse import DepositTransactionResponse
from dtos.response.TransferTransactionResponse import TransferTransactionResponse
from dtos.response.WithdrawalTransactionResponse import WithdrawalTransactionResponse
from services.UserServiceInterfaceImpl import UserServiceInterfaceImpl
from services.WalletServiceInterface import WalletServiceInterface


class WalletServicesInterfaceImplementation(WalletServiceInterface, ABC):
    user_service = UserServiceInterfaceImpl()

    def deposit(self, deposit_request: DepositRequest) -> DepositTransactionResponse:
        user = self.user_service.find_user_by_account_number(deposit_request.account_number)
        if user is None:
            raise Exception("User does not exist")

        user.deposit(deposit_request.amount)
        deposit_transaction_response = \
            DepositTransactionResponse(user.get_first_name() + " " + user.get_last_name(), deposit_request.amount,
                                       deposit_request.account_number)

        deposit_transaction_response.set_status("Successful")
        return deposit_transaction_response

    def withdraw(self, withdrawal_request: WithdrawalRequest) -> WithdrawalTransactionResponse:
        sender = self.user_service.find_user_by_account_number(withdrawal_request.account_number)
        if withdrawal_request.password != sender.get_password():
            raise Exception("Invalid pin")
        if sender.get_balance() < withdrawal_request.amount:
            raise ValueError("Insufficient Fund")
        else:
            sender.withdraw(withdrawal_request.amount)
            withdrawal_transaction_response = WithdrawalTransactionResponse(
                sender.get_last_name() + " " + sender.get_last_name(), withdrawal_request.account_number,
                withdrawal_request.amount)
            withdrawal_transaction_response.set_status("Successful")
            return withdrawal_transaction_response

    def transfer(self, transfer_request: TransferRequest) \
            -> TransferTransactionResponse:

        withdrawal_request = WithdrawalRequest(transfer_request.sender_account_number, transfer_request.amount,
                                               transfer_request.password)
        deposit_request = DepositRequest(transfer_request.receiver_account_number, transfer_request.amount)

        self.withdraw(withdrawal_request)
        self.deposit(deposit_request)
        sender = self.user_service.find_user_by_account_number(transfer_request.sender_account_number)
        receiver = self.user_service.find_user_by_account_number(transfer_request.receiver_account_number)
        transfer_transaction_response = TransferTransactionResponse(
            sender.get_last_name() + " " + sender.get_first_name(), receiver.get_last_name() + " "+
            receiver.get_first_name(), transfer_request.amount)
        transfer_transaction_response.set_status("Successful")
        return transfer_transaction_response

    def check_balance(self, account_number, password):
        user = self.user_service.find_user_by_account_number(account_number)
        if password != user.get_password():
            raise Exception("Invalid pin")
        return user.get_balance()
