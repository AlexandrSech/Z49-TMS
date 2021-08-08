""" Написать калькулятор. Программа должна содержать 4 функции
принимающие два аргумента и возвращающие результаты сложения,
вычитания, умножения и деления. Реализовать пользовательский
интерфейс с бесконечным циклом. Добавить валидацию входных данных.
Программа должна состоять из четырех файлов(main.py, func.py, ui_func.py
exceptions.py). [my-oop-t05]"""

from exceptions import *


def number_check():
    while True:
        a = input('Введите число: ')
        if (a[0] == '-' and a[1::].isdigit()) or a.isdigit():
            break
        else:
            print("Вы ввели не число")
    return int(a)


def summ(a, b):
    return "{} + {} = {}".format(a, b, a + b)


def diff(a, b):
    return "{} - {} = {}".format(a, b, a - b)


def multi(a, b):
    return "{} * {} = {}".format(a, b, a * b)


def divide(a, b):
    try:
        if b == 0:
            raise MyZeroDivision("На ноль делить нельзя")
        else:
            return "{} / {} = {}".format(a, b, a / b)
    except MyZeroDivision as ex:
        return ex
