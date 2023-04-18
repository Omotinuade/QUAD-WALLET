class User:
    def __init__(self):
        self.__password = ""
        self.__user_id = 0
        self.__first_name = ""
        self.__last_name = ""
        self.__account_number = ""
        self.__email_address = " "
        self.__date_of_birth = ""
        self.__phone_number = ""
        self.__balance = 0

    def get_user_id(self):
        return self.__user_id

    def set_user_id(self, user_id):
        self.__user_id = user_id

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

    def get_email_address(self):
        return self.__email_address

    def set_email_address(self, email_address):
        self.__email_address = email_address

    def get_phone_number(self):
        return self.__phone_number

    def set_phone_number(self, phone_number):
        self.__phone_number = phone_number

    def get_date_of_birth(self):
        return self.__date_of_birth

    def set_date_of_birth(self, date_of_birth):
        self.__date_of_birth = date_of_birth

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        self.__balance -= amount

    def get_password(self):
        return self.__password

    def __str__(self):
        return f"First name: {self.__first_name}" \
               f"Last name:  {self.__last_name}" \
               f"Account Number: {self.__account_number}" \
               f"User name: {self.__email_address}" \
               f"User Id: {self.__user_id}"

    def set_password(self, password):
        self.__password = password
