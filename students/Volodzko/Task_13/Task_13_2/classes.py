from ui_func import IMathFunc
from exceptions import MyZeroException


class Math(IMathFunc):

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def my_sum(self, x, y):  # Функция сложения двух чсел
        return "x + y = {}".format(self.x + self.y)

    def my_dif(self, x, y):  # Функция вычитания двух чсел
        return "x - y = {}".format(self.x - self.y)

    def my_mul(self, x, y):  # Функция умножения двух чсел
        return "x * y = {}".format(self.x * self.y)

    def my_division(self, x, y):  # Функция деления двух чсел
        try:
            if self.y == 0:
                raise MyZeroException("Деление на ноль запрещено!")  # Генерируется собственное исключение
            else:
                return "x / y = {}".format(round(self.x / self.y, 4))
        except MyZeroException as ex:
            print(ex)
