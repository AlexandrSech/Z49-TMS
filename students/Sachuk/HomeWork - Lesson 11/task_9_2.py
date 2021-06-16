"""
Создать класс Car. Атрибуты: марка, модель, год выпуска, скорость(по
умолчанию 0). Методы: увеличить скорости(скорость + 5), уменьшение
скорости(скорость - 5), стоп(сброс скорости на 0), отображение скорости,
разворот(изменение знака скорости). Все атрибуты приватные.
"""


class Car:
    __mark = str  # Марка автомобиля
    __model = str  # Модель
    __type_body = str  # Тип кузова
    __equipment = str  # Комплектация
    __transmission = str  # Коробка передач (автомат, механика, робот)
    __color = str  # Цвет
    __engine_type = str  # Тип двигателя (бензин, дизель, электро)
    __engine_volume = float  # Объём двигателя
    __year = int  # Год выпуска
    __radius_wheel = int  # Радиус колеса
    __speed = 0  # Скорость ( по умолчанию 0)
    __resource = 30  # Ресурс двигателя до ремонта
    __balance_owner = 100  # Баланс владельца

    def __init__(self, mark, model, type_body, equipment, transmission, color,
                 engine_type, engine_volume, year, radius_wheel):
        self.__mark = mark
        self.__model = model
        self.__type_body = type_body
        self.__equipment = equipment
        self.__transmission = transmission
        self.__color = color
        self.__engine_type = engine_type
        self.__engine_volume = engine_volume
        self.__year = year
        self.__radius_wheel = radius_wheel

    def __del__(self):
        return None

    @property
    def mark(self):
        return self.__mark

    @mark.setter
    def mark(self, mark):
        self.__mark = mark

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, model):
        self.__model = model

    @property
    def type_body(self):
        return self.__type_body

    @type_body.setter
    def type_body(self, type_body):
        self.__type_body = type_body

    @property
    def equipment(self):
        return self.__equipment

    @equipment.setter
    def equipment(self, equipment):
        self.__equipment = equipment

    @property
    def transmission(self):
        return self.__transmission

    @transmission.setter
    def transmission(self, transmission):
        self.__transmission = transmission

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, color):
        self.__color = color

    @property
    def engine_type(self):
        return self.__engine_type

    @engine_type.setter
    def engine_type(self, engine_type):
        self.__engine_type = engine_type

    @property
    def engine_volume(self):
        return self.__engine_volume

    @engine_volume.setter
    def engine_volume(self, engine_volume):
        self.__engine_volume = engine_volume

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, year):
        self.__year = year

    @property
    def radius_wheel(self):
        return self.__radius_wheel

    @radius_wheel.setter
    def radius_wheel(self, radius_wheel):
        self.__radius_wheel = radius_wheel

    @property
    def speed(self):
        return self.__speed

    def show_info(self):
        return f'Car : {self.mark} \nModel : {self.model} \nType body : {self.type_body} ' \
               f'\nEquipment : {self.equipment}' \
               f'\nTransmission : {self.transmission} \nColor : {self.color} \nEngine type : {self.engine_type}' \
               f'\nEngine volume : {self.engine_volume} \nYear : {self.year} \nRadius_wheel : {self.radius_wheel} '

    def speed_up(self):
        if self.__resource < 1:
            print(f'Машина сломана, нужно срочно делать ремонт. Вызовите соответсвующий метод')
            return self.stop()
        self.__speed = self.speed + 5
        self.__resource = self.__resource - 5
        if 0 < self.__resource < 10:
            print(f'Осталось проехать {self.__resource} и нужно будет делать ТО')
        return self.speed

    def speed_down(self):
        if self.__resource < 1:
            print(f'Машина сломана, нужно срочно делать ремонт. Вызовите соответсвующий метод')
            self.__speed = 0
            return self.stop()
        self.__speed = self.speed - 5
        self.__resource = self.__resource - 3
        if 0 < self.__resource < 10:
            print(f'Осталось проехать {self.__resource} и нужно будет делать ТО')
        return self.speed

    def stop(self):
        self.__speed = 0
        return self.speed

    def show_speed(self):
        return self.speed

    def reverse(self):
        self.__speed = - self.speed
        return self.speed

    def remote(self):
        self.__price = 50
        self.__resource = 50
        if self.__balance_owner > self.__price:
            self.__balance_owner = self.__balance_owner - self.__price
        else:
            print(f'У вас не хватает денег на ремонт. МАШИНУ ВЕЗЁМ В ГАТОВО. А объект {x.__str__()} будет уничтожен '
                  f'при вызове метода Crash')
    def crash(self):
        return self.__del__()

x = Car('Toyota', 'Avensis', 'Universal', 'Sport', 'Mechanical', 'black', 'petrol', 2.0, 1999, 16)
print(x.show_info())
x.speed_up()
print(x.speed)
x.speed_up()
x.speed_up()
x.speed_up()
print(x.reverse())
x.speed_up()
x.speed_up()
print(x.speed)
print(x.speed_up())
x.crash()
x.remote()
print(x.speed_up())
x.speed_up()
print(x.reverse())
print(x.speed_up())
print(x.speed)