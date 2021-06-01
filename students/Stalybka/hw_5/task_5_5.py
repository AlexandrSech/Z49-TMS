'''В массиве целых чисел с количеством элементов 19 определить максимальное
число и заменить им все четные по значению элементы.'''
import random

my_array = []
count = 0
while count < 19:
    my_array.append(random.randint(0,1000))
    count += 1
print(my_array)
for id, value in enumerate(my_array):
        if value % 2 ==0:
            my_array[id] = max(my_array)
print(my_array)

