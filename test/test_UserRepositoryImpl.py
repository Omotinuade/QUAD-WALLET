from unittest import TestCase
from models.User import User
from repositories.UserRepositoryImpl import UserRepositoryImpl


class Test(TestCase):
    def setUp(self):
        self.userRepository = UserRepositoryImpl()
        self.user = User()

    def test_save_user_will_show_user_saved(self):
        saved_user = self.userRepository.save_user(self.user)
        self.assertEqual(1, self.userRepository.count())

    def test_save_one_user_id_of_user_will_be_one(self):
        saved_user = self.userRepository.save_user(self.user)
        print(saved_user)
        print(self.user.get_user_id())
        self.assertEqual(1, self.user.get_user_id())

    def test_user_can_be_found_by_id(self):
        saved_user = self.userRepository.save_user(self.user)
        self.assertEqual(1, saved_user.get_user_id())
        find_user = self.userRepository.find_by_id(1)
        self.assertEqual(find_user, saved_user)

    def test_if_twoUser_areSaved_withThe_sameId_countWill_beOne(self):
        saved_user1 = self.userRepository.save_user(self.user)
        self.assertEqual(1, saved_user1.get_user_id())
        self.userRepository.save_user(saved_user1)
        saved_user1.set_user_name("Shitty Guy")
        self.assertEqual(1, self.userRepository.count())

    def test_delete_user_byAccount_number(self):
        saved_user = self.userRepository.save_user(self.user)
        self.assertEqual(1, self.userRepository.count())
        self.userRepository.delete_by_id(1)
        self.assertEqual(0, self.userRepository.count())
