'''В массиве целых чисел с количеством элементов 19 определить максимальное
число и заменить им все четные по значению элементы.'''
spis = [12, 947, 351, 678, 123, 1, 346, 1000, 235, 13, 0, 45, 42, 11, 99, 57, 12, 345, 503]
max = 0
for el in spis:
    if max <= el: max = el
for el in range(len(spis)):
    if spis[el] % 2 == 0:
        spis[el] = max
print(spis)