from unittest import TestCase

from data.models.User import User
from data.repositories.UserRepositoryImpl import UserRepositoryImpl


class TestUserRepository(TestCase):

    def setUp(self) -> None:
        self.repository = UserRepositoryImpl()
        self.user = User()
        self.user.set_email_address("benten")
        self.user.set_password("2121")
        self.user.set_phone_number("08138732503")
        self.user.set_account_number(self.user.get_phone_number()[1:])

    def test_save_user(self):
        result = self.repository.save_user(self.user)
        self.assertEquals(1, result.get_user_id())
        self.assertEquals(result.get_email_address(), self.user.get_email_address())

    # def test_find
