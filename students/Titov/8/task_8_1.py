"""Описать функцию fact2( n ), вычисляющую двойной факториал :n!! =
1·3·5·...·n, если n — нечетное; n!! = 2·4·6·...·n, если n — четное (n > 0 —
параметр целого типа. С помощью этой функции найти двойные
факториалы пяти данных целых чисел [01-11.2-Proc35]"""
from random import randint
def fact2(n):
    f = 1
    if n % 2 == 0:
        for i in range(2, n + 1, 2):
            f *= i

        return f
    else:
        for i in range(1, n + 1, 2):
            f *= i
            #print(i)
        return f
spis = [randint(1, 9) for item in range(5)]
for i in range(5):
    print(spis[i], ' ', fact2(spis[i]))