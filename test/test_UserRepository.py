from unittest import TestCase
from models import User
from repositories import UserRepositoryImpl


class TestUserRepository(TestCase):

    def setUp(self) -> None:
        self.repository = UserRepositoryImpl

    user = User()
    user.set_user_name("John")
    user.

    def test_save_user(self):
        self.fail()

    def test_find
