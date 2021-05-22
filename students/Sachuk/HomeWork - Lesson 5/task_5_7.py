# Дана целочисленная квадратная матрица. Найти в каждой строке
# наи-больший элемент и поменять его местами с элементом главной диагонали.
# [02-4.2-ML22]
from random import randint
size = int(input())
matrix = [[randint(1,100) for i in range(size)] for j in range(size)]

for i in matrix:
    print(i)

for i in range(len(matrix)):
    max = matrix[i][0]
    index_row = i
    index_col = 0
    for j in range(len(matrix[i])):
        if matrix[i][j] > max:
            max = matrix[i][j]
            index_row = i
            index_col = j
    if max > matrix[i][i]:
        temp = matrix[i][i]
        matrix[i][i] = max
        matrix[index_row][index_col] = temp

print()
for i in matrix:
    print(i)
