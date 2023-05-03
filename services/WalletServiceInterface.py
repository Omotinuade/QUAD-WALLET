from abc import ABC, abstractmethod

from dtos.request.DepositRequest import DepositRequest
from dtos.request.TransferRequest import TransferRequest
from dtos.request.WithdrawalRequest import WithdrawalRequest
from dtos.response.DepositTransactionResponse import DepositTransactionResponse
from dtos.response.TransferTransactionResponse import TransferTransactionResponse
from dtos.response.WithdrawalTransactionResponse import WithdrawalTransactionResponse


class WalletServiceInterface(ABC):

    @abstractmethod
    def deposit(self, deposit_request: DepositRequest) -> DepositTransactionResponse:
        pass

    @abstractmethod
    def withdraw(self, withdrawal_request: WithdrawalRequest) -> WithdrawalTransactionResponse:
        pass

    @abstractmethod
    def transfer(self, transfer_request: TransferRequest) -> TransferTransactionResponse:
        pass

    @abstractmethod
    def check_balance(self, account_number, password):
        pass
