'''Создать класс Car. Атрибуты: марка, модель, год выпуска, скорость(по
умолчанию 0). Методы: увеличить скорости(скорость + 5), уменьшение
скорости(скорость - 5), стоп(сброс скорости на 0), отображение скорости,
разворот(изменение знака скорости). Все атрибуты приватные.'''
class Car():

    __speed : int = 0

    def __init__(self, mark, model, year, speed = 0):
        self.__mark = mark
        self.__model = model
        self.__year = year
        self.__speed = speed

    def getter(self):
        return self.__speed

    def setter(self, speed):
        self.__speed = speed

    def increase(self):
        self.__speed += 5
        return self.__speed

    def decrease(self):
        self.__speed -= 5
        return self.__speed

    def stop(self):
        self.__speed = 0
        return self.__speed

    def spidometr(self):
        print(self.__speed)

    def reversal(self):
        self.__speed *= -1

a = Car('ford', 'mustang', 2010)
