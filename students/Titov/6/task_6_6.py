'''Найти индекс колонки с максимальной суммой элементов'''

import random
def maximum(sp):
    k = 0
    for el in sp:
        if el > k:
            k = el
    return k

matr = []
spis = []
for i in range(5):
    matr.append([])
    for j in range(5):
        matr[i].append(random.randint(1, 30))
    print(matr[i])
for i in range(len(matr)):
    s = 0
    for j in range(len(matr[i])):
        s += matr[j][i]
    spis.append(s)

print(spis)
print("Индекс наибольшего столбца:", spis.index(maximum(spis)))
