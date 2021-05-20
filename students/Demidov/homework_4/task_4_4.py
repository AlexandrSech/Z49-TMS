# Дан список. Создать новый список, сдвинутый на 1 элемент влево
# Пример: 1 2 3 4 5 -> 2 3 4 5 1


my_dict = [1, 2, 3, 4, 5]
new_dict = []

for elem in my_dict:
    if elem == my_dict[0]:
        new_dict = my_dict.pop(0)
        my_dict.append(1)
        new_dict = my_dict
        print(new_dict)