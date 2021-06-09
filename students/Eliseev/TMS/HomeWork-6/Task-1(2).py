import random
size_x = int(input("Размер матрицы по x: "))
size_y = int(input("Размер матрицы по y: "))
a = int(input("Стартовое число: "))
b = int(input("Конечное число: "))
list_1 = []

for el in range(size_y):
    list_el = []
    for el in range(size_x):
        list_el.append(random.randint(a, b))
    list_1.append(list_el)
for el in list_1:
    print(el)
