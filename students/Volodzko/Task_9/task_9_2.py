"""
Создать lambda функцию, которая принимает на вход неопределенное
количество именных аргументов и выводит словарь с ключами
удвоенной длины. {‘abc’: 5} -> {‘abcabc’: 5}
"""

my_dict_power = lambda **args: {"{} : {}".format(k * 2, v) for k, v in args.items()}
print(my_dict_power(a=1, b=2, c=3, d=4))
