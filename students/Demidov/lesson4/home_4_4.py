l = [1, 2, 3, 4, 5,]

for index in range(len(l) -1):
    # l[index], l[index + 1] = l[index + 1], l[index]
    temp = l[index]
    l[index] = l[index + 1]
    l[index + 1] = temp
    print(l)

n = 0
l = [1, 2, 3, 4, 5,]
while n < len(l):
    temp = l[n]
    l[n] = l[n + 1]
    l[n + 1]
    print(l)