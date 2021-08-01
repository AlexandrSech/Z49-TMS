from config import Chat

class User(Chat):
    '''отправить сообщение,получить список сообщений,хранение имени пользователя'''
    user_name: str

    def __init__(self, user_name):
        self.user_name = user_name
        self.message_list = []

