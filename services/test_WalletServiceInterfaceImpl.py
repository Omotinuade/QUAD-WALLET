from unittest import TestCase

from data.models.User import User
import WalletServiceInterfaceImpl
from dtos.request.RegisterRequest import RegisterRequest
from services.UserServiceInterfaceImpl import UserServiceInterfaceImpl


class TestWalletServicesInterfaceImplementation(TestCase):

    def setUp(self) -> None:
        self.user_service = UserServiceInterfaceImpl()
        self.register_request = RegisterRequest()
        self.register_request.set_first_name("Joshua")
        self.register_request.set_last_name("Oluwakuse")
        self.register_request.set_phone_number("07033490197")
        self.register_request.set_email_address("kuse")
        self.register_request.set_password("1234")
        self.wallet_service = WalletServiceInterfaceImpl.WalletServicesInterfaceImplementation()

    def test_deposit(self):
        self.user_service.register_user(self.register_request)
        print(self.wallet_service.deposit("7033490197", 1000))
        self.assertEqual(1000, self.user_service.find_user_by_account_number("7033490197").get_balance())

    def test_withdrawal(self):
        self.user_service.register_user(self.register_request)
        self.wallet_service.deposit("7033490197", 10000)
        self.wallet_service.withdraw("7033490197", 5000, "1234")
        self.assertEqual(5000, self.user_service.find_user_by_account_number("7033490197").get_balance())

    def test_transfer(self):
        self.register_request = RegisterRequest()
        self.register_request.set_phone_number("07033490197")
        self.register_request.set_email_address("kuse")
        self.register_request.set_password("1234")
        self.user_service.register_user(self.register_request)

        self.register_request2 = RegisterRequest()
        self.register_request2.set_phone_number("08033490197")
        self.register_request2.set_email_address("josh")
        self.register_request2.set_password("12345")
        self.user_service.register_user(self.register_request2)

        self.wallet_service.deposit("8033490197", 2000)

        self.assertEqual(2000, self.wallet_service.check_balance("8033490197", "12345"))
