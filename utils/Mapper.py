from data.models.User import User
from dtos.request import RegisterRequest


def maps(registerRequest: RegisterRequest, user: User):
    user.set_password(registerRequest.get_password())
    user.set_last_name(registerRequest.get_last_name())
    user.set_first_name(registerRequest.get_first_name())
    user.set_email_address(registerRequest.get_email_address())
    registerRequest.get_date_of_birth()
    registerRequest.get_phone_number()


class Mapper:
    pass
