'''
1) Написать программу, в которой вводятся два операнда Х и Y и знак операции sign (+, –, /, *).
Вычислить результат Z в зависимости от знака. Предусмотреть реакции на возможный неверный знак операции,
а также на ввод Y=0 при делении. Организовать возможность многократных вычислений без перезагрузки
программа (т.е. построить бесконечный цикл). В качестве символа прекращения вычислений принять ‘0’
(т.е. sign='0').
'''


while True:
    print('\nEnter values and a math sign ("+", "-", "*" or "/".) Print "exit" to terminate the program.\n')

    x = input('Enter X:\n') # Ввод и проверка ввода X
    if x == 'exit':
        break

    try:
        x = float(x)
    except: ValueError

    if type(x) != float:
        print('X must be a number!')
        continue



    y = input('Enter Y:\n') # Ввод и проверка ввода Y
    if y == 'exit':
        break

    try:
        y = float(y)
    except: ValueError

    if type(y) != float:
        print('Y must be a number!')
        continue


    sign = input('Enter a math sign ( +, -, *, /:)\n')  # Ввод и проверка ввода sign
    if sign == 'exit' or sign == '0':
        break

    if sign == '+':
        print(str(x + y) + '\n\n***')
    elif sign == '-':
        print(str(x - y) + '\n\n***')
    elif sign == '*':
        print(str(x * y) + '\n\n***')
    elif sign == '/':
        if y == 0:
            print("Error: You can't divide by zero!")
            continue
        else: print(str(x / y) + '\n\n***')
    else: print('\nError! Sign must be "+", "-", "*" or "/".\n\n***')
