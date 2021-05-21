import random

print(random.randint(1, 13))




exit()

def foo(*arg):
    print(arg)


foo(1,2,3,4,5,7,8,0,'asdvasfdv',8,7,5,4,3,2)
foo()
foo('hello')


def foo2(arg=''):
    print(arg)



exit()

def foo(a1='', a2=0, a3=True):
    if a3:
        print(a1)
        print(a2)


foo(a3=True, a1='hello', a2=42)


exit()


def my_print(*items, end=' '):
    for i in items:
        print(i, end=end)
    print()

my_print(1, 2,3,56,7, end='__')

exit()

def foo(a1='', a2=0, a3=True):
    print(a1)
    print(a2)
    print(a3)


foo(a3=False, a1='hello', a2=42)

exit()

def to_dict(**my_d):
    return my_d


d = to_dict(a1=1, a2=2, a3=True)
print(type(d), d)


exit()

def foo(*xyz):
    for i in xyz:
        print(i)
    print()

foo(1)
foo(1, 2)
foo(1, 2, 5, 2, 'sdfgsf', True)
foo()



exit()

def foo():
    print('start')
    def bar():
        print('123')
    print('end')
    return 'sdfvs'

foo()

exit()

def oper(x:int, y: int, operand: str) -> int:
    if operand == '/' and y == 0:
        print('Divizion by ZERO is wrong!')
        return None
    chooser = {
        '+': x + y,
        '-': x - y,
        '*': x * y,
        '/': x / y,
    }
    if operand in chooser:
        return chooser[operand]
    else:
        print('Вы ввели неправильное значение операнда!\nПожалуйста, введите из списка доступных: {}'.format(chooser.keys()))


print(oper(1, 2, '+'))
print(oper(4, 2, '*'))

print(oper(2, 5, '**'))

exit()

def operationer(x: int, y: int, operand: str) -> int:
    if operand == '+':
        return x + y
    elif operand == '-':
        return x - y
    else:
        return "ERROR"


n = operationer(1, 2, '+')
print(n)
n = operationer(10, 201, '-')
print(n)


# + - * /

exit()

def foo(x, y, z, a1=''):
    print('X = {}'.format(x))
    print('Y = {}'.format(y))
    print('Z = {}'.format(z))
    if a1:
        print('a1 = {}'.format(a1))


d = {'x': 1, 'y': 31415, 'z': 42}

foo(1, 31415, 42)
foo(3, 666, 12321)
print()
foo(1, 31415, 42, a1='AWESOME')




exit()

def foo(obj: str):
    if type(obj) == str:
        print(type(obj), obj, len(obj))
    elif type(obj) == list:
        print(obj.pop(0))
        print(obj)
    else:
        print(obj)


foo()








exit()

import random

print(random.randint(1, 13))

exit()

# Написать программу, в которой вводятся два операнда Х и Y и знак операции
# sign (+, –, /, *). Вычислить результат Z в зависимости от знака. Предусмотреть
# реакции на возможный неверный знак операции, а также на ввод Y=0 при
# делении. Организовать возможность многократных вычислений без перезагрузки
# программа (т.е. построить бесконечный цикл). В качестве символа прекращения
# вычислений принять ‘0’ (т.е. sign='0').


# главный цикл
while True:
    while True: # ввод первого числа
        x = input('Enter the number_1: ')
        if x.isdigit():
            x = int(x)
            break
        else:
            print('Please, enter only number')
    while True:
        y = input('Enter the number_2: ')
        if y.isdigit():
            y = int(y)
            break
        else:
            print('Please, enter only number')
    while True:
        z = input('Enter the operand: ')
        if z == '0':
            print("You are logged out of the current session of calculate")
            break
        elif z == '+':
            print('{} {} {} = {}'.format(x, z, y, (x + y)))
            break
        elif z == '-':
            print('{} {} {} = {}'.format(x, z, y, (x - y)))
            break
        elif z == '*':
            print('{} {} {} = {}'.format(x, z, y, (x * y)))
            break
        elif z == '/':
            if y != 0:
                print('{} {} {} = {}'.format(x, z, y, (x / y)))
                break
            else:
                print('Division by ZERO (0) is not possible')
                break
        else:
            print('Please, enter the + - * /')



exit()

def my_append(l, obj):
    result = []
    for i in l:
        result.append(i)
    result.append(obj)
    return result
my_list = [1,2,3,5,6,]
print(my_list)

my_list = my_append(my_list, 'abcde')
print(my_list)



exit()

def foo(a ,b ,c):
    i = 0
    print(ii)
    return 1


ii = 1

foo()
print(i)




exit()

l = [1,2,3,4,5,]

print(l.append(7))


def my_append(l, obj):
    return l + obj

exit()


def my_len(obj):
    counter = 0
    for _ in obj:
        counter += 1
    return counter


result = my_len([1,2,3,4,5,])
result = my_len('hello joe')
result = my_len({'key': 'value', 'name': 'Ace'})
print('count = {}'.format(result))
