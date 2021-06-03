n = int(input('Введите количество  столбцов и строк: '))
matrix = []
maxi = 0
for i in range(n):
    b = []
    for i in range(n):
        b.append(int(input()))
    matrix.append(b)
for i in range(n):
    for j in range(n):
        print(matrix[i][j], end = ' ')
    print()
for i in range(n):
    for j in range(n):
        if matrix[i][j] >= maxi:
            maxi =  matrix[i][j]
for i in range(n):
    for j in range(n):
        if i == j:
            matrix[i][j] = maxi
print("Максимальный элемент:", maxi, '\n' + 'Новая матрица:')
for i in range(n):
    for j in range(n):
        print(matrix[i][j], end = ' ')
    print()
