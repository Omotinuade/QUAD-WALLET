import sys
import tkinter as tk
from tkinter import messagebox, simpledialog
import re

from controllers.UserController import UserController
from controllers.WalletController import WalletController

from dtos.request.DepositRequest import DepositRequest

from dtos.request.LoginRequest import LoginRequest
from dtos.request.RegisterRequest import RegisterRequest
from dtos.request.TransferRequest import TransferRequest
from dtos.request.WithdrawalRequest import WithdrawalRequest

user_controller = UserController()
account_controller = WalletController()


def input_collector(prompt):
    root = tk.Tk

    collect_input = tk.simpledialog.askstring(title="Quad-Wallet", prompt=prompt)
    return collect_input


def display(prompt):
    messagebox.showinfo("Quad Wallet Africa", prompt)


def register_page():
    page = """
      WELCOME TO Quad-WALLET
    =========================
    1. Login
    2. Create Account
    3. Exit Application
    ========================="""
    user_input = input_collector(page)

    if user_input == "1":
        login()
    elif user_input == "2":
        create_account()
    elif user_input == "3":
        exit_application()
    else:
        register_page()


def login():
    login_request = LoginRequest()
    email = input_collector("Enter Your Email Address: ")
    password = input_collector("Enter Your Password: ")
    login_request.set_email_address(email)
    login_request.set_password(password)
    login_response = user_controller.login(login_request)
    display(login_response)
    if login_response is True:
        home_page()
    else:
        register_page()


def create_account():
    register_user = RegisterRequest()
    first_name = input_collector("Enter Your First Name: ")
    last_name = input_collector("Enter Your Last Name: ")
    email = input_collector("Enter Your Email: ")
    while True:
        phone_number = input_collector("Enter your valid Phone Number")
        if validate_nigerian_phone_number(phone_number):
            break
        else:
            display("Invalid Phone Number. Please Enter a Valid Nigerian Phone Number.")
    password = input_collector("Create A Password: ")
    register_user.set_first_name(first_name)
    register_user.set_last_name(last_name)
    register_user.set_email_address(email)
    register_user.set_phone_number(phone_number)
    register_user.set_password(password)

    response = user_controller.register_user(register_user)
    display(response)
    register_page()


def exit_application():
    display("Thank You For Banking with Quad-Wallet Africa")
    sys.exit()


def home_page():
    home = """
    =============================
    1. Deposit
    2. Withdraw
    3. Transfer
    4. Check Balance
    5. Logout
    =============================="""
    user_input = input_collector(home)
    if user_input == "1":
        deposit()
    elif user_input == "2":
        withdraw()
    elif user_input == "3":
        transfer()
    elif user_input == "4":
        check_balance()
    elif user_input == "5":
        register_page()
    else:
        print("Wrong Input! Enter A Valid Input")
    home_page()


def deposit():
    account_number = input_collector("Enter Your Account Number: ")
    amount = float(input_collector("Enter Amount: "))

    deposit_request = DepositRequest(account_number, amount)
    response = account_controller.deposit(deposit_request)
    display(response)
    home_page()


def withdraw():
    account_number = input_collector("Enter Your Account Number: ")
    amount = float(input_collector("Enter The Amount You want to Withdraw: "))
    password = input_collector("Enter Your Password: ")

    withdrawal_request = WithdrawalRequest(account_number, amount, password)
    response = account_controller.withdraw(withdrawal_request)
    display(response)

    home_page()


def transfer():
    sender_account_number = input_collector("Enter Sender's Account: ")
    receiver_account_number = input_collector("Enter Receiver's Account Number: ")
    amount = float(input_collector("Enter Amount: "))
    password = input_collector("Enter Your Password: ")
    remark = input_collector("Add A Remark: ")

    transfer_request = TransferRequest(sender_account_number, receiver_account_number, amount, password)
    response = account_controller.transfer(transfer_request)
    display(response)

    home_page()


def check_balance():
    account_number = input_collector("Enter Account Number: ")
    password = input_collector("Enter Password: ")
    response = account_controller.check_balance(account_number, password)
    display(response)
    home_page()


def validate_nigerian_phone_number(phone_number):
    pattern = r"^(080|081|090|070|091)\d{8}$"
    return bool(re.match(pattern, phone_number))


def validate_email_address(email):
    pat = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return bool(re.match(pat, email))


if __name__ == '__main__':
    register_page()
