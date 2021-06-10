# Создать декоратор для функции, которая принимает список чисел.
# Декоратор должен производить предварительную проверку данных -
# удалять все четные элементы из списка.


def correct_list(func):
    def inner(*args):
        result = func(*args)
        l = [i for i in result if i % 2 !=0]
        return l
    return inner


@correct_list
def list_of_numbers(l: list):
    return l


print((list_of_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])))
