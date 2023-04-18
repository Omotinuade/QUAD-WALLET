class Wallet:
    def __init__(self, wallet_id):
        self.__wallet_id = wallet_id
        self.__user_list = []

    def set_user_list(self, user_list):
        self.__user_list = user_list

    def get_user_list(self):
        return self.__user_list

    def set_wallet_id(self, wallet_id):
        self.__wallet_id = wallet_id

    def get_wallet_id(self):
        return self.__wallet_id

