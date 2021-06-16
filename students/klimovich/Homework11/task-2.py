'''2. Создать класс Car. Атрибуты: марка, модель, год выпуска, скорость(по
умолчанию 0). Методы: увеличить скорости(скорость + 5), уменьшение
скорости(скорость - 5), стоп(сброс скорости на 0), отображение скорости,
разворот(изменение знака скорости). Все атрибуты приватные.'''


class Car:
    __mark: str
    __model: str
    __year: int
    __speed: float = 0

    def __init__(self, mark, model, year, speed):
        self.__mark = mark
        self.__model = model
        self.__year = year
        self.__speed = speed

    def print_info(self):
        print(self.__mark, self.__model, self.__year, self.__speed)

    def add_speed(self):
        self.__speed += 5
        return self.__speed

    def del_speed(self):
        self.__speed -= 5
        return self.__speed

    def stop_dat_car(self):
        self.__speed = 0
        return self.__speed

    def check_my_speed(self):
        return self.__speed


car1 = Car('mercedes', 's-class', 2015, 200)
car1.print_info()
print(car1.add_speed())
car1.print_info()
print(car1.del_speed())
car1.print_info()
print(car1.stop_dat_car())
car1.print_info()
print(car1.check_my_speed())

