"""Создать матрицу равную сумме matrix_a и matrix_b"""
import random
matr_a = []
matr_b = []
matr_c = []
for i in range(5):
    matr_a.append([])
    matr_b.append([])
    matr_c.append([])
    for j in range(5):
        matr_a[i].append(random.randint(1, 9))
        matr_b[i].append(random.randint(1, 9))
        matr_c[i].append(matr_a[i][j] + matr_b[i][j])
    print(matr_a[i], '   ',matr_b[i], '    ', matr_c[i])
