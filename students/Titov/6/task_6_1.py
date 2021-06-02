"""Создать матрицу случайных чисел от a до b, размерность матрицы n*m"""
import random
a = 1
b = 10
matr = []
for i in range(5):
    matr.append([])
    for j in range(5):
        matr[i].append(random.randint(a, b))
    print(matr[i])