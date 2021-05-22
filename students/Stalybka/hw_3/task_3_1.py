"""Введите число. Если это число делиться на 1000 без остатка, то выведите на
экран millennium"""

users_num = int (input('Введите число: '))
if users_num % 1000 == 0:
    print('millennium')
else:
    exit()
