'''
4) Дан список. Создать новый список, сдвинутый на 1 элемент влево Пример:12345-> 23451
'''

# example_1

list_1 = [1, 2, 8, 45, 76, 3, 4, 5, 6, 99, 101]

new_list = []
for i in list_1:
    i += 1
    new_list.append(i)
print(new_list)


# example_2

list_1 = [1, 2, 8, 45, 76, 3, 4, 5, 6, 99, 101]

i = 0
while i < len(list_1):
    list_1[i] += 1
    if i == len(list_1) - 1:
        print(list_1)
    i += 1
