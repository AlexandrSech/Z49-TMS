x = int(input('Ввежите первое число'))
y = int(input('Введите второе число'))
while x and y != 0:
    znak = input('Введите знак')
    if znak == '+':
        print(x + y)
    elif znak == "-":
        print(x - y)
    elif znak == "/":
        print(x / y)
    elif znak == ('*'):
        print(x * y)
    elif znak == ('0'):
        print('Программа завершена')
        break
    elif znak != '+' or znak != '-' or znak != '/'  or znak != '*':
        print('Вы ввели неверный знак')

