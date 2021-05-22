import random

"""
1)Создать матрицу случайных чисел от a до b, размерность матрицы n*m
2)Найти максимальный элемент матрицы.
3)Найти минимальный минимальный матрицы.
4)Найти сумму всех элементов матрицы.
5)Найти индекс ряда с максимальной суммой элементов.
6)Найти индекс колонки с максимальной суммой элементов.
7)Найти индекс ряда с минимальной суммой элементов.
8)Найти индекс колонки с минимальной суммой элементов.
9) Обнулить все элементы выше главной диагонали.
10) Обнулить все элементы ниже главной диагонали.
"""
n = int(input("Введите размерность матрицы N: "))
m = int(input("Введите размерность матрицы M: "))

a = int(input("Введите нижнюю границу случайных чисел: "))
b = int(input("Введите ыерхнюю границу случайных чисел: "))
matrix = []

# 1. Создаём матрицу m*n
for i in range(n):
    t = []
    matrix.append(t)
    for j in range(m):
        t.append(random.randint(a, b))

for i in matrix:  # Вывод матрицы на консоль
    print(i)

max_value = 0
for item, value in enumerate(matrix):
    for i, ii in enumerate(value):
        if ii > max_value:
            max_value = ii
print("Максимальный элемент матрицы: ", max_value)  # 2. Максимальный элемент матрицы

min_value = matrix[0][0]
for item, value in enumerate(matrix):
    for i, ii in enumerate(value):
        if ii < min_value:
            min_value = ii
print("Минимальный элемент матрицы: ", min_value)  # 3. Минимальный элемент матрицы

# 4. Сумма всех элементов матрицы
sum_value = 0
for item, value in enumerate(matrix):
    for i, ii in enumerate(value):
        sum_value += ii
print("Сумма всех элементов матрицы: ", sum_value)

# 5. Индекс ряда с максимальной суммой элементов.
mas_res = []
for i in matrix:
    res = 0
    for j in range(len(i)):
        res += i[j]
    mas_res.append(res)
print(mas_res)  # Список сумм элементов каждого ряда

r_max = mas_res[0]
index_max = 0
for i in range(len(mas_res)):
    if mas_res[i] > r_max:
        r_max = mas_res[i]
        index_max = i
print("Индекс ряда с максимальной суммой элементов: ", index_max)

# 8)Найти индекс колонки с минимальной суммой элементов.
r_min = mas_res[0]
index_min = 0
for i in range(len(mas_res)):
    if mas_res[i] < r_min:
        r_min = mas_res[i]
        index_min = i
print("Индекс ряда с минимальной суммой элементов: ", index_min)

# 9) Обнулить все элементы выше главной диагонали.
for item in range(len(matrix)):
    for i in range(len(matrix[item])):
        if i - item > 0:
            matrix[item][i] = 0

for i in matrix:
    print(i)

print()
# 10) Обнулить все элементы ниже главной диагонали.
for item in range(len(matrix)):
    for i in range(len(matrix[item])):
        if i - item < 0:
            matrix[item][i] = 0

for i in matrix:
    print(i)
