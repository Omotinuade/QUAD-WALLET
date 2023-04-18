class UserRequest:
    def __init__(self, first_name, last_name, email_address, date_of_birth, phone_number, BVN, password):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__email_address = email_address
        self.__date_of_birth = date_of_birth
        self.__phone_number = phone_number
        self.__BVN = BVN
        self.__password = password

    def set_first_name(self, first_name):
        self.__first_name = first_name

    def get_first_name(self):
        return self.__first_name

    def set_last_name(self, last_name):
        self.__last_name = last_name

    def get_last_name(self):
        return self.__last_name

    def set_email_address(self, email_address):
        self.__email_address = email_address

    def get_email_address(self):
        return self.__email_address

    def set_date_of_birth(self):
        return self.__date_of_birth

    def get_date_of_birth(self):
        return self.__date_of_birth

    def set_phone_number(self, phone_number):
        self.__phone_number = phone_number

    def get_phone_number(self):
        return self.__phone_number

    def set_password(self, password):
        self.__password = password

    def get_password(self):
        return self.__password
