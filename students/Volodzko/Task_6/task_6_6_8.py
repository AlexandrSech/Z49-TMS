import random

"""
1)Создать матрицу случайных чисел от a до b, размерность матрицы n*m
6)Найти индекс колонки с максимальной суммой элементов.
8)Найти индекс колонки с минимальной суммой элементов.
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
print()

for i in matrix:
    print(i)  # Выводим матрицу на консоль

print()

matrix2 = []
for j in range(m):  # Меняем строки и столбцы местами
    lst = []
    for i in range(n):
        lst.append(matrix[i][j])
    matrix2.append(lst)

print()

for i in matrix2:
    print(i)  # Проверяем заменились ли строки на столбцы

print()

res_mas = []
for i in matrix2:
    res = 0
    for j in range(len(i)):
        res += i[j]  # Суммируем числа строки
    res_mas.append(res)  # Добавляем сумму в список

print(res_mas)  # Список сумм столбцов

index = 0
r = res_mas[0]
for i in range(len(res_mas)):
    if res_mas[i] > r:
        r = res_mas[i]
        index = i
print("Индекс колонки с максимальной суммой элементов: ", index)  # Индекс колонки с максимальной суммой элементов

for i in range(len(res_mas)):
    if res_mas[i] < r:
        r = res_mas[i]
        index = i
print("Индекс колонки с минимальной суммой элементов: ", index)  # Индекс колонки с минимальной суммой элементов
