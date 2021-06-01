'''Написать программу, в которой вводятся два операнда Х и Y и знак операции
sign (+, –, /, *). Вычислить результат Z в зависимости от знака. Предусмотреть
реакции на возможный неверный знак операции, а также на ввод Y=0 при
делении. Организовать возможность многократных вычислений без перезагрузки
программа (т.е. построить бесконечный цикл). В качестве символа прекращения
вычислений принять ‘0’ (т.е. sign='0').'''

while True:
    X = input('Please, enter the first number\n')
    if not X.isdigit():
        print('What you entered is not a number, please enter a number!')
        continue
    else:
        X = int(X)
    Y = input('Please, enter the second number\n')
    if not Y.isdigit():
        print('What you entered is not a number, please enter a number!')
        continue
    else:
        Y = int(Y)
    Z = input('''Please enter one of the following operands: +  -  *  /
    Enter 0 if you wanna stop the program\n''')
    if Z == '+':
        print(X, Z, Y, '=', X + Y)
    elif Z == '-':
        print(X, Z, Y, '=', X - Y)
    elif Z == '*':
        print(X, Z, Y, '=', X * Y)
    elif Z == '/':
        if Y != 0:
            print(X, Z, Y, '=', X / Y)
        else:
            print('Division by 0 is impossible! Try entering different number')
    else:
        print('Operand is not recognised. Please enter one of the following: + - * /')

