"""
В массиве целых чисел с количеством элементов 19
определить максимальное число и заменить им все четные
по значению элементы.
"""

mas = [1, 2, 33, 4, 52, 6, 7, 81, 9, 1, 11, 12, 1, 14, 5, 16, 7, 18, 19]
result = 0

for i in range(len(mas)):
    if result < mas[i]:
        result = mas[i]
print(result)

for i in range(len(mas)):
    if mas[i] % 2 == 0:
        mas[i] = result
    print(mas[i], end=" ")
print("\n")
print(mas)