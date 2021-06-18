from abc import ABCMeta, abstractmethod

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


class Point:  # Класс описывающий координату точки
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


class Figure(metaclass=ABCMeta):  # Абстрактный класс произвольной фигуры, все методы обязательны для переопределения
    @abstractmethod
    def perimetr(self):  # Периметр
        raise NotImplementedError("Необходимо переопределить метод")

    @abstractmethod
    def area(self):  # Площадь
        raise NotImplementedError("Необходимо переопределить метод")


class Circle(Figure):  # Круг
    centre: Point  # Центр круга
    __radius: float  # Радиус

    def __init__(self, centre, radius):
        self.centre = centre
        self.__radius = radius

    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self, radius):
        self.__radius = radius

    def area(self):
        print(f"Площадь круга равна {round(3.14 * self.radius ** 2, 2)}")

    def perimetr(self):
        print(f"Пeриметр круга равен {round(2 * 3.14 * self.radius, 2)}")


class Triangle(Figure):
    a: Point  # Точка А треугольника с координатами х, у
    b: Point  # Точка В треугольника с координатами х, у
    c: Point  # Точка С треугольника с координатами х, у

    __perim: float  # Периметр треугольнка
    __l1: float  # Длинны сторон треугольника
    __l2: float
    __l3: float

    def __init__(self, p1, p2, p3):
        self.a = p1
        self.b = p2
        self.c = p3

    def perimetr(self):
        self.__l1 = ((abs(self.b.x - self.a.x)) ** 2 + (abs(self.b.y - self.a.y)) ** 2) ** (1 / 2)
        self.__l2 = ((abs(self.c.x - self.a.x)) ** 2 + (abs(self.c.y - self.a.y)) ** 2) ** (1 / 2)
        self.__l3 = ((abs(self.c.x - self.b.x)) ** 2 + (abs(self.c.y - self.b.y)) ** 2) ** (1 / 2)
        self.__perim = self.__l1 + self.__l2 + self.__l3
        print(f"Периметр треугольника равен: {round(self.__perim, 2)}")

    def area(self):
        per = self.__perim / 2  # Полупериметр
        s = (per * (per - self.__l1) * (per - self.__l2) * (per - self.__l3)) ** (1 / 2)
        print(f"Площадь треугольника равна: {round(s, 2)}")


class Square(Figure):
    a: Point  # Точка А квадрата с координатами х, у
    b: Point  # Точка В квадрата с координатами х, у

    __l1: float  # Длинна стороны квадрата

    def __init__(self, p1, p2):
        self.a = p1
        self.b = p2
        self.__l1 = ((abs(self.b.x - self.a.x)) ** 2 + (abs(self.b.y - self.a.y)) ** 2) ** (1 / 2)

    def perimetr(self):
        print(f"Периметр квадрата равен: {self.__l1 * 4}")

    def area(self):
        print(f"Площадь квадрата равена: {self.__l1 ** 2}")
