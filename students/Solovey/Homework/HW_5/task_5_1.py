x = input('Enter X:\n')
y = input('Enter Y:\n')
sign = input('Enter a math sign ( +, -, *, /:)\n')

while True:
    try:
        float(x)
        while y:
            try:
                float(y)
                if sign == '+':
                    print(float(x) + float(y))
                elif sign == '-':
                    print(float(x) - float(y))
                elif sign == '*':
                    print(float(x) * float(y))
                elif sign == '/':
                    if float(y) == 0:
                        print('Error!')
                    else: print(float(x) / float(y))
            except ValueError:
                print('error')
    except ValueError:
        print('error')