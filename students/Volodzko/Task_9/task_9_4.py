"""
Создать универсальный декоратор, который меняет
порядок аргументов в функции на противоположный.
"""


def decoration(func):
    def wrapper(*args):
        res = reversed(args)  # Разворачиваем аргументы функции
        return func(*res)

    return wrapper


@decoration
def func(*args):
    return args


print(func(1, 2, 3))  # Проверка: на консоли доллжны быть аргументы в обратном порядке


def power(x, y, z):  # Проверка функции без декоратора
    print(x * y + z)


power(2, 3, 4)  # Результат должен быть равен 10


@decoration
def power2(x, y, z):  # Проверка функции c декоратором
    print(x * y + z)


power2(2, 3, 4)  # Результат должен быть равен 14
