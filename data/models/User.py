class User:

    def __init__(self):
        self.__balance = 0.0
        self.__userId = 0
        self.__phone_number = ""
        self.__first_name = ""
        self.__last_name = ""
        self.__account_number = ""
        self.__user_name = ""
        self.__password = ""

    def set_phone_number(self, phone_number):
        self.__phone_number = phone_number

    def get_phone_number(self):
        return self.__phone_number

    def get_user_id(self):
        return self.__userId

    def set_user_id(self, user_id):
        self.__userId = user_id

    def get_first_name(self):
        return self.__first_name

    def set_first_name(self, first_name):
        self.__first_name = first_name

    def get_last_name(self):
        return self.__last_name

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

    def get_balance(self):
        return self.__balance

    def __str__(self):
        return f"First name: {self.__first_name}\n" \
               f"Last name:  {self.__last_name}\n" \
               f"Account Number: {self.__account_number}\n" \
               f"User name: {self.__user_name}\n" \
               f"User Id: {self.__userId}\n" \
               f"Balance: {self.__balance}"
