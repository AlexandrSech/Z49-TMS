"""
Создать класс Point, описывающий точку(атрибуты: x, y). Создать класс Figure.
Создать три дочерних класса Circle(атрибуты: координаты центра(тип Point),
длина радиуса; методы: нахождение периметра и площади окружности),
Triangle(атрибуты: три точки, методы: нахождение площади и периметра),
Square(атрибуты: две точки, методы: нахождение площади и периметра).
При потребности создавать все необходимыеметоды не описанные в задании.
Создать список фигур и в цикле подсчитать и вывести площади всех фигур на экран.
Примечание: в рамках задание создать два файла: classes.py и main.py.
Впервом будут описаны все классы, во втором классы будути мпортированы и использованы.
"""

from abc import ABCMeta, abstractmethod
import math


class Point:  # Класс описывающий точку(атрибуты: x, y)
    __x: int
    __y: int

    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        self.__y = y


class Figure:
    def perimeter(self):
        raise NotImplementedError("Abstract method error")

    def square(self):
        raise NotImplementedError("Abstract method error")


class Circle(Figure):
    centre: Point
    __radius: float

    def __init__(self, centre, radius):
        self.centre = centre
        self.__radius = radius

    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self, radius):
        self.__radius = radius

    def square(self):
        print("Площадь круга -", math.pi * (self.radius ** 2))

    def perimeter(self):
        print("Пeриметр круга -", 2 * math.pi * self.radius)


class Triangle(Figure):
    a: Point
    b: Point
    c: Point

    __p: float  # Периметр треугольнка
    __s1: float
    __s2: float
    __s3: float

    def __init__(self, p1, p2, p3):
        self.a = p1
        self.b = p2
        self.c = p3

    def perimeter(self):
        self.__s1 = ((abs(self.b.x - self.a.x)) ** 2 + (abs(self.b.y - self.a.y)) ** 2) ** 0.5
        self.__s2 = ((abs(self.c.x - self.a.x)) ** 2 + (abs(self.c.y - self.a.y)) ** 2) ** 0.5
        self.__s3 = ((abs(self.c.x - self.b.x)) ** 2 + (abs(self.c.y - self.b.y)) ** 2) ** 0.5
        self.__p = self.__s1 + self.__s2 + self.__s3
        print("Периметр треугольника -", self.__p)

    def square(self):
        p2 = self.__p / 2
        print("Площадь треугольника -", (p2 * (p2 - self.__s1) * (p2 - self.__s2) * (p2 - self.__s3)) ** (1 / 2))


class Square(Figure):
    a: Point
    b: Point

    __s1: float  # длина грани

    def __init__(self, p1, p2):
        self.a = p1
        self.b = p2
        self.__l1 = ((abs(self.b.x - self.a.x)) ** 2 + (abs(self.b.y - self.a.y)) ** 2) ** (1 / 2)

    def perimeter(self):
        print("Периметр квадрата -", self.__l1 * 4)

    def square(self):
        print("Площадь квадрата -", self.__l1 ** 2)