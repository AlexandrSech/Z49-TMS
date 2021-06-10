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


max_res = []
index_max = 0
index_min = 0
puk = 0
pik = m*b
for j, i in enumerate(matrix):
    res = 0
    for k in range(len(i)):
        res += i[k]
    max_res.append(res)
    if puk < res:
        puk = res
        index_max = j
    if pik > res:
        pik = res
        index_min = j
print('Суммы ряда:', max_res)
print('Индекс ряда с максимальной суммой элементов:', index_max)
print('Индекс ряда с минимальной суммой элементов:', index_min)

