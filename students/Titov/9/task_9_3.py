"""Создать декоратор для функции, которая принимает список чисел.
Декоратор должен производить предварительную проверку данных -
удалять все четные элементы из списка."""

def outer(chisla):
    def inner(spis = []):
        spis_1 = []
        for i in range(len(spis)):
            print(i)
            if spis[i] % 2 != 0:
                spis_1.append(spis[i])
        chisla(spis_1)
    return inner

@outer
def foo(spis):
    print(spis)

spis = [1, 2, 46, 9, 12]
foo(spis)