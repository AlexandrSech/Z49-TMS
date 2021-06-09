x = [1, 2, 3, 1, 1, 1, 2, 3, 4, 5, 6, 1, 2, 3, 5, 6, 1, 1, 2, 3, ]
col = 0
i = 0
for el in x:
    if len(x) - i == 2:
        if el < x[i+1]:
            col += 1
    elif len(x) - i <= 1:
        continue
    elif el < x[i+1]:
        if x[i+1] > x[i+2]:
            col += 1
        pass
    i += 1
print(col)


