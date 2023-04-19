from unittest import TestCase

from data.models.User import User
import WalletServiceInterfaceImpl
from data.repositories.UserRepositoryImpl import UserRepositoryImpl
from dtos.request.RegisterRequest import RegisterRequest
from services.UserServiceInterfaceImpl import UserServiceInterfaceImpl
from services.WalletServiceInterface import WalletServiceInterface


class TestWalletServicesInterfaceImplementation(TestCase):

    def test_deposit(self):
        self.register_request = RegisterRequest()
        self.user_service = UserServiceInterfaceImpl()
        self.register_request.set_phone_number("07033490197")
        self.register_request.set_email_address("kuse")
        self.user_service.register_user(self.register_request)
        self.wallet_service = WalletServiceInterfaceImpl.WalletServicesInterfaceImplementation()
        self.wallet_service.deposit("7033490197", 1000)
        print(self.user_service.find_user_by_email_address("kuse"))





