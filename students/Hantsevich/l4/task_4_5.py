'''
f1 = 1
f2 = 1
print(f1)
print(f2)
i = 0
while i < 15:
    f3 = f1 + f2
    f1 = f2
    f2 = f3
    i = i + 1
    print(f2)
'''
f1 = 1
f2 = 1
print(f1)
print(f2)
for i in range(15):
    f3 = f1 + f2
    f1 = f2
    f2 = f3
    print(f2)