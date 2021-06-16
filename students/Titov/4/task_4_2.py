spis = [0, 3, 14, -19, 10, 973]
a = 0
e = 0
while e < len(spis):
    if spis[e] % 2 == 0:
        a += 1
    e += 1
print(a)
exit()
for el in range(len(spis)):
    if spis[el] % 2 == 0:
        a += 1
print(a)