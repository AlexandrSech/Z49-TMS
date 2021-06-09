spis = [0, 1]
i = 0
while i < 13:
    spis.append(spis[-1] + spis[-2])
    i += 1
print(spis)
exit()
for el in range(13):
    spis.append(spis[-1] + spis[-2])
print(spis)
