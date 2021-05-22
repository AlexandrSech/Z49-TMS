
print('Ноль завершит программу!')
z = 0
while True:
    print('Введите знак(+, -, /, *) или 0 для прекращения программы: ')
    sign = input()
    if sign == "0":
        break
    if ('+' in sign) or ('-' in sign) or ('/' in sign) or ('*' in sign):
        x = float(input('Введите X: '))
        y = float(input('Введите Y: '))
        if sign == '+':
            print(x + y)
        elif sign == '-':
            print(x - y)
        elif sign == '/':
            if y != '0':
                print(x / y)
            else:
                print('Деление на ноль!')
        elif sign == '*':
            print(x * y)
    else:
        print('Неверный знак операции!')







