while True:
    number = input('Введите число: ')
    sum = 0
    mult = 1
    if number.isdigit():
        for i in number:
            sum += int(i)
            mult *= int(i)
        print('\n' + 'Сумма цифр числа:', sum, '\n' + 'Произведение цифр числа:', mult, '\n')
    else:
        print('Введите !число!')
