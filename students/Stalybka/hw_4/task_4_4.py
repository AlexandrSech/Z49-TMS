'''Дан список. Создать новый список, сдвинутый на 1 элемент влево
Пример: 1 2 3 4 5 -> 2 3 4 5 1'''

my_list = [1, 2, 3, 4, 5, ]
dl = int(len(my_list))

for i in range(0,dl):
    if i == 0:
        my_list.append(my_list[i])
        my_list.pop(i)
    else:
        pass
print(my_list)

my_list = [1, 2, 3, 4, 5, ]
dl = int(len(my_list))
while dl > 0 and dl != 1:
    dl -= 1
else:
    my_list.append(my_list[0])
    my_list.pop(0)
print(my_list)

