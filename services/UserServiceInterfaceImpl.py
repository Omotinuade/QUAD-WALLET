from data.models.User import User
from data.repositories.UserRepository import UserRepository
from data.repositories.UserRepositoryImpl import UserRepositoryImpl
from dtos.request.LoginRequest import LoginRequest
from dtos.request.RegisterRequest import RegisterRequest
from dtos.response import LoginResponse
from services.UserServicesInterface import UserServicesInterface


def maps(registerRequest: RegisterRequest, user: User):
    user.set_password(registerRequest.get_password())
    user.set_last_name(registerRequest.get_last_name())
    user.set_first_name(registerRequest.get_first_name())
    user.set_email_address(registerRequest.get_email_address())
    user.set_date_of_birth(registerRequest.get_date_of_birth())
    user.set_phone_number(registerRequest.get_phone_number())
    user.set_account_number(registerRequest.get_phone_number()[1:])
    return user


class UserServiceInterfaceImpl(UserServicesInterface):
    user_repo = UserRepositoryImpl()

    def register_user(self, user_request: RegisterRequest) -> User:
        if self.user_repo.find_by_email_address(user_request.get_email_address()) is not None:
            raise ValueError("User already Exist")
        else:
            user = User()
            return self.user_repo.save_user(maps(user_request, user))

    def find_user_by_email_address(self, email_address) -> User:
        user_response = self.user_repo.find_by_email_address(email_address)
        if not user_response:
            raise ValueError("User does not exist")
        else:
            return user_response

    def login_user(self, login_request: LoginRequest) -> bool:  # LoginResponse:
        user_response = self.user_repo.find_by_email_address(login_request.get_email_address())
        if user_response is None:
            raise ValueError("User not there")

        if user_response.get_password() != login_request.get_password():
            raise ValueError("Invalid email address or password")
        return True

    def find_user_by_account_number(self, account_number) -> User:
        user_response = self.user_repo.find_by_account_number(account_number)
        print("I am ", user_response)
        if user_response is None:
            raise ValueError("User does not exist")
        else:
            return user_response

    def print_users(self):
        self.user_repo.print_all_users()


