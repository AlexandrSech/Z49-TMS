mt = [[5, 9, 2, 4], [7, 3, 9, 1], [4, 9, 1, 3], [9, 4, 5, 7]]


for i in mt:
    print(i)
print("\n")

for item, value in enumerate(mt):
    max_value = 0
    r = 0
    for j in range(len(mt[item])):
        if mt[item][j] > max_value:
            max_value = mt[item][j]
            r = j
    mt[item][r] = mt[item][item]
    mt[item][item] = max_value



for i in mt:
    print(i)

