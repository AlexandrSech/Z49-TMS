from exceptions import DigitException, OperationException, ZeroException


def summ(a, b):
    return a + b


def subtraction(a, b):
    return a - b


def multiply(a, b):
    return a * b


def division(a, b):
    return a / b


def number_validation():
    while True:
        a = input('Введите число: ')
        if (a[0] == '-' and a[1::].isdigit()) or a.isdigit():
            break
        else:
            raise DigitException("Вы ввели не число")
    return int(a)


def operation_validation(b, c):
    while True:
        list_operators = ['-', '+', '*', '/']
        a = input('Введите операцию + - / * : ')
        if a in list_operators:
            break
        else:
            raise OperationException("Введена не корректная операция")
    if a == '-':
        return subtraction(b, c)
    if a == '+':
        return summ(b, c)
    if a == '*':
        return multiply(b, c)
    if a == '/':
        if c != 0:
            return division(b, c)
        else:
            raise ZeroException('Деление на 0 запрещено')
