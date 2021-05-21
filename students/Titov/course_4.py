import random
spis = []
m = 0
n = 3
for i in range(4):
    spis.append([])
    for j in range(4):

        if i == j:
            spis[i].append(1)
        elif i == m and j == n:
            spis[i].append(1)
        else:
            spis[i].append(0)
    m += 1
    n -= 1
    print(spis[i])
for i in range(len(spis)):
    for j in range(len(spis[i])):
        print(0)





exit()
for i in range(200, 301): #220
    sum_of_divide = 0
    n = 0
    for x in range(1, i):
        if i % x == 0:
            sum_of_divide += x

    for j in range(1, sum_of_divide):
        if sum_of_divide % j == 0:
            n += j

    if i == n and i != sum_of_divide and i == min(i, sum_of_divide):
        print(i, sum_of_divide)