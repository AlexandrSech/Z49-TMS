# В массиве целых чисел с количеством элементов 19 определить максимальное
# число и заменить им все четные по значению элементы.
from random import randint
list_of_number = []
for i in range(19):
    list_of_number.append(randint(0,100))
max = list_of_number[0]
for i in list_of_number:
    if i > max:
        max = i
print(list_of_number)
print(max)