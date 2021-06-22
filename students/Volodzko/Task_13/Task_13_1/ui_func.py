from func import my_sum, my_dif, my_mul, my_division
from exceptions import MyValueException

"""Пользовательский интерфейс"""


def ui_function():
    print("Вас приветствует программа колькулятор!!!")
    while True:
        """Проверка на тип входных данных, так как isdigit 
        принимет минус как строку, то сначала проверяем является ли
        строка числом без первого символа"""
        try:
            x = input("Введите число x: ")
            if len(x) > 1:
                if not x[1:].isdigit():
                    raise MyValueException("Введено не число!")  # Генерируется собственное исключение
                else:
                    x = int(x)
            else:
                if not x.isdigit():
                    raise MyValueException("Введено не число!")  # Генерируется собственное исключение
                else:
                    x = int(x)

            y = input("Введите число y: ")
            if len(y) > 1:
                if not y[1:].isdigit():
                    raise MyValueException("Введено не число!")
                else:
                    y = int(y)
            else:
                if not y.isdigit():
                    raise MyValueException("Введено не число!")
                else:
                    y = int(y)

            # Меню калькулятора
            disp = input("Введите действие которое хотите выполнить:"
                         "\n+ : сложение\n- : вычитание\n* : умножение\n"
                         "/ : деление\n0 : выход из программы\n>>> ")
            if disp == "+":
                print(my_sum(x, y))
            elif disp == "-":
                print(my_dif(x, y))
            elif disp == "*":
                print(my_mul(x, y))
            elif disp == "/":
                print(my_division(x, y))
            elif disp == "0":
                print("Вы вышли из программы!")
                break
            else:
                print("Указан неверный тип операции")

        except MyValueException as ex:
            print(ex)
