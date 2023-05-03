from abc import ABC, abstractmethod
from typing import List

from data.models.User import User


class UserRepository(ABC):

    @abstractmethod
    def count(self) -> int:
        pass

    @abstractmethod
    def save_user(self, user: User) -> User:
        pass

    @abstractmethod
    def find_by_id(self, user_id: int) -> User:
        pass

    @abstractmethod
    def delete_by_account_number(self, account_number: str) -> None:
        pass

    @abstractmethod
    def delete_by_id(self, user_id: int):
        pass

    @abstractmethod
    def find_all(self) -> List[User]:
        pass

    @abstractmethod
    def find_by_email_address(self, email_address: str) -> User:
        pass

    @abstractmethod
    def find_by_account_number(self, account_number: str) -> User:
        pass