from abc import ABC, abstractmethod

from data.models.User import User


class WalletRepositoryInterface(ABC):
    @abstractmethod
    def create_new_user(self, user: User) -> User:
        pass

    @abstractmethod
    def find_user_by_id(self, user_id: int) -> User:
        pass

    @abstractmethod
    def find_user_by_account_number(self, account_number: str) -> User:
        pass

    @abstractmethod
    def delete_user_by_id(self, user_id):
        pass
