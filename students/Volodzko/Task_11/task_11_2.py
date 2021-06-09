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
            print("Некоректрно указана марка автомобиля!")

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, model):
        if model.lower().isalpha():
            self.__model = model
        else:
            print("Некоректрно указана марка автомобиля!")

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, year):
        if 1950 < year < 2021:
            self.__year = year
        else:
            print("Не верно указан год автомобиля!")

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, speed):
        if 0 > speed > 350:
            print("Неверно указана скорость автомобиля")
        else:
            self.__speed = speed

    def speed_inc(self):  # Увеличение скорости
        self.__speed += 5
        return self.__speed

    def speed_dec(self):  # Уменьшение скорости
        self.__speed -= 5
        return self.__speed

    def stop(self):  # Остановка
        self.__speed = 0
        return self.__speed

    def reversal(self):  # Разворот
        self.__speed *= (-1)
        return self.__speed

    def display(self):  # Вывод на экран текущей скорости
        print(self.__speed)


car = Car("Toyota", "Camry", 2005, 25)
car.speed_inc()
car.display()
car.stop()
car.speed_inc()
car.display()
car.speed_inc()
car.display()
car.speed_dec()
car.display()
car.speed_dec()
car.reversal()
car.display()
car.speed_inc()
car.display()
car.speed_inc()
car.display()
car.speed_inc()
car.display()
car.speed_dec()
car.display()
car.speed_dec()
car.display()
car.speed_dec()
car.display()
car.speed_dec()
car.display()
car.speed_dec()
car.display()
