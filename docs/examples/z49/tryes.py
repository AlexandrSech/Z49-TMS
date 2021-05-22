









exit()

l = [1,2,3,4,5,]

for index in range(len(l) - 1):
    # l[index], l[index + 1] = l[index + 1], l[index]
    temp = l[index]
    l[index] = l[index + 1]
    l[index + 1] = temp
    print(l)

print()
l = [1,2,3,4,5,]
n = 0
while n < len(l) - 1:
    temp = l[n]
    l[n] = l[n + 1]
    l[n + 1] = temp
    n += 1
    print(l)




exit()

# типы данных
# string
ms = "123a adscasrfa awed23"
print(ms)
print(ms.split(' '))
print(ms.split(','))

text = '''text
vs
some
lines'''
text2 = 'one\ntwo\nthree'
print(type(text))
print(text2)
print(ms.splitlines())  # ms.split('\n') - the same
print(text2.splitlines())

# print(dir(ms))

simple_list = [1,2,3,4,5]
print('->'.join(map(str, simple_list)))

print(
    'Шаблон письма.\nПривет, {name}!\nКак твои дела? Слышал ты уезжаешь в отпус????'.format(name='Игорь')
)

print('Hello world! I like cheese!'.replace(' ', '_'))
print('Hello world! I like cheese!'.replace('cheese', 'vodka'))

ex1 = 'my simple text'
print(ex1)
ex1 = ex1.capitalize()
print(ex1)

print(ex1.isdigit())
print('123'.isdigit())
print('123123'.isalpha())
print(ex1)


# lists

l = [1, 'adc', True, {'name': 'foo'}, [1, 2, 3,]]
print(l)
print(l[1])
l[1] += '!'
print(l[1])
print(l)

l[4].append(6666)
print(l)
print(l[3])
print(l[3]['name'])
l[3]['age'] = 12
print(l)

print(l[1:3])

print()
print('_'*20)
print('цикл начал работу')
for iterator in [1,2,3,4,5,6,7,8,9,]:
    print('iterator = {}'.format(iterator))
else:
    print('цикл закончил работу')



print()
print('_'*20)
print('цикл начал работу')
for iterator in 'это моя строка и только я могу на нее смотреть':
    print('iterator = {}'.format(iterator))
else:
    print('цикл закончил работу')


print()
print('_'*20)
print('цикл начал работу')
for iterator in l:
    print('iterator = {}'.format(iterator))
    if type(iterator) == dict:
        print(iterator.items())
        for k, v in iterator.items():
            print('{}->{}'.format(k, v))
else:
    print('цикл закончил работу')

print()
print()
print()


user_choose = ''
to_exit = 'exit'
menu = '1. some text\n2. try continue\n3. sdcsd\nexit - to exit\nchoose: '
while user_choose != to_exit:
    user_choose = input(menu)
    if user_choose == '1':
        print('что ты тут нам  рассказываешь в пятницу вечером, мы устали, отстань от нас!!!!')
    elif user_choose == '2':
        print('start')
        continue
        print('end')
    elif user_choose == 'exit':
        break
    else:
        print('please print correct item!!!')
else:
    print('end while')






'''
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', 
'__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', 
'__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', 
'__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 
'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 
'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 
'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 
'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 
'translate', 'upper', 'zfill']'''














exit()



print(0.1 + 0.2 == 0.3)


print('65+78')

x = [12.1, 34.0]
print(list(map(str, x)))
print(len(' '.join(list(map(str, x)))))


a = 10
a = a + - + -- + 10

print(a)



print(str(.0))
s = str(2/2/2/2/2*2*2*2)*2 + str(.0)

print(s)


exit()

m = 'sdfjhvsodjfhvoashvcaisudc'
rs = str()
n = list(m)
for item in n:
    rs += item + " "
print(rs)


exit()

email = 'ksdjbfvksjldfbv@sdkfjhbsdfhbv.ndc'
if '@' in email:
    index_at = email.split('@')
    print(index_at)
if '.' in index_at[1]:
    print(index_at[-1].split('.'), len(index_at[-1].split('.')))
    if len(index_at[-1].split('.')[-1]) > 1:
        print(True)
    else:
        print(False)





exit()


import GoogleNews


gg = GoogleNews.GoogleNews(lang='ru', period='7d')
gg.search('APPLE')
rr = gg.result()
for my_dict in rr:
    for key, value in my_dict.items():
        print(key, value)
    break
    '''print(i['title'])
    print(i['date'])
    print(i['desc'])
    print(i['link'])

    print()'''



exit()

dd = {

}

print(dd)
dd['name'] = 'Totoshka'
dd['name'] = 'Alex'
dd['users'] = [1,2,3,4,5,]
dd['another_dict'] = {'name': 'ololol'}
print(dd['another_dict']['name'])

exit()

queue = []

for i in range(1000):
    queue.append(i)

while queue:
    print(queue.pop(-1))


exit()

eee = [
    (0, 1), (1, 2), (2, 3), (3, 4), (4, 5)
]



ll = [
        1,
        2,
        3,
        4,
        5
]

for index, value in enumerate(ll):
    print(index, value)
    print(ll.pop(index))
    # print(ll[index], value)
    # print(index, value)

print(ll)




exit()


x = 10
y = 10


lst = []
for i in range(x):
    lst.append([])
    # print(id(lst[i]))
    for q in range(y):
        lst[i].append(0)
'''for i in lst:
    print(i)'''

for i, ii in enumerate(lst):
    for j in range(i, y):
        # if i == j:
        lst[i][j] = 1
        #print(i,j,jj, end='   ')
    # print()


for i in lst:
    print(i)

exit()
for i in range(len(lst)):
    #print(i)
    for j in range(4):
        lst[i].append(0)

for i in lst:
    print(i)





exit()

fib_list = [0, 1,]

# for _ in range(100):
while len(fib_list) < 100:
    fib_list.append(fib_list[-1] + fib_list[-2])

print(fib_list)
