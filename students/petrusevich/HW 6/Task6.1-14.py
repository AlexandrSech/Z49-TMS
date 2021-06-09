import random
n, m = int(input()), int(input())
a, b = int(input()), int(input())
for i in range(n):
    print()
    for j in range(m):
        print(random.randrange(a, b), end=' ')