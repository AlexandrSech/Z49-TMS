m = int(input("Введите m: "))
n = int(input("Введите n: "))

for i in range(m, n+1):
    print(i, ": ", end=" ")
    for j in range(1, i):
        if  j != 1 and j != i and i % j == 0:
            print(j, end = " ")
    print(end="\n")