class User:

    def __init__(self, first_name: str, last_name: str, account_number: str, user_name, user_id: int,
                 password: str, phone_number: str):
        self.__userId = user_id
        self.__phone_number = phone_number
        self.__first_name = first_name
        self.__last_name = last_name
        self.__account_number = account_number
        self.__user_name = user_name
        self.__password = password

    def get_user_id(self):
        return self.__userId

    def set_user_id(self, user_id):
        self.__userId = user_id

    def get_first_name(self):
        return self.__first_name

    def set_first_name(self, first_name):
        self.__first_name = first_name

    def get_last_name(self):
        return self._last_name

    def set_last_name(self, last_name):
        self.__last_name = last_name

    def get_account_number(self):
        return self.__account_number

    def set_account_number(self, account_number):
        self.__account_number = account_number

    def get_user_name(self):
        return self.__user_name

    def set_user_name(self, user_name):
        self.__user_name = user_name

    def deposit(self, balance):
        self.balance = balance

    def get_balance(self):
        return self.balance

    def __str__(self):
        return f"First name: {self.__first_name}" \
               f"Last name:  {self.__last_name}" \
               f"Account Number: {self.__account_number}" \
               f"User name: {self.__user_name}" \
               f"User Id: {self.__userId}"
