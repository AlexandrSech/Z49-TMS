# Создать универсальный декоратор,
# который меняет порядок аргументов в функции на противоположный.

def correct_reverse(func):
    def inner(*args):
        revers = reversed(args)
        return func(*revers)
    return inner


@correct_reverse
def take_arguments(*args):
    return args


print(take_arguments(1, 2, 3, 4, 5, 'q', 'w', [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 'qwerty'))
