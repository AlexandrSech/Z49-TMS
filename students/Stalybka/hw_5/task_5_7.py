'''
Дана целочисленная квадратная матрица. Найти в каждой строке
наибольший элемент и поменять его местами с элементом главной диагонали.
'''

import random
m = 5
n = 5
my_array = [[random.randint(0, 100) for i in range(m)] for item in range(n)]
for i in my_array:
    print(i)
print('\n')
for i in range(n):
    _ = my_array[i].index(max(my_array[i]))
    my_array[i][i], my_array[i][_] = my_array[i][_], my_array[i][i]
for i in my_array:
    print(i)