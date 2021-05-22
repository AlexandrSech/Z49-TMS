a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, ]
b = len([i for i in a if i % 2 == 0])
print(b)


j = 0
p = 0
c = len(a)
while j < c:
        p += a[j] % 2 == 0
        j += 1
print(p)
