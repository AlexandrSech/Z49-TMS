# Написать программу, в которой вводятся два операнда Х и Y и знак операции
# sign (+, –, /, *). Вычислить результат Z в зависимости от знака. Предусмотреть
# реакции на возможный неверный знак операции, а также на ввод Y=0 при
# делении. Организовать возможность многократных вычислений без перезагрузки
# программа (т.е. построить бесконечный цикл). В качестве символа прекращения
# вычислений принять ‘0’ (т.е. sign='0').


while True:
    while True:
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
