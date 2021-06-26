import math


class Point:
    x: float
    y: float
    z: float


class Circle(Point):

    def __init__(self, x, y, radius):
        Point.x = x
        Point.y = y
        self.radius = radius

    def find_perimeter(self):
        return 2 * math.pi * self.radius

    def find_square(self):
        return math.pi * (self.radius ** 2)


class Triangle(Point):

    def __init__(self, x, y, z):
        Point.x = x
        Point.y = y
        Point.z = z

    def find_perimeter(self):
        per = self.x + self.y + self.z
        return per

    def find_square(self):
        p = self.x + self.y + self.z
        square = (p * (p - self.x) * (p - self.y) * (p - self.z))**(1/2)
        return square


class Square(Point):

    def __init__(self, x, y):
        Point.x = x
        Point.y = y

    def find_perimeter(self):
        return (self.x * 2) + (self.y * 2)

    def find_square(self):
        return self.x * self.y


circle1 = Circle(10, 20, 15)

triangle1 = Triangle(10, 18, 11)

square1 = Square(10, 5)
print(triangle1.find_perimeter())


while True:
    print('Choose figure:')
    print('1. circle')
    print('2. triangle')
    print('3. square')
    print('0. exit')
    sign = input('enter ur choose: ')
    if sign == '1':
        print('1.1. output perimeter')
        print('1.2. output square')
        sign = input('enter ur choose: ')
        if sign == '1.1':
            print(circle1.find_perimeter())
            continue
        if sign == '1.2':
            print(circle1.find_square())
            continue
    if sign == '2':
        print('2.1. output perimeter')
        print('2.2. output square')
        sign = input('enter ur choose: ')
        if sign == '2.1':
            print(triangle1.find_perimeter())
            continue
        if sign == '2.2':
            print(triangle1.find_square())
            continue
    if sign == '3':
        print('3.1. output perimeter')
        print('3.2. output square')
        sign = input('enter ur choose: ')
        if sign == '3.1':
            print(square1.find_perimeter())
            continue
        if sign == '3.2':
            print(square1.find_square())
            continue
    if sign == '0':
        break


