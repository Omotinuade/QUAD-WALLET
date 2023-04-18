class RegisterResponse:
    def __init__(self):
        self.__first_name = ""
        self.__last_name = ""
        self.__email_address = ""
        self.__date_of_birth = ""
        self.__phone_number = ""
        self.__BVN = ""
        self.__account_number = ""

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

    def set_account_number(self, account_number):
        self.__account_number = account_number

    def get_account_number(self):
        return self.__account_number

    def __str__(self):
        return f"""
        Welcome to Quad Wallet!
        Account Number: {self.__account_number}
        Name: {self.__first_name} '+'{self.__last_name}
        Email Address: {self.__email_address}'
        Phone Number: {self.__phone_number}        
        """
