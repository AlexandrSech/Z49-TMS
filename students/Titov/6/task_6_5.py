"""Найти индекс ряда с максимальной суммой элементов."""
import random


sum = 0
matr = []
spis = []
for i in range(5):
    matr.append([])
    for j in range(5):
        a = random.randint(1, 30)
        matr[i].append(a)
        sum += a
    spis.append(sum)
    print(matr[i])
    sum = 0
for i in range(len(spis)):
    if spis[i] > sum:
        sum = spis[i]
for i in range(len(spis)):
    if sum == spis[i]:
        print(i)