import random


size_x = int(input("Размер матрицы по x: "))
size_y = int(input("Размер матрицы по y: "))
a = int(input("Стартовое число: "))
b = int(input("Конечное число: "))
list_1 = []
list_summa_matrix = []



for el in range(size_x):
    list_1.append(random.randint(a, b))
for el in range(size_y):
    i = 0
    summa_matrix = 0
    for el in list_1:
        list_1[i] = random.randint(a, b)
        summa_matrix += list_1[i]
        i += 1
    list_summa_matrix.append(summa_matrix)
    print(list_1)
min_el = min(list_summa_matrix)
print(list_summa_matrix.index(min_el))