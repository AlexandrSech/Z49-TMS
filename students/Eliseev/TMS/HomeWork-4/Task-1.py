list_1 = [1, 2, 3, 44, 5, 6, ]
list_2 = []
list_3 = []
x = 0
for el in list_1:
    list_2.append((el * 2))
print(list_2)
while x < len(list_1):
    list_3.append((list_1[x] * 2))
    x += 1
print(list_3)