import math
a = input('Введите строку')
print(a[int(len(a)/2)], a[0])
if a[0] == a[int(len(a)/2)]:
    print(a[:math.ceil(len(a)/2)])
else:
    print(a[0])