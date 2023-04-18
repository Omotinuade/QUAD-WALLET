from abc import ABC, abstractmethod

from dtos.request.RegisterRequest import UserRequest
from dtos.response.RegisterResponse import UserResponse


class UserServicesInterface(ABC):
    @abstractmethod
    def register_user(self, user_request: UserRequest) -> UserResponse:
        pass

    @abstractmethod
    def login_user(self, user_request: UserRequest) -> UserResponse:
        pass

    @abstractmethod
    def find_user(self, user_request: UserRequest) -> UserResponse:
        pass

