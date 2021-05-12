"""
1) Введите число. Если это число делиться на 1000
без остатка, то выведите наэкран "millennium"
"""
x = int(input("Введите число: "))
if x % 1000 == 0:
    print("Millennium")
else:
    print(False)
