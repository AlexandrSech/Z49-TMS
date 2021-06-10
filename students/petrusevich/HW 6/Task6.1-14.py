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