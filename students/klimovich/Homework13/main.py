import func
import exceptions


while True:
    a = input('Введите первое число: ')
    b = input('Введите второе число: ')
    print('Выберите действие:\n'
          ' 1. Умножение\n'
          ' 2. Вычитание\n'
          ' 3. Деление\n'
          ' 4. Сложениe\n'
          ' 0. exit')
    try:
        b = int(b)
        a = int(a)
    except exceptions.IntCheck:
        print('Не является числом')
    sign = input('Введите номер действия: ')
    if sign == '1':
        print(func.Cmult(a, b))
        continue
    if sign == '2':
        print(func.Cmin(a, b))
        continue
    if sign == '3':
        try:
            print(func.Cdel(a, b))
        except exceptions.DevisionByZero:
            raise exceptions.DevisionByZero
        continue
    if sign == '4':
        print(func.Csum(a, b))
        continue
    if sign == '0':
        break