from abc import ABC, abstractmethod

from data.models.User import User
from dtos.request.LoginRequest import LoginRequest
from dtos.request.RegisterRequest import RegisterRequest
from dtos.response import LoginResponse


class UserServicesInterface(ABC):
    @abstractmethod
    def register_user(self, user_request: RegisterRequest) -> User:
        pass

    @abstractmethod
    def login_user(self, login_request: LoginRequest) -> LoginResponse:
        pass

    @abstractmethod
    def find_user_by_email_address(self, email_address)->User:
        pass

