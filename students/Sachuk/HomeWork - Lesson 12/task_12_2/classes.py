"""
Создать класс Point, описывающий точку(атрибуты: x, y). Создать класс
Figure. Создать три дочерних класса Circle(атрибуты: координаты
центра(тип Point), длина радиуса; методы: нахождение периметра и
площади окружности), Triangle(атрибуты: три точки, методы: нахождение
площади и периметра), Square(атрибуты: две точки, методы: нахождение
площади и периметра). При потребности создавать все необходимые
методы не описанные в задании. Создать список фигур и в цикле
подсчитать и вывести площади всех фигур на экран[my-oop-03]
Примечание: в рамках задание создать два файла:  classes.py и main.py. В
первом будут описаны все классы, во втором классы будут
импортированы и использованы.
"""
import math
from abc import ABC


class Point(ABC):
    x: int
    y: int

    def area(self):
        pass

    def perimeter(self):
        pass


class Figure(Point):
    pass


class Circle(Figure):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def perimeter(self):
        return 2 * 3.14 * abs(self.x - self.y)

    def area(self):
        return 3.14 * ((abs(self.x - self.y)) ** 2)


class Triangle(Figure):
    z: int

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def half_perimeter(self):
        return (abs(self.x - self.y) + abs(self.y - self.z) + abs(self.x - self.z)) / 2

    def perimeter(self):
        return abs(self.x - self.y) + abs(self.y - self.z) + abs(self.x - self.z)

    def area(self):
        print(self.half_perimeter())
        return (self.half_perimeter() * (self.half_perimeter() - abs(self.x - self.y)) *
                (self.half_perimeter() - abs(self.y - self.z)) * (
                        self.half_perimeter() - abs(self.x - self.z))) / 0.5


class Square(Figure):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def perimeter(self):
        return 4 * abs(self.x - self.y)

    def area(self):
        return abs(self.x - self.y) * abs(self.x - self.y)
