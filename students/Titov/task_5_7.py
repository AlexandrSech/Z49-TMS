""" Дана целочисленная квадратная матрица. Найти в каждой строке наи-
больший элемент и поменять его местами с элементом главной диагонали."""
import random
def maximum(sp):
    k = 0
    for el in sp:
        if el > k:
            k = el
    return k
spis = []
for i in range(5):
    spis.append([])
    for j in range(5):
        spis[i].append(random.randint(1, 9))
    print(spis[i])
for i in range(len(spis)):
    for j in range(len(spis[i])):
        if i == j:
            spis[i].pop(j)
            spis[i].insert(j, maximum(spis[i]))
    print(spis[i])