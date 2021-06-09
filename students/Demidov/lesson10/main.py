import chat
import user

user1 = user.User('alex')

user1.send_message('hey, im alex!')
user1.send_message('hey, im alex!')
user1.send_message('hey, im alex!')
user1.send_message('hey, im alex!')
user1.send_message('hey, im alex!')
user1.send_message('hey, im alex!')

r = user.get_message_list()
print(r)