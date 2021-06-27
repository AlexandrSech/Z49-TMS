import math


def deco1(foo):
    def inner(*args):
        try:
            return foo(*args)
        except ZeroDivisionError as zz:
            print('dont divide on zero bitch')
        except Exception as my_ex:
            print('some error: {}'.format(my_ex))
    return inner


def logger(foo):
    def inner(*args):
        with open('logs/25062021.log', 'a') as l_file:
            l_file.write(str(foo(*args)) + '\n')
    return inner





class MyPi:
    max: int

    def __init__(self, max):
        self.max = max

    def ff(self, i):
        if i == 0:
            return 1
        rez = 1
        for ii in range(1, i+1):
            rez *= ii
        return rez

    @deco1
    def calc(self):
        sum = 0
        k = 0
        # for k in range(self.max):
        while True:
            sum += (self.ff(4 * k) / (self.ff(k) ** 4)) * ((1103 + 26390 * k) / ((4 * 99) ** (4 * k)))
            k += 1
            yield 9801 / ((2 * (2 ** (1/2))) * sum)

    @deco1
    @logger
    def manager(self):
        o_gen = self.calc()
        r = 0
        for _ in range(self.max):
            r = next(o_gen)
        return r


if __name__ == '__main__':
    for i in range(-10, 1000):
        c1 = MyPi(i)
        r = c1.manager()
        print(r)



