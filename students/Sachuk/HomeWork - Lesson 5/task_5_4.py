# Для заданного числа N составьте программу вычисления суммы
# S=1+1/2+1/3+1/4+...+1/N, где N – натуральное число. [02-3.2-ML21]

while True:
    x = input('Please, Enter the number > 0: ')
    if x.isdigit() and int(x) > 0:
        x = int(x)
        sum = 0
        for i in range(1, x+1):
            sum +=(1/i)
        print(sum)
    else:
        print('You enter not number or number not more 0. Please, enter the number > 0!')
