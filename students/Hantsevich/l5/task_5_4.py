n = int(input("Введите число: "))
m = 0
a = 0
for i in range (1,n):
    a += 1 / (m + 1)
    m += 1
print(a)