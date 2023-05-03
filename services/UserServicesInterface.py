from data.models.User import User
from dtos.request.LoginRequest import LoginRequest
from dtos.request.RegisterRequest import RegisterRequest
from dtos.response import LoginResponse


class UserServicesInterface:

    def register_user(self, user_request: RegisterRequest) -> User:
        raise NotImplementedError

    def login_user(self, login_request: LoginRequest) -> LoginResponse:
        raise NotImplementedError

    def find_user_by_email_address(self, email_address) -> User:
        raise NotImplementedError

    def find_user_by_account_number(self, account_number) -> User:
        raise NotImplementedError

    def print_users(self):
        raise NotImplementedError
