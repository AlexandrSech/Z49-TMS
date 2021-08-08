"""
Создать класс MyTime. Атрибуты: hours, minutes, seconds. Методы:
переопределить магические методы сравнения(==, !=, >=, <=, <, >),
сложения, вычитания, умножения на число, вывод на экран. Перегрузить
конструктор на обработку входных параметров вида: одна строка, три
числа, другой объект класса MyTime, и отсутствие входных параметров.
Реализовать нормальное отображение времени(​ 12:65:83​ - 13:06:23)
[my-oop-02] ​ Задание доделать в рамках cw12
"""

class MyTime:
    hours: int
    minutes: int
    seconds: int

    def __init__(self, strdate='', hours=0, minutes=0, seconds=0, object=None):
        if strdate:
            self.hours, self.minutes, self.seconds = strdate.split(':')
        elif hours or minutes or seconds:
            self.hours = hours
            self.minutes = minutes
            self.seconds = seconds
        elif  object:
           self.__dict__ = object.__dict__

    def __eq__(self, other):
        return self.hours == other.hours and self.minutes == other.minutes and self.seconds == other.seconds

    def __ne__(self, other):
        return self.hours != other.hours or self.minutes != other.minutes or self.seconds != other.seconds

    def __lt__(self, other):
        return self.hours * 3600 + self.minutes * 60 + self.seconds < other.hours * 3600 + other.minutes * 60 + \
               other.seconds
    def __gt__(self, other):
        return self.hours * 3600 + self.minutes * 60 + self.seconds > other.hours * 3600 + other.minutes * 60 + \
               other.seconds

    def __le__(self, other):
        return self.hours * 3600 + self.minutes * 60 + self.seconds <= other.hours * 3600 + other.minutes * 60 + \
               other.seconds

    def __ge__(self, other):
        return self.hours * 3600 + self.minutes * 60 + self.seconds >= other.hours * 3600 + other.minutes * 60 + \
               other.seconds


x = MyTime(hours=15, minutes=25, seconds=40)
print('bla-bla')
y = MyTime(strdate='16:38:49')
print('bla-bla')
z = MyTime(object=y)
print('bla-bla')
print(f'{x.hours}:{x.minutes}:{x.seconds}')
print(f'{y.hours}:{y.minutes}:{y.seconds}')
print(f'{z.hours}:{z.minutes}:{z.seconds}')
c = MyTime(strdate='18:45:00')
print(z > c)
print(z < c)
