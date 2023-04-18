from data.repositories.WalletRepositoryInterface import WalletRepositoryInterface


class WalletRepositoryImpl(WalletRepositoryInterface):
    def __init__(self):
        self.user_list = []
        self.id = 0

    def create_new_user(self, user):
        self.id += 1
        self.user_list.append(user)

    def find_user_by_id(self, user_id):
        for user in self.user_list:
            if user.get_user_id() == user_id:
                return user
        else:
            return None

    def find_user_by_account_number(self, account_number):
        for user in self.user_list:
            if user.get_account_number == account_number:
                return user
            else:
                return None

    def delete_user_by_id(self, user_id):
        for user in self.user_list:
            if user.get_user_id == id:
                self.user_list.remove(user)
                break
