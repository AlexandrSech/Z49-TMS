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
        self.mark = mark
        self.model = model
        self.year = year
        self.speed = speed

    @property
    def mark(self):
        return self.__mark

    @mark.setter
    def mark(self, mark):
        try:
            if mark.lower().isalpha():
                self.__mark = mark
            else:
                print("Некоректрно указана марка автомобиля!")
        except:
            print('Не корректно указана марка')
            self.__mark = ''

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, model):
        self.__model = model

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, year):
        try:
            year = int(year)
            if 1950 < year < 2021:
                self.__year = year
            else:
                print("Не верно указан год автомобиля!")
        except:
            print('Не корректно указан год')
            self.__year = 0

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, speed):
        try:
            speed = int(speed)
            if speed < 0 or speed > 350:
                print("Неверно указана скорость автомобиля")
                self.__speed = 0
            else:
                self.__speed = speed
        except:
            print("Неверно указана скорость автомобиля")
            self.__speed = 0

    def speed_inc(self):  # Увеличение скорости
        self.__speed += 5
        return self.__speed

    def speed_dec(self):  # Уменьшение скорости

        self.__speed -= 5
        if self.__speed <= 0:
            self.__speed = 0
            return self.__speed
        else:
            return self.__speed

    def stop(self):  # Остановка
        self.__speed = 0
        return self.__speed

    def reversal(self):  # Разворот
        self.__speed *= (-1)
        return self.__speed

    def display(self):  # Вывод на экран текущей скорости
        print(self.__speed)


car = Car(111, "Camry", 2005, -25)
print(car.mark)
print(car.speed)
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
