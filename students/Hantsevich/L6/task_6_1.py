import random
n = int(input("n: "))
m = int(input(" m: "))
a = int(input("Нижний порог значений:"))
b = int(input("Верхний порог значений:"))
matrix = []
for i in range(n):
    l = []
    matrix.append(l)
    for j in range(m):
        l.append(random.randint(a, b))
for i in matrix:
    print(i)

#2) Найти максимальный элемент матрицы.
maxv = 0
for item, value in enumerate(matrix):
    for i, ii in enumerate(value):
        if ii > maxv:
            maxv = ii
print('Максимальный элемент:', maxv)

#3) Найти минимальный минимальный матрицы.

minv = b
for item, value in enumerate(matrix):
    for i, ii in enumerate(value):
        if ii < minv:
            minv = ii
print('Минимальный элемент:', minv)

#4) Найти сумму всех элементов матрицы.

stotal = 0
for item, value in enumerate(matrix):
    for i, ii in enumerate(value):
        stotal += ii
print('Сумма:', stotal)

#5) Найти индекс ряда с максимальной суммой элементов.

max_res = []
for i in matrix:
    res = 0
    for j in range(len(i)):
        res += i[j]
    max_res.append(res)
print(max_res)

r_max = max_res[0]
index_max = 0
for i in range(len(max_res)):
    if max_res[i] > r_max:
        r_max = max_res[i]
        index_max = i
print("Индекс ряда с максимальной суммой элементов: ", index_max, matrix[int(index_max)])

#6) Найти индекс колонки с максимальной суммой элементов.

max_kol = []
for j in range(m):
    kol = 0
    for k in matrix:
        kol += k[j]
    max_kol.append(kol)

k_max = max_kol[0]
index_k_max = 0

for i in range(len(max_kol)):
    if max_kol[i] > k_max:
        k_max = max_kol[i]
        index_k_max = i

kolumn_max = []
for i in matrix:
    kolumn_max.append(i[index_k_max])
print("Индекс колонки с максимальной суммой элементов: ", index_k_max, kolumn_max)