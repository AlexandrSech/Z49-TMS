result = 0
while True:
    x = input('Enter number 1\n')
    y = input('Enter number 2\n')
    sign = input('Enter an operand. Enter 0 (zero) to exit\n')
    if x.isdigit():
        x = float(x)
    else:
        print('Error on the first number: try to enter only numbers')
    if y.isdigit():
        y = float(y)
    else:
        print('Error: try to enter only numbers')
    if sign == '+':
        print(x + y)
    elif sign == '-':
        print(x - y)
    elif sign == '*':
        print(x * y)
    elif sign == '/':
        if y == 0:
            print('Division by zero, try again')
        print(x / y)
    elif sign == '0':
        exit()
    else:
        print('Error: try to enter only +, -, *, /')
