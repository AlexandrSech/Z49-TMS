list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, ]
list_2 = []
list_3 = []
x = 0
for el in list_1:
    if el == list_1[0]:
        continue
    list_2.append(el)
list_2.append(list_1[0])
print(list_2)

while x < (len(list_1) -1):
    x += 1
    y = list_1[x]
    list_3.append(y)

list_3.append(list_1[0])
print(list_3)