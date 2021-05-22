# Дано число. Найти сумму и произведение его цифр.
while True:
    number = input('Please, enter the number: ')
    if number.isdigit():
        sum = 0
        multiply = 1
        for i in number:
            sum += int(i)
            multiply *= int(i)
        print(sum)
        print(multiply)
    else:
        print('You enter not number')
