import chat
import user


my_chat = chat.Chat()
user1 = user.User('Artem')

user1.send_message('abrakadabra')
user1.send_message('abrakadabra1')
user1.send_message('abrakadabra2')
user1.send_message('abrakadabra3')
user1.send_message('abrakadabra4')

r = user1.get_message_list()
print(r)