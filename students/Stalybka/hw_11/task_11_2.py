"""
Создать класс Car. Атрибуты: марка, модель, год выпуска, скорость(по
умолчанию 0). Методы: увеличить скорости(скорость + 5), уменьшение
скорости(скорость - 5), стоп(сброс скорости на 0), отображение скорости,
разворот(изменение знака скорости). Все атрибуты приватные.
"""


class Car:

    def __init__(self, brand, model, year, speed=0):
        self.__brand = brand
        self.__model = model
        self.__year = year
        self.__speed = speed

    @property
    def speed(self):
        return self.__speed

    def increase_speed(self):
        self.__speed += 5
        return self.__speed

    def decrease_speed(self):
        self.__speed -= 5
        return self.__speed

    def stop(self):
        self.__speed = 0
        return self.__speed

    def u_turn(self):
        self.__speed *= -1
        return self.__speed
