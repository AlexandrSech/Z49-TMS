'''
1) Создать матрицу случайных чисел от a до b, размерность матрицы n*m
2) Найти максимальный элемент матрицы.
3) Найти минимальный элемент матрицы.
4) Найти сумму всех элементов матрицы.
5) Найти индекс ряда с максимальной суммой элементов.
6) Найти индекс колонки с максимальной суммой элементов.
7) Найти индекс ряда с минимальной суммой элементов.
8) Найти индекс колонки с минимальной суммой элементов.
9) Обнулить все элементы выше главной диагонали.
10) Обнулить все элементы ниже главной диагонали.
11) Создать две новые матрицы matrix_a, matrix_b случайных чисел
размерностью n*m.
12)Создать матрицу равную сумме matrix_a и matrix_b.
13)Создать матрицу равную разности matrix_a и matrix_b.
14)Создать новую матрицу равную matrix_a умноженной на g. g вводится с
клавиатура
'''
import random
import copy
a, b = 20, 100
n, m = 6, 6
my_array = [[random.randint(a, b) for i in range(n)]for item in range(m)]
for i in my_array:
    print(i)

#2) Найти максимальный элемент матрицы.
#3) Найти минимальный элемент матрицы.

max_num_list, min_num_list = [], []
for i in range(m):
    max_num_list.append(max(my_array[i]))
    min_num_list.append(min(my_array[i]))
print('максимальный элемент матрицы =', max(max_num_list))
print('минимальный элемент матрицы =', min(min_num_list))

#4) Найти сумму всех элементов матрицы.
#5) Найти индекс ряда с максимальной суммой элементов.
#7) Найти индекс ряда с минимальной суммой элементов.

sum_list = []
for i in range(m):
    sum_list.append(sum(my_array[i]))
print('Cуммa всех элементов матрицы =', sum(sum_list))
print('индекс ряда с максимальной суммой элементов =', sum_list.index(max(sum_list)))
print('индекс ряда с минимальной суммой элементов =', sum_list.index(min(sum_list)))

#6) Найти индекс колонки с максимальной суммой элементов.
#8) Найти индекс колонки с минимальной суммой элементов.

column_sum= []
for j in range(n):
    summ = 0
    for i in range(m):
        summ += my_array[i][j]
    column_sum.append(summ)
print('индекс колонки с максимальной суммой элементов =', column_sum.index(max(column_sum)))
print('индекс колонки с минимальной суммой элементов =', column_sum.index(min(column_sum)))

#9) Обнулить все элементы выше главной диагонали.
#10) Обнулить все элементы ниже главной диагонали.
my_array_up = copy.deepcopy(my_array)
for item in my_array_up:
    i = m-1
    while i > my_array_up.index(item):
        item[i] = 0
        i -= 1
for i in my_array_up:
    print(i)
print('\n')
my_array_down = copy.deepcopy(my_array)
for item in my_array_down:
    i = 0
    while i < my_array_down.index(item):
        item[i] = 0
        i += 1
for i in my_array_down:
    print(i)

#11) Создать две новые матрицы matrix_a, matrix_b случайных чисел размерностью n*m.

matrix_a = [[random.randint(a, b) for i in range(n)]for item in range(m)]
matrix_b = [[random.randint(a, b) for i in range(n)]for item in range(m)]
matrix_sub, matrix_sum = [[] for item in range(m)], [[] for item in range(m)]
for i in range(n):
    print(matrix_a[i], '   ', matrix_b[i])

#12)Создать матрицу равную сумме matrix_a и matrix_b.
#13)Создать матрицу равную разности matrix_a и matrix_b.

for i in range(m):
    for j in range(n):
        matrix_sum[i].append(matrix_a[i][j] + matrix_b[i][j])
        matrix_sub[i].append(matrix_a[i][j] - matrix_b[i][j])
for i in range(n):
    print(matrix_sum[i], '   ', matrix_sub[i])

# 14)Создать новую матрицу равную matrix_a умноженной на g. g вводится с клавиатура

new_matrix = [[] for item in range(m)]
g = int(input('Введите число:'))
for i in range(m):
    for j in range(n):
        new_matrix[i].append(matrix_a[i][j] * g)
for item in range(m):
    print(matrix_a[item], '   ', new_matrix[item])
