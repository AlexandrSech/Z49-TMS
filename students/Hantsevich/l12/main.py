from classes import Circle, Triangle, Square, Point


p = Point(1, 3)
ci = Circle(p, 5)
ci.perimeter()
ci.square()


p1 = Point(2, 1)
p2 = Point(7, 2)
p3 = Point(1, 5)

tr = Triangle(p1, p2, p3)
tr.perimeter()
tr.square()


p4 = Point(2, 2)
p5 = Point(4, 4)

sq = Square(p4, p5)
sq.perimetr()
sq.square()


figures = [ci, tr, sq]

for i in figures:
    i.square()