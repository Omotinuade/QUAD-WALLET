from abc import ABC
from typing import List, Any

from data.models.User import User
from data.repositories.UserRepository import UserRepository

count: int = 0


def generate_user_id():
    return count + 1


class UserRepositoryImpl(UserRepository, ABC):
    users = []

    def __init__(self):
        self.count = 0

    def save_user(self, user: User) -> User:
        if user.get_user_id() == 0:
            user.set_user_id(generate_user_id())
            self.users.append(user)
            self.count += 1
            return user

    def find_by_id(self, user_id: int) -> Any | None:
        for user in self.users:
            if user.get_user_id() == user_id:
                return user
            else:
                return None

    def count(self) -> int:
        return self.count

    def find_user_by_email_address(self, email_address: str) -> Any | None:
        for user in self.users:
            if user.get_email_address().casefold(email_address):
                return user
            else:
                return None

    def delete_by_account_number(self, account_number: str) -> None:
        for user in self.users:
            if user.get_account_number() == account_number:
                self.users.remove(user)

    def find_by_account_number(self, account_number: str) -> Any | None:
        for user in self.users:
            if user.get_account_number() == account_number:
                return user
            else:
                return None

    def find_all(self) -> List[User]:
        return self.users
