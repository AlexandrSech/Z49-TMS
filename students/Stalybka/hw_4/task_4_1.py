'''Дан список целых чисел.
Создать новый список, каждый элемент которого равен исходному элементу
умноженному на -2'''

my_list = [13, 5, 43, 6, -6,]
new_list = my_list[:]
for i in range(0,len(new_list)):
    new_list[i] = new_list[i] * -2
print(my_list)
print(new_list)


new_list = my_list[:]
cycle = len(new_list)
while cycle > 0:
    new_list[i] = new_list[i] * -2
    cycle -= 1
    i -= 1
print(new_list)