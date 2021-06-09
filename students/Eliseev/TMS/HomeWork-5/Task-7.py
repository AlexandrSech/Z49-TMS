import random

size = int(input("Размер матрицы: "))
list_1 = []
for el in range(size):
    list_1.append(random.randint(1, 9))



for el in range(size):
    i = 0
    for el_i in list_1:
        list_1[i] = random.randint(1, 9)
        i += 1
    max_el = max(list_1)
    list_1[el] = max_el
    list_1[el - 1] = random.randint(1, 9)
    print(list_1)
