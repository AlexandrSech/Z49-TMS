from classes import Circle, Square, Triangle
figures = []
a = Circle(5, 10)
figures.append(a)
b = Square(1,5)
figures.append(b)
c = Triangle(7, 5, 6)
figures.append(c)

for i in figures:
    print(i.perimeter(), i.area())