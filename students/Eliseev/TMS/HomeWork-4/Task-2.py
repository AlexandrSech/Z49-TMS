list_1 = [1, 2, 3, 44, 5, 6, ]
x = 0
z = 0
y = 0
for el in list_1:
    if el % 2 == 0:
        x += 1
print(x)

while y < len(list_1):
    if list_1[y] % 2 == 0:
        z += 1
    y += 1
print(z)