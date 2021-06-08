'''
Создать декоратор для функции, которая принимает список чисел.
Декоратор должен производить предварительную проверку данных -
удалять все четные элементы из списка.
'''


def check(main):
    def wrapper(new_list):
        for i ,v in enumerate(new_list):
            if v % 2 == 0:
                new_list.pop(i)
        return main(new_list)
    return wrapper


@check
def main(new_list: list):
    return new_list


k = [1, 2, 3, 4, 5, 6, 7, 8, 9, 12, 13, 11, ]
print(main(k))