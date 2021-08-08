import unittest
from Task_12_2.classes import *


class TestTask_12_2(unittest.TestCase):
    def my_object(self, x, y, x_r, y_r):
        point = Point(x, y)
        self.assertEqual(point.x, x_r)
        self.assertEqual(point.y, y_r)

    def test_Mytime(self):
        self.my_object(10, 15, 10, 15)
        self.my_object(50, 70, 50, 70)
        self.my_object(-10, -20, -10, -20)
        self.my_object("10", "20", 10, 20)
        self.my_object("aa", "bb", None, None)

    def test_Circle(self):
        p = Point(3, 2)
        c = Circle(p, 10)
        self.assertEqual(c.radius, 10)
        self.assertEqual(c.area(), 314)
        self.assertEqual(c.perimetr(), 62.8)

        c2 = Circle(p, "szd")
        self.assertEqual(c2.radius, None)
        self.assertEqual(c2.area(), None)
        self.assertEqual(c2.perimetr(), None)

        c3 = Circle(p, "10")
        self.assertEqual(c3.radius, 10)
        self.assertEqual(c3.area(), 314)
        self.assertEqual(c3.perimetr(), 62.8)

        c4 = Circle(p, 2.5)
        self.assertEqual(c4.radius, 2.5)
        self.assertEqual(c4.area(), 19.62)
        self.assertEqual(c4.perimetr(), 15.7)

    def test_Triangle(self):
        p1 = Point(2, 3)
        p2 = Point(5, -1)
        p3 = Point(-2, 1)

        t = Triangle(p1, p2, p3)
        self.assertEqual(t.perimetr(), 16.75)

        p4 = Point("2", 3)
        p5 = Point(5, -1)
        p6 = Point(-2, 1)

        t = Triangle(p4, p5, p6)
        self.assertEqual(t.perimetr(), 16.75)

        p7 = Point(2, 3)
        p8 = Point("sd", -1)
        p9 = Point(-2, 1)

        t = Triangle(p7, p8, p9)
        self.assertEqual(t.perimetr(), None)

    def test_Square(self):
        p1 = Point(2, 3)
        p2 = Point(4, 8)
        s = Square(p1, p2)
        self.assertEqual(s.perimetr(), 21.56)
        self.assertEqual(s.area(), 29.05)

        p3 = Point("2", 3)
        p4 = Point(4, 8)
        s = Square(p3, p4)
        self.assertEqual(s.perimetr(), 21.56)
        self.assertEqual(s.area(), 29.05)

        p5 = Point(2, 3)
        p6 = Point("ada", 8)
        s = Square(p5, p6)
        self.assertEqual(s.perimetr(), 0)
        self.assertEqual(s.area(), 0)

    if __name__ == '__main__':
        unittest.main()
