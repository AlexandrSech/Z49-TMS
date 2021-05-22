# Дан список. Создать новый список, сдвинутый на 1 элемент влево Пример: 1 2 3 4 5 ->  2 3 4 5 1
lst = [1, 10, 15, 30, 45]
lst_1 = []
x = 1
while x < len(lst):
    lst_1.append(lst[x])
    x += 1
lst_1.append(lst[0])
print(lst_1)

exit()

lst = [1, 10, 15, 30, 45]
lst_1 = []
for i in lst[1:]:
    lst_1.append(i)
lst_1.append(lst[0])
print(lst_1)
