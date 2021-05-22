import random

"""
11) Создать две новые матрицы matrix_a, matrix_b случайных чисел размерностью n*m.
12)Создать матрицу равную сумме matrix_a и matrix_b.
13)Создать матрицу равную разности matrix_a и matrix_b.
14)Создать новую матрицу равную matrix_a умноженной на g. g вводится склавиатура
"""

# 11) Создать две новые матрицы matrix_a, matrix_b случайных чисел размерностью n*m.
n = int(input("Введите размерность матрицы N: "))
m = int(input("Введите размерность матрицы M: "))

a = int(input("Введите нижнюю границу случайных чисел: "))
b = int(input("Введите ыерхнюю границу случайных чисел: "))

matrix_a = []
matrix_b = []

for i in range(n):
    lst_a = []
    lst_b = []
    for j in range(m):
        lst_a.append(random.randint(a, b))
        lst_b.append(random.randint(a, b))
    matrix_a.append(lst_a)
    matrix_b.append(lst_b)

for i in matrix_a:
    print(i)

print()

for i in matrix_b:
    print(i)

print()

# Создать матрицу равную сумме matrix_a и matrix_b.
matrix_sum = []

for i in range(len(matrix_a)):
    lst_sum = []
    for j in range(len(matrix_a[i])):
        lst_sum.append(matrix_a[i][j] + matrix_b[i][j])
    matrix_sum.append(lst_sum)

for i in matrix_sum:
    print(i)

print()

# 13)Создать матрицу равную разности matrix_a и matrix_b.
matrix_minus = []

for i in range(len(matrix_a)):
    lst_sum = []
    for j in range(len(matrix_a[i])):
        lst_sum.append(matrix_a[i][j] - matrix_b[i][j])
    matrix_minus.append(lst_sum)

for i in matrix_minus:
    print(i)

print()

# 14)Создать новую матрицу равную matrix_a умноженной на g. g вводится склавиатура
matrix_mult = []
g = int(input("Введите число g, на которое будет умножаться матрица matrix_a: "))
for i in range(len(matrix_a)):
    lst_sum = []
    for j in range(len(matrix_a[i])):
        lst_sum.append(matrix_a[i][j] * g)
    matrix_mult.append(lst_sum)

for i in matrix_mult:
    print(i)
