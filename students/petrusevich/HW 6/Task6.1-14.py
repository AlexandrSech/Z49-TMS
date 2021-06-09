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
