""" Написать калькулятор. Программа должна содержать 4 функции
принимающие два аргумента и возвращающие результаты сложения,
вычитания, умножения и деления. Реализовать пользовательский
интерфейс с бесконечным циклом. Добавить валидацию входных данных.
Программа должна состоять из четырех файлов(main.py, func.py, ui_func.py
exceptions.py). [my-oop-t05]"""

from exceptions import *
from func import *


def calc():
    print("Вас приветствует... Пам-пам-пам... калькулятор -_-")
    while True:
        a = number_check()
        b = number_check()
        lst = ['-', '+', '*', '/']
        i = input('Введите операцию (+ - / * ) : ')
        if i in lst:
            if i == '+':
                print(summ(a, b))
            elif i == '-':
                print(diff(a, b))
            elif i == '*':
                print(multi(a, b))
            elif i == '/':
                print(divide(a, b))
        else:
            print("Неверная операция")
