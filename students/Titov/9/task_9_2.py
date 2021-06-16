"""Создать lambda функцию, которая принимает на вход неопределенное
количество именных аргументов и выводит словарь с ключами удвоенной
длины. {‘abc’: 5} -> {‘abcabc’: 5}"""

def foo(slov):
    slov_1 = {}
    for i in slov:
        j = lambda x: str(x) * 2
        print(j(i))
        slov_1[j(i)] = slov[i]
    return slov_1
slov = {'abc': 5, 65: 'la90d'}
m = foo(slov)
print(m)