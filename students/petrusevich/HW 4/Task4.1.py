a = [1, 2, 3, 4, 5, 6, 7, ]
b = [(-2) * i for i in a]
print(b)



c = []
j = 0
while j < len(a):
    for i in a:
        c.append(i * (-2))
        j += 1
print(c)
