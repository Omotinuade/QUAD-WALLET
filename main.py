import sys
import tkinter

from controllers.UserController import UserController
from controllers.WalletController import WalletController
from dtos.request.LoginRequest import LoginRequest
from dtos.request.RegisterRequest import RegisterRequest

if __name__ == '__main__':

    user_controller = UserController()
    wallet_controller = WalletController()
    def start_app():
        message = """QUAD WALLET
                        1>>> Register
                        2>>> Login
                        3>>> Find Account
                        4>>>Exit Application"""
        input_value = input(message)
        choice = input_value[0]
        if choice == '1':
            register()
        elif choice == '2':
            login()
        elif choice == '3':
            find()
        elif choice == '4':
            exit_application()
        else:
            display("Wrong selection")
        start_app()


    def withdraw():
        wallet_controller.withdraw()



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


    def display(message):
        tkinter.messagebox.showinfo(title="Information", message=message)


    def register():
        register_request = RegisterRequest()
        register_request.set_first_name(input("Enter First Name"))
        register_request.set_last_name(input("Enter Last Name: "))
        register_request.set_email_address(input("Enter E-mail Address: "))
        register_request.set_phone_number(input("Enter Phone Number: "))
        register_request.set_date_of_birth(input("Enter Date of Birth: "))
        register_request.set_password(input("Enter Password: "))
        return user_controller.register


    def input(prompt):
        return inputbox.askstring("Input", prompt)


    def login():
        login_request = LoginRequest()
        loginRequest.set_email_address(input("Enter Your Email Address: "))
        loginRequest.set_password(input("Enter Password: "))
        user_controller.login


    def find()


    def exit_application():
        sys.exit()


    def deposit()
