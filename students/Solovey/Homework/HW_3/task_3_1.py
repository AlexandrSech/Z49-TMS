'''
1) Введите число. Если это число делится на 1000 без остатка,
то выведите на экран "millennium"
num = 1000
'''

num = input('Entea a number:\n')
if int(num) / 1000 == 1:
    print('Millenium')
else: print('Error')