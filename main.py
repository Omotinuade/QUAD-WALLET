import sys
import tkinter
from tkinter import Tk

from controllers.UserController import UserController
from controllers.WalletController import WalletController
from dtos.request.RegisterRequest import RegisterRequest

if __name__ == '__main__':

    user_controller = UserController()
    wallet_controller = WalletController()


    def start_app():
        print("""
                QUAD WALLET
                1>>> Register
                2>>> Login
                3>>> Find Account
                4>>>Exit Application
                """)
        input_value = input("please select: ")
        choice = input_value[0]
        if choice == '1':
            register()
        elif choice == '2':
            login()
        elif choice == '3':
            find_user()
        elif choice == '4':
            exit_application()
        else:
            print("Wrong selection")
        start_app()


    def withdraw():
        wallet_controller.withdraw()


    def transfer():
        pass


    def check_balance():
        pass


    def deposit():
        pass


    def display_after_login():
        message = input("""
                Welcome to Your Favourite Wallet
                1. >>> Deposit
                2. >>> Withdraw
                3. >>> Transfer
                4. >>> Check Balance
             """)
        choice = message[0]
        if choice == '1':
            deposit()
        elif choice == '2':
            withdraw()
        elif choice == '3':
            transfer()
        elif choice == '4':
            check_balance()


    def login():
        pass


    def find_user():
        pass


    def exit_application():
        pass

    def register():

        register_request = RegisterRequest()
        first_name = input("Enter First Name")
        register_request.set_first_name(first_name)
        last_name = input("Enter Last Name: ")
        register_request.set_last_name(last_name)
        email_address = input("Enter E-mail Address: ")
        register_request.set_email_address(email_address)
        phone_number = input("Enter Phone Number: ")
        register_request.set_phone_number(phone_number)
        date_of_birth = input("Enter Date of Birth: ")
        register_request.set_date_of_birth(date_of_birth)
        password = input("Enter Password: ")
        register_request.set_password(password)
        print(user_controller.register_user(register_request).__str__())

    # def input(prompt):
    #     return inputbox.askstring("Input", prompt)
    #
    # 
    # def login():
    #     login_request = LoginRequest()
    #     login_request.set_email_address(input("Enter Your Email Address: "))
    #     login_request.set_password(input("Enter Password: "))
    #     user_controller.login(login_request)
    # 
    #
    # def find()
    # 
    # 
    # def exit_application():
    #     sys.exit()
    # 
    # 
    # def deposit()

print(start_app())