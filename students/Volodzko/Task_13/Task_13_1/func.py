from exceptions import MyZeroException


def my_sum(x, y):  # Функция сложения двух чсел
    return "x + y = {}".format(x + y)


def my_dif(x, y):  # Функция вычитания двух чсел
    return "x - y = {}".format(x - y)


def my_mul(x, y):  # Функция умножения двух чсел
    return "x * y = {}".format(x * y)


def my_division(x, y):  # Функция деления двух чсел
    try:
        if y == 0:
            raise MyZeroException("Деление на ноль запрещено!")  # Генерируется собственное исключение
        else:
            return "x / y = {}".format(round(x / y, 4))
    except MyZeroException as ex:
        print(ex)
