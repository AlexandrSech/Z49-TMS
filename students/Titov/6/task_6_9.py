"""Обнулить все элементы выше главной диагонали"""
import random

matr = []
for i in range(5):
    matr.append([])
    for j in range(5):
        if j > i:
            matr[i].append(0)
        else:
            matr[i].append(random.randint(1, 9))
    print(matr[i])