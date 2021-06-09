"""
Дан список целых чисел.Создать новый список,
каждый элемент которого равен исходному элементу умноженному на -2
"""
# Способ 1
my_list = [2, 5, 3, 8, 7, 9]
my_list2 = list()
i = 0
while i < len(my_list):
    my_list2.append(my_list[i]*(-2))
    i+=1
print(my_list2)

# Способ 2
my_list3 = [2, 5, 3, 8, 7, 9]
my_list4 = list()

for i in my_list3:
    my_list4.append(i*(-2))
print(my_list4)
