'''
Описать функцию fact2( n ), вычисляющую двойной факториал :n!! =
1·3·5·...·n, если n — нечетное; n!! = 2·4·6·...·n, если n — четное (n > 0 —
параметр целого типа. С помощью этой функции найти двойные
факториалы пяти данных целых чисел
'''


def fact2(n: int):
    fact = 1
    if n == 0:
        return 1
    elif n % 2 == 1:
        for i in range(1, n+1, 2):
            fact *= i
        return fact
    else:
        for i in range(2, n + 1, 2):
            fact *= i
        return fact


num_list = [5, 14, 15, 8, 10]
for i in num_list:
    print(f'{i}!! = {fact2(i)}')
