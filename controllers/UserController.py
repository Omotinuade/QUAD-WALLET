from dtos.request import RegisterRequest
from services.UserServiceInterfaceImpl import UserServiceInterfaceImpl


class UserController:
    user_service = UserServiceInterfaceImpl()

    def register_user(self, request: RegisterRequest):
        try:
            return self.user_service.register_user(request)
        except ValueError as ex:
            return ex.args[0]

    def login(self, request):
        try:
            return self.user_service.login_user(request)
        except ValueError as ex:
            return ex.args[0]
