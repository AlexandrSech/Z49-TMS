"""Найти минимальный минимальный матрицы."""
"""Найти максимальный элемент матрицы."""
import random


def minimum(sp, k):
    for el in sp:
        if el < k:
            k = el
    return k


a = 1
b = 1000
matr = []
spis = []
for i in range(5):
    matr.append([])
    for j in range(5):
        matr[i].append(random.randint(a, b))
    print(matr[i])
for i in range(len(matr)):
    spis.append(minimum(matr[i], b))
print(minimum(spis, b))