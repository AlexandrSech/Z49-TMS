"""Создать две новые матрицы matrix_a, matrix_b случайных чисел
размерностью n*m."""
import random
matr_a = []
matr_b = []
for i in range(5):
    matr_a.append([])
    matr_b.append([])
    for j in range(5):
        matr_a[i].append(random.randint(1, 9))
        matr_b[i].append(random.randint(1, 9))
    print(matr_a[i], '   ',matr_b[i])