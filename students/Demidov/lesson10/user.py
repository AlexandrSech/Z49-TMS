from chat import Chat 

class User(Chat):
    '''
    Хранение имени пользователя
    отправить сообщение
    получить список сообщений
    '''

    user_name: str

    def __init__(self, user_name):
        self.user_name = user_name
        self.message_list = []