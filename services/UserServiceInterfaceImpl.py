from abc import ABC

from data.models.User import User
from dtos.request.LoginRequest import LoginRequest
from dtos.request.RegisterRequest import UserRequest
from dtos.response import LoginResponse
from dtos.response.RegisterResponse import UserResponse
from services.UserServicesInterface import UserServicesInterface
from utils.Mapper import Mapper




class UserServiceInterfaceImpl(UserServicesInterface):
    user_repo = UserRepositoryImpl()
    mapper = Mapper()


def register_user(self, user_request: UserRequest) -> UserResponse:
    if self.find_user_by_email_address(user_request.get_email_address()) is not None:
        raise ValueError("User already Exist")
    else:
        return user_repo.saveUser(mapper.map)


def find_user_by_email_address(self, user_request: UserRequest) -> UserResponse:
    user_response = self.user_repo.find_user_by_email_address(user_request.get_email_address())
    if not user_response:
        raise ValueError("User does not exist")
    else:
        return user_response


def login_user(self, login_request: LoginRequest) -> LoginResponse:
    user_response = self.user_repo.find_user_by_email_address(login_request.get_email_address())
    if user_response is None:
        raise ValueError("User does not Exist")
    if user_response.get_password != login_request.get_password():
        raise ValueError("Password incorrect")
    else:
        return user_response
