class Chat:
    '''хранение сообений, ф-ия отправки сообщений,ф-ия вывода списка'''
    message_list: list

    def send_message(self, text: str):
        self.message_list.append(text)

    def get_message_list(self):
        return self.message_list