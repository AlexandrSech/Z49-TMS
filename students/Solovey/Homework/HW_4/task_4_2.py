'''
2) Дан список целых чисел. Подсчитать сколько четных чисел в списке
'''

# examle_1

list_1 = [2, 3, 7, 12, 24, 76, 102, 118]
list_2 = []

for i in list_1:
    if i % 2 == 0:
        list_2.append(i)
print(len(list_2))



# example_2

list_1 = [2, 3, 7, 12, 24, 76, 102, 118]
list_2 = []
i = 0
while i < len(list_1):
    if list_1[i] % 2 == 0:
        list_2.append(list_1[i])
    i += 1
print(len(list_2))