from typing import List, Any

from data.models.User import User


class UserRepository:

    def save_user(self, user: User) -> User:
        raise NotImplementedError

    def find_by_id(self, user_id: int) -> User:
        raise NotImplementedError

    def delete_by_account_number(self, account_number: str) -> None:
        raise NotImplementedError

    def find_all(self) -> List[User]:
        raise NotImplementedError

    def find_user_by_email_address(self, email_address: str) -> Any | None:
        raise NotImplementedError

    def find_by_account_number(self, account_number: str) -> List:
        raise NotImplementedError
