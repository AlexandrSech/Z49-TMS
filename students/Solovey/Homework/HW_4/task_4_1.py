'''
1) Дан список целых чисел.
Создать новый список, каждый элемент которого равен исходному элементу умноженному на -2
'''

# example_1

list_1 = [1, 4, 7, 11]
x = 0
new_list = []
while x < len(list_1):
    new_list.append(list_1[x] * -2)
    x += 1
print(new_list)



# example_2

list_1 = [1, 4, 7, 11]
list_2 = []
for i in list_1:
    list_2.append(i * -2)

print(list_2)
