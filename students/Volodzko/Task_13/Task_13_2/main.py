from classes import Math
from exceptions import MyValueException

"""1.Написать калькулятор. Программа должна содержать 4 функциипринимающие
два аргумента и возвращающие результаты сложения,вычитания, умножения и деления.
Реализовать пользовательскийинтерфейс с бесконечным циклом. Добавить валидацию входных данных.
Программа должна состоять из четырех файлов(main.py, func.py, ui_func.pyexceptions.py)
Задане 1 выполнено в файле Task_13_1

2. Выполнить задание 1 с использованием класса Math. Класс принимает вкачестве аргументов два числа.
Определить 4 метода(сложение,вычитание, умножение, деление). Добавить валидацию входных данных.
Программа должна состоять из четырех файлов(main.py, classes.py,ui_func.py exceptions.py)"""

if __name__ == '__main__':
    print("Вас приветствует программа колькулятор!!!")
    while True:
        """Проверка на тип входных данных, так как isdigit 
        принимет минус как строку, то сначала проверяем является ли
        строка числом без первого символа"""
        calc = Math()
        try:
            calc.x = input("Введите число x: ")
            if len(calc.x) > 1:
                if not calc.x[1:].isdigit():
                    raise MyValueException("Введено не число!")  # Генерируется собственное исключение
                else:
                    calc.x = int(calc.x)
            else:
                if not calc.x.isdigit():
                    raise MyValueException("Введено не число!")  # Генерируется собственное исключение
                else:
                    calc.x = int(calc.x)

            calc.y = input("Введите число y: ")
            if len(calc.y) > 1:
                if not calc.y[1:].isdigit():
                    raise MyValueException("Введено не число!")
                else:
                    calc.y = int(calc.y)
            else:
                if not calc.y.isdigit():
                    raise MyValueException("Введено не число!")
                else:
                    calc.y = int(calc.y)

            # Меню калькулятора
            disp = input("Введите действие которое хотите выполнить:"
                         "\n+ : сложение\n- : вычитание\n* : умножение\n"
                         "/ : деление\n0 : выход из программы\n>>> ")
            if disp == "+":
                print(calc.my_sum(calc.x, calc.y))
            elif disp == "-":
                print(calc.my_dif(calc.x, calc.y))
            elif disp == "*":
                print(calc.my_mul(calc.x, calc.y))
            elif disp == "/":
                print(calc.my_division(calc.x, calc.y))
            elif disp == "0":
                print("Вы вышли из программы!")
                break
            else:
                print("Указан неверный тип операции")

        except MyValueException as ex:
            print(ex)
