def foo2(foo):
    def wrapper(*args):
        my_list = foo(*args)
        l = 0
        for i in my_list:
            if l % 2 == 1:
                my_list.remove(i)
                l += 1
            else:
                l += 1
        return my_list
    return wrapper


def reverse_args(foo):
    def inner(*args):  # фактически вызываемая после декорирования функция
        return foo(*args)[::-1]  # вызываем с теми же args, реверсим, возвращаем
    return inner

@reverse_args
def foo(*a):
    my_list = []
    for i in range(len(a)):
        my_list.append(a[i])
    return my_list




print(foo(1, 21, 21, 22, 1, 31, 31, 31))
