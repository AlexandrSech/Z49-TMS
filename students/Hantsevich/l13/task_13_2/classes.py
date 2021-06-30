from exceptions import *


def number_check():
    while True:
        a = input('Введите число: ')
        if (a[0] == '-' and a[1::].isdigit()) or a.isdigit():
            break
        else:
            print("Вы ввели не число")
    return int(a)


class My_Math:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def sum(self):
        return "{} + {} = {}".format(self.a, self.b, self.a + self.b)

    def diff(self):
        return "{} - {} = {}".format(self.a, self.b, self.a - self.b)

    def multi(self):
        return "{} * {} = {}".format(self.a, self.b, self.a * self.b)

    @property
    def divide(self):
        try:
            if self.b == 0:
                raise MyZeroDivision("На ноль делить нельзя")
            else:
                return "{} / {} = {}".format(self.a, self.b, self.a / self.b)
        except MyZeroDivision as ex:
            return ex
