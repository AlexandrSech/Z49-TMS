"""Создать новую матрицу равную matrix_a умноженной на g. g вводится с
клавиатура"""
import random
g = input("Введите число")
matr = []
for i in range(5):
    matr.append([])
    for j in range(5):
        matr[i].append(int(random.randint(1, 9)) * 9)
    print(matr[i])