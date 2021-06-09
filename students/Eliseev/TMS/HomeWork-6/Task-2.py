import random

size_x = int(input("Размер матрицы по x: "))
size_y = int(input("Размер матрицы по y: "))
a = int(input("Стартовое число: "))
b = int(input("Конечное число: "))
list_1 = []
max_elems = []


for el in range(size_x):
    list_1.append(random.randint(a, b))
for el in range(size_y):
    i = 0
    for el in list_1:
        list_1[i] = random.randint(a, b)
        i += 1
    max_el = max(list_1)
    max_elems.append(max_el)
    print(list_1)
max_el = max(max_elems)
print(max_el)