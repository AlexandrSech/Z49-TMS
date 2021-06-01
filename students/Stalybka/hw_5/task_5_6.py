"""Задан целочисленный массив. Определить количество участков массива,
на котором элементы монотонно возрастают (каждое следующее число
больше предыдущего)"""

import random

my_array = [random.randint(0, 50) for item in range(10)]
count = 0
for i in range(1, len(my_array) - 1):
    if my_array[i] > my_array[i-1] \
            and my_array[i] > my_array[i+1]: # тут ищу точку, на которой возрастание заканчивается
        count += 1
if my_array[-1] > my_array[-2]: #тут проверяю, есть ли эта точка в конце
   count +=1

print(my_array, '\n', count)
