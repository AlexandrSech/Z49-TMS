slov = {1: 'asd', 2: 'sdf', 3: 321}
print(slov.keys())
for i in slov:
    print(i, slov.get(i), ';;;;;;')
for i, j in enumerate(slov):
    print(i, j)