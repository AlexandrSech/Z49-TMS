"""Найти сумму всех элементов матрицы."""

import random


sum = 0
matr = []
for i in range(5):
    matr.append([])
    for j in range(5):
        a = random.randint(1, 30)
        matr[i].append(a)
        sum += a
    print(matr[i])
print(sum)