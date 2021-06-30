from MyUser import MUser

new_user = MUser('нюхач бэбры', 'http://johnray.pythonanywhere.com/')
e = 0
print(new_user.post_login())
print(new_user.get_messages())
print(new_user.send_messages(''))

r = new_user.get_messages()

menu = "Приготовь глессе:\n"\
    '1. send mess\n' \
    '2. get mess\n'\
    '3. exit\n'

for i in r:
    print(i)
#print(new_user.get_messages())
print(new_user.post_logout())