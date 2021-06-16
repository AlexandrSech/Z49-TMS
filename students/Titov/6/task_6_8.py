'''Найти индекс колонки с минимальной суммой элементов'''

import random
def minimum(sp, k):
    for el in sp:
        if el < k:
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
print("Индекс наименьшего столбца:", spis.index(minimum(spis, spis[0])))
