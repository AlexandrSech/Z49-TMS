l = [1, 5.85, {'ok': 'okay'}, [1, 2, 3], True]

print("Цикл начал работу")
for iterator in l:
    print('iterator = {}'.format(iterator))
    if type(iterator) == dict:
        print(iterator.items())
        for k, v in iterator.items():
            print('{}-->{}'.format(k, v))
else:
    print("Цикл закончил работу")


print('-------------------------')

user_choose  = ''
to_exit = 'exit'
menu = '1. asdfe\n2. sddf\n3.dssdds\nexit - to exit\nchoose: '

while user_choose != to_exit:
    user_choose  = input(menu)
    if user_choose == '1':
        print('Ypu choose 1 element')
    elif user_choose == '2':
        print('start')
        continue
        print('end')
    elif user_choose == 'exit':
        break
    else:
        print('please, print correct item')
else:
    print('end whule')