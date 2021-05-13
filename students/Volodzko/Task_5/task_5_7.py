"""
Дана целочисленная квадратная матрица.
Найти в каждой строке наи-больший элемент
и поменять его местами с элементом главной диагонали
"""
matrix = [[5, 8, 2, 3], [7, 11, 1, 8], [9, 4, 6, 5], [2,12,1,3]]

for i in matrix:
    print(i)
print("\n")

for item, value in enumerate(matrix):
    max_value = 0
    for j in range(len(matrix[item])):
        if matrix[item][j] > max_value:
            max_value = matrix[item][j]
    matrix[item][item] = max_value



for i in matrix:
    print(i)


