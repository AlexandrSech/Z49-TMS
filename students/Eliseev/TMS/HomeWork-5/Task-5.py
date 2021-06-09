x = [11, 24, 54, 1, 42, 53, 5, 2313, 54, 2, 10, 21, 6, 124, 109, 9, 89, 54, 12, ]
max_el = max(x)
i = 0
for el in x:
    if el % 2 == 0:
        x[i] = max_el
    i += 1
print(x)