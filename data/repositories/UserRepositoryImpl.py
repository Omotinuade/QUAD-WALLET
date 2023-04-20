from abc import ABC
from typing import List, Any

from models import User
from repositories.UserRepository import UserRepository


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
        return None

    def find_by_user_name(self, user_name: str) -> List[User]:
        for user in self.users:
            if user.get_user_name().__eq__(user_name):
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

    def find_by_account_number(self, account_number: str) -> None:
        for user in self.users:
            if user.get_account_number() == account_number:
                return user
        else:
            return None

    def find_all(self) -> List[User]:
        return self.users
