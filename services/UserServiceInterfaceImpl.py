from abc import ABC

from data.models.User import User
from dtos.request.RegisterRequest import UserRequest
from dtos.response.RegisterResponse import UserResponse
from services.UserServicesInterface import UserServicesInterface
from utils.Mapper import Mapper


class UserRepositoryImpl:
    def find_account_by_email_address(self, email_address)->User:
        pass

class User:
    email_address=""
    def find_user_by_email_address( self, email_address)->:
        self.email_address= email_address
    pass

class UserServiceInterfaceImpl(UserServicesInterface):
        user_repo = UserRepositoryImpl()
        mapper= Mapper()

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

