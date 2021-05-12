# Введите число. Если это число делиться на 1000 без остатка, то выведите на экран "millennium"

num = int(input())

if num % 1000 == 0:
    print('millennium')
else:
    print('remainder of the division {} divided on 1000 is equal {}'.format(num, num % 1000))
