"""def outer(niz, verh):
    def inner():
        if niz < verh:"""
def fact(f):
    m = 0
    for i in range(f + 1):
        m += i
    return m
def otric(k):
    if k < 0:
        k *= -1
    return k
def epsil(niz, verh):
    m = 0
    for i in range(niz, verh + 1):
        m += i
    return m

k = int(input('Введите число к '))
besk = int(input('Введите '))
first = 2 * 2 ** (1 / 2) * epsil(k, besk) * (fact(4 * k) / fact(k) ** 4)
second = otric(1103 + 26390 * k) / (4 * 99) ** (4 * k)
fact = 9801 / (first * second)
print(fact, first, second, 9801 / 1100 * (27493 / (396 ** 4)))