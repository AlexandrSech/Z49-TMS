spis =[1, 2, 3, 4, 5, 6, ]
a, *b, c = spis
print(a, b, c)

exit()
class House:
    len: int
    wid: int
    hei: int
    def __init__(self, len, wid, hei):
        self.len = len

    def get_size(self):
        return [self.len, self.wid, self.hei]


office = House()
office.len = 1
office.wid = 1
office.hei = 1
print(office.get_size())

exit()
def foo():
    l = [item for item in range(100) if item % 2 == 1]
    return l

def foo2(l1 = foo()):
    return {i: i**3 for i in l1}

print('\n'.join([k, v] for k, v in foo().items()))

exit()
def func(m, n):
    m += 1
    if m == n:
        return 50
    else:
        print(m)
        return(func(m, n))
print(func(0, 50))



exit()
import random
spis = []
m = 0
n = 3
for i in range(4):
    spis.append([])
    for j in range(4):

        if i == j:
            spis[i].append(1)
        elif i == m and j == n:
            spis[i].append(1)
        else:
            spis[i].append(0)
    m += 1
    n -= 1
    print(spis[i])
for i in range(len(spis)):
    for j in range(len(spis[i])):
        pass





exit()
for i in range(200, 301): #220
    sum_of_divide = 0
    n = 0
    for x in range(1, i):
        if i % x == 0:
            sum_of_divide += x

    for j in range(1, sum_of_divide):
        if sum_of_divide % j == 0:
            n += j

    if i == n and i != sum_of_divide and i == min(i, sum_of_divide):
        print(i, sum_of_divide)