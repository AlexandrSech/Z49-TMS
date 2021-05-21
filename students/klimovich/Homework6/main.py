import random
#1
m = int(input())
n = int(input())
a = int(input())
b = int(input())
matrix = [[random.randrange(a, b) for i in range(m)] for j in range(n)]

for i in range(m):
    print(matrix[i])

#2,3,4
max = matrix[0][0]
min = matrix[0][0]
sum = 0
for i in range(len(matrix)):
    for j in range(len(matrix)):
        if matrix[i][j] > max:
            max = matrix[i][j]
        elif matrix[i][j] < min:
            min = matrix[i][j]
        sum += matrix[i][j]
print('Максимальный элемент матрицы:', max)
print('Минимальный элемент матрицы:', min)
print('Сумма элементов матрицы:', sum)

#5, 7
sum_of_str_temp = 0
sum_of_str = 0
min_of_str = 0
for i in range(len(matrix)):
    for j in range(len(matrix)):
        if i == 0:
            sum_of_str += matrix[i][j]
            min_of_str += matrix[i][j]
        else:
            break

print('----')
num_of_str = 0
num_of_str2 = 0
for i in range(len(matrix)):
    for j in range(len(matrix)):
        sum_of_str_temp += matrix[i][j]
        if sum_of_str_temp > sum_of_str:
            sum_of_str = sum_of_str_temp
            num_of_str = i
        elif sum_of_str_temp < min_of_str:
            min_of_str = sum_of_str_temp
            num_of_str2 = i
    sum_of_str_temp = 0
print('Номер строки с макс суммой элементов', num_of_str, ' --сумма: ', sum_of_str)
print('Номер строки с мин суммой элементов', num_of_str2, ' --сумма: ', min_of_str)

#6,8
sum_of_column = 0
min_of_column = 0
sum_of_column_temp = 0
min_of_column_temp = 0
for i in range(len(matrix)):
    for j in range(len(matrix)):
        if i == 0:
            sum_of_column += matrix[i][j]
            min_of_column += matrix[i][j]
        else:
            break
num_of_column = 0
num_of_column2 = 0
for i in range(len(matrix)):
    for j in range(len(matrix)):
        sum_of_column_temp += matrix[j][i]
        min_of_column_temp += matrix[j][i]
        if sum_of_column_temp > sum_of_column:
            sum_of_column = sum_of_column_temp
            num_of_column = i
        if i == len(matrix):
            if min_of_column_temp < min_of_column:
                min_of_column = sum_of_column_temp
                num_of_column2 = i
            min_of_column_temp = 0
    sum_of_column_temp = 0

print('Номер колонки с макс суммой элементов', num_of_column, ' --сумма: ', sum_of_column)
print('Номер колонки с мин суммой элементов', num_of_column2, ' --сумма: ', min_of_column)

#9
matrix_zero1 = [[random.randrange(a, b) for i in range(m)] for j in range(n)]

for i in range(m):
    print(matrix_zero1[i])
print('-----')
for i in range(len(matrix_zero1)):
    for j in range(len(matrix_zero1)):
        if j > i:
            matrix_zero1[i][j] = 0

for i in range(m):
    print(matrix_zero1[i])

print('-----')
print('-----')
#10
matrix_zero2 = [[random.randrange(a, b) for i in range(m)] for j in range(n)]

for i in range(m):
    print(matrix_zero2[i])
print('-----')
for i in range(len(matrix_zero2)):
    for j in range(len(matrix_zero2)):
        if j < i:
            matrix_zero2[i][j] = 0
for i in range(m):
    print(matrix_zero2[i])


print('-----')
print('-----')
#11
matrix_a = [[random.randrange(1, 15) for i in range(5)] for j in range(5)]
matrix_b = [[random.randrange(2, 14) for i in range(5)] for j in range(5)]
matrix_multi = [[random.randrange(2, 14) for i in range(5)] for j in range(5)]
matrix_sum = [[random.randrange(2, 14) for i in range(5)] for j in range(5)]

print('MATRIX_A: ')
for i in range(len(matrix_a)):
    print(matrix_a[i])

print('---')

print('MATRIX_B: ')
for i in range(len(matrix_b)):
    print(matrix_b[i])

print('---')


for i in range(len(matrix_a)):
    for j in range(len(matrix_a)):
        matrix_multi[i][j] = matrix_b[i][j] * matrix_a[j][i]
print('MATRIX_A * MATRIX_B: ')
for i in range(len(matrix_multi)):
    print(matrix_multi[i])
print('---')
for i in range(len(matrix_a)):
    for j in range(len(matrix_a)):
        matrix_sum[i][j] = matrix_b[i][j] + matrix_a[i][j]
print('MATRIX_A + MATRIX_B: ')
for i in range(len(matrix_sum)):
    print(matrix_sum[i])



