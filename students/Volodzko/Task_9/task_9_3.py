"""
Создать декоратор для функции, которая принимает список чисел.
Декоратор должен производить предварительную проверку
данных -удалять все четные элементы из списка.
"""


def decoration(func):
    def wrapper(my_list):
        my_list2=[]
        for i in my_list:
            try:
                i = int(i)
            except:
                my_list2.append(i)
                continue
            if i %2 != 0:
                my_list2.append(i)
        result = func(my_list2)
        return result

    return wrapper


@decoration
def func(my_list: list):
    return my_list


print(func([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(func(["a",2,3,True,5]))
