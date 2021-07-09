#Описать функцию fact2( n ), вычисляющую двойной факториал
# :n!! = 1·3·5·...·n, если n — нечетное; n!! = 2·4·6·...·n,
# если n — четное (n > 0 —параметр целого типа.
# С помощью этой функции найти двойные
# факториалы пяти данных целых чисел

def fact2(*args):
    lst_fact2 = []
    for i in args:
        result = 1
        if i % 2 == 0:
            for i in range (2, i+1, 2):
                result = result * i
            lst_fact2.append(result)
        elif i % 2 != 0:
            for i in range(1, i+1, 2):
                result = result * i
            lst_fact2.append(result)

    return lst_fact2

print(fact2(4, 5, 6, 7, 8))