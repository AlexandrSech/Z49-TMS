import random
n, m = int(input('Количество столбцов: ')), int(input('Количество строк: '))
a, b = int(input('Интервал от: ')), int(input('до: '))
matrix = []
for i in range(n):
    l = []
    matrix.append(l)
    for j in range(m):
        l.append(random.randrange(a, b+1))
    print(matrix[i])



max_el = 0
min_el = b
for item, value in enumerate(matrix):
    for i, j in enumerate(value):
        if j > max_el:
            max_el = j
        if j < min_el:
            min_el = j
print('Максимальный элемент матрицы:', max_el)
print('Минимальный элемент матрицы:', min_el)