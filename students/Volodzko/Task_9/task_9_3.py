"""
Создать декоратор для функции, которая принимает список чисел.
Декоратор должен производить предварительную проверку
данных -удалять все четные элементы из списка.
"""


def decoration(func):
    def wrapper(my_list):
        func(my_list)
        return [i for i in my_list if i % 2 != 0]

    return wrapper


@decoration
def func(my_list: list):
    return my_list


print(func([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
