"""
Создать класс Car. Атрибуты: марка, модель, год  выпуска, скорость(поумолчанию 0).
Методы: увеличить скорости(скорость + 5), уменьшени ескорости(скорость  - 5),
стоп(сброс скорости на 0), отображение скорости,
разворот(изменение знака скорости). Все атрибуты приватные.
"""


class Car:
    __mark: str  # Марка
    __model: str  # Модель
    __year: int  # Год выпуска
    __speed: int = 0  # Скорость
    __side: str = '+'  #  Направление



    def __init__(self, mark, model, year, speed):
        self.__mark = mark
        self.__model = model
        self.__year = year
        self.__speed = speed

    @property
    def mark(self):
        return self.__mark

    @mark.setter
    def mark(self, mark):
        if mark.lower().isalpha():
            self.__mark = mark
        else:
            print("Wrong Mark")


    def model(self):
        return self.__model


    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, year):
        if 1887 < year < 2021:
            self.__year = year
        else:
            print("This auto was not/ is not invented")

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, speed):
        if speed > 350:
            print("You cant be that fast, u know?!")
        else:
            self.__speed = speed

    def speed_up(self):  # Увеличение скорости
        if self.__speed >= 346:
            print('U cant be so fast')
        elif self.__speed <= 345:
            self.__speed += 5
        return self.__speed

    def speed_down(self):  # Уменьшение скорости
        if self.__speed <=5:
            self.__speed = 0
            print('You stopped')
        elif self.__speed > 5:
            self.__speed -= 5
        return self.__speed

    def stop(self):  # Остановка
        self.__speed = 0
        return self.__speed

    def revere(self):  # Разворот
        if self.__side == '+':
            self.__side = '-'
        else:
            self.__side = '+'

    def display(self):  # Текущая скорость
        print(self.__side, self.__speed)

a = Car('Bra', 'Bru', 1992, 200)
print(a.mark, a.model(), a.year, a.speed)
a.speed_up()
a.display()
a.revere()
a.display()
a.speed_down()
a.display()
a.stop()
a.display()