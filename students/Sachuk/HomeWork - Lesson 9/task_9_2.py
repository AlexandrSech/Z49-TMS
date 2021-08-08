# Создать lambda функцию, которая принимает на вход неопределенное
# количество именных аргументов и выводит словарь с ключами удвоенной
# длины. {‘abc’: 5} -> {‘abcabc’: 5}

def my_lambda(**kwargs):
    d = {}
    for key, value in kwargs.items():
        pow2 = lambda x: x * 2
        d[pow2(key)] = value
    return d


print(my_lambda(a='qwerty', b=1, c=4))
