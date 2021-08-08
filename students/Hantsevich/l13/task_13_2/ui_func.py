""" Выполнить задание 1 с использованием класса Math. Класс принимает в
качестве аргументов два числа. Определить 4 метода(сложение,
вычитание, умножение, деление). Добавить валидацию входных данных.
Программа должна состоять из четырех файлов(main.py, classes.py,
ui_func.py exceptions.py). [my-oop-t06]"""

from exceptions import *
from classes import *


def calc():
    print("Вас приветствует... Пам-пам-пам... калькулятор -_-")
    while True:
        a = number_check()
        b = number_check()
        d = My_Math(a, b)
        lst = ['-', '+', '*', '/']
        i = input('Введите операцию (+ - / * ) : ')
        if i in lst:
            if i == '+':
                print(d.sum)
            elif i == '-':
                print(d.diff)
            elif i == '*':
                print(d.multi)
            elif i == '/':
                print(d.divide)
        else:
            print("Неверная операция")
