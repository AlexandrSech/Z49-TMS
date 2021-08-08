from classes import Circle, Triangle, Square, Point

if __name__ == '__main__':
    print("Проверка!!!")
    print("Круг:")
    p = Point(3, 5)
    c1 = Circle(p, 5)
    c1.perimetr()
    c1.area()
    print("." * 50)

    print("Треугольник:")
    p1 = Point("dasda", 1)
    p2 = Point(5, 2)
    p3 = Point(1, 3)

    t1 = Triangle(p1, p2, p3)
    t1.perimetr()
    t1.area()
    print("." * 50)

    p4 = Point(0, 0)
    p5 = Point(3, 0)
    p6 = Point(0, 4)

    t2 = Triangle(p4, p5, p6)
    t2.perimetr()
    t2.area()
    print("." * 50)

    print("Квадрат:")
    p7 = Point(4, 4)
    p8 = Point(4, 8)

    s1 = Square(p7, p8)
    s1.perimetr()
    s1.area()
    print("=" * 50)

    """Создаём список фигур. Считаем и выводим площади на экран"""
    my_figure = [c1, t2, s1]

    for i in my_figure:
        i.area()
