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
print()


max_el = 0
min_el = b
summ = 0
for item, value in enumerate(matrix):
    for i, j in enumerate(value):
        if j > max_el:
            max_el = j
        if j < min_el:
            min_el = j
        summ += j
print('Максимальный элемент матрицы:', max_el)
print('Минимальный элемент матрицы:', min_el)
print('Сумма всех элементов:', summ)
print()



summ_lst = []
for j, i in enumerate(matrix):
    res = 0
    for k in range(len(i)):
        res += i[k]
    summ_lst.append(res)
print('Суммы рядов:', summ_lst)
print('Индекс ряда с максимальной суммой элементов:', summ_lst.index(max(summ_lst)))
print('Индекс ряда с минимальной суммой элементов:', summ_lst.index(min(summ_lst)))
print()

column_sum = []
for j in range(n):
    ssumm = 0
    for i in range(m):
        ssumm += matrix[i][j]
    column_sum.append(ssumm)
print('Сумма столбцов:', column_sum)
print('Индекс колонки с максимальной суммой элементов:', column_sum.index(max(column_sum)))
print('Индекс колонки с минимальной суммой элементов:', column_sum.index(min(column_sum)))

print('\n' + 'Обнуленная матрица:')
for i in range(n):
    for j in range(m):
        if i != j:
            matrix[i][j] = 0
    print(matrix[i])
print()


print('Матрицы a и b:')
matrix_a = [[random.randrange(a, b+1) for i in range(n)] for j in range(m)]
matrix_b = [[random.randrange(a, b+1) for i in range(n)] for j in range(m)]
for i in range(n):
    print(matrix_a[i], '    ', matrix_b[i])
print()


print('Матрицы суммы и разности матриц a и b: ')
ssum = [[] for j in range(m)]
razn = [[] for j in range(n)]
for i in range(m):
    for j in range(n):
        ssum[i].append(matrix_a[i][j] + matrix_b[i][j])
        razn[i].append(matrix_a[i][j] - matrix_b[i][j])
for i in range(n):
    print(ssum[i], '    ', razn[i])

g = int(input('\n' + 'Введите g: '))
print('Новая матрица a умноженная на g: ')
new_matr = [[] for i in range(m)]
for i in range(n):
    for j in range(m):
        new_matr[i].append(matrix_a[i][j] * g)
for i in range(n):
    print(new_matr[i])