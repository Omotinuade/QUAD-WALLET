class LoginRequest:
    def __init__(self):
        self.__email_address = ""
        self.__password = ""

    def set_password(self, password):
        self.__password = password

    def get_password(self):
        return self.__password

    def set_email_address(self, email_address):
        self.__email_address = email_address

    def get_email_address(self):
        return self.__email_address
