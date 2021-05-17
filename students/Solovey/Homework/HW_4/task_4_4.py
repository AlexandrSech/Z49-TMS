'''
4) Дан список. Создать новый список, сдвинутый на 1 элемент влево Пример: 12345 -> 23451
'''

# example_1

list_1 = [2,3,4,5,6,7]
new_list = []

for i in list_1:
    if i == len(list_1):
        new_list = list_1[1:]
        new_list.append(list_1[0])
        print(new_list)

# example_2

list_1 = [2,3,4,5,6,7]
new_list = []
i = 0

while i < len(list_1):
    new_list = list_1[1:]
    new_list.append(list_1[0])
    i += 1
print(new_list)