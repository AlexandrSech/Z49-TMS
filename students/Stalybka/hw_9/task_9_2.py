'''
Создать lambda функцию, которая принимает на вход неопределенное
количество именных аргументов и выводит словарь с ключами удвоенной
длины. {‘abc’: 5} -> {‘abcabc’: 5}
'''

def foo(**kwargs):
    my_dict = {}
    for keys, values in kwargs.items():
        new_key = lambda keys: keys * 2
        my_dict[new_key(keys)] = values
    return my_dict


print(foo(abc=5, aaa=5, llc=5))
