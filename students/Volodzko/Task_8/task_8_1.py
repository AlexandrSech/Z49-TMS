"""
Описать функцию fact2( n ), вычисляющую двойной факториал:
n!! =1·3·5·...·n, если n — нечетное; n!! = 2·4·6·...·n,
если n — четное (n > 0 —параметр целого типа. С помощью этой
функции найти двойныефакториалы пяти данных целых чисел [01-11.2-Proc35]
"""


# Способ 1
def fact(n):
    my_list = list(range(1, n + 1, 2))
    my_list2 = list(range(2, n + 1, 2))
    print(my_list, my_list2)

    def fact1(m):
        result = 1
        for i in range(len(m)):
            result *= m[i]
        return result

    return f"Факториал чётных чисел от числа {n}: {fact1(my_list)}\n" \
           f"Факториал нечётных чисел от числа {n}: {fact1(my_list2)} "


print(fact(10))

