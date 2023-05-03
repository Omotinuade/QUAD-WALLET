from abc import ABC
from typing import List, Any

from data.models.User import User
from data.repositories.UserRepository import UserRepository


class UserRepositoryImpl(UserRepository, ABC):

    def __init__(self):
        self.user_count = 0
        self.users: list[User] = []

    def generate_user_id(self):
        self.user_count += 1
        pass

    def save_user(self, user: User) -> User:
        if user.get_user_id() == 0:
            self.user_count += 1
            user.set_user_id(self.user_count)
        self.users.append(user)
        return user

    def count(self):
        return self.user_count

    def find_by_id(self, user_id: int) -> User:
        for userId in self.users:
            if userId.get_user_id() == user_id:
                return userId

    def find_by_email_address(self, email_address: str) -> User:

        for user in self.users:
            if user.get_email_address().__eq__(email_address):
                return user

    def delete_by_account_number(self, account_number: str) -> None:
        for user in self.users:
            if user.get_account_number() == account_number:
                self.users.remove(user)
                self.user_count -= 1

    def delete_by_id(self, user_id: int):
        for user in self.users:
            if user.get_user_id() == user_id:
                self.users.remove(user)
                self.user_count -= 1

    def find_by_account_number(self, account_number: str) -> User:
        for user in self.users:
            if user.get_account_number().__eq__(account_number):
                return user

    def find_all(self) -> List[User]:
        return self.users
