"""4) Дан список. Создать новый список,
сдвинутый на 1 элемент влево Пример: 1 2 3 4 5 ->  2 3 4 5 1"""

my_list = [1, 2, 3, 4, 5]

my_list.append(my_list[0])
del my_list[0]
print(my_list)

my_list2 = [1, 2, 3, 4, 5]
my_list3 = list()
i = 0


