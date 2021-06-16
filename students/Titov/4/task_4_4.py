spis = [1, 2, 3, 4, 5]
i = 0
while i < len(spis) - 1:
    spis[i], spis[i + 1] = spis[i + 1], spis[i]
    i += 1
print(spis)
exit()
for el in range(len(spis) - 1):
    spis[el], spis[el + 1] = spis[el + 1], spis[el]
print(spis)