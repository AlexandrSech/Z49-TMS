class Chat:
    '''
    Хранение сообщений
    ф-ия отправки сообщений
    ф-ия вывода списка сообщений
    '''

    message_list: list

    def send_message(self, text: str):
        self.message_list.append(text)

    def get_message_list(self):
        return self.message_list