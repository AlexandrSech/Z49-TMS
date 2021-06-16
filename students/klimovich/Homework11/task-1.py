'''
1. Создать пять классов описывающие реальные объекты. Каждый класс
должен содержать минимум три приватных атрибута, конструктор, геттеры
и сеттеры для каждого атрибута, два метода.
'''


class Building:
    __square: float
    __width: float
    __height: float

    def __init__(self, square, width, height):
        self.__square = square
        self.__width = width
        self.__height = height

    def print_passport(self):
        print(self.__width, self.__square, self.__height)


class Shop(Building):
    name: str
    street: str

    def __init__(self, __square, __width, __height, name, street):
        # Необходимо вызвать метод инициализации родителя.
        # В Python 3.x это делается при помощи функции super()
        super().__init__(__square, __width, __height)
        self.name = name
        self.street = street

    def print_passport(self):
        super().print_passport()
        print(self.name, self.street)

    def set_name(self, new_name):  # сеттер для имени
        self.name = new_name

    def get_name(self):  # геттер для имени
        return self.name

    def set_street(self, new_street):  # сеттер для street
        self.street = new_street

    def get_street(self):  # геттер для street
        return self.street



shop1 = Shop(10, 20, 30, 'EVROOPT', 'Street №10')
print(shop1.get_name())
shop1.print_passport()


class Bank(Building):
    name: str
    street: str

    def __init__(self, __square, __width, __height, name, street):
        # Необходимо вызвать метод инициализации родителя.
        # В Python 3.x это делается при помощи функции super()
        super().__init__(__square, __width, __height)
        self.name = name
        self.street = street

    def print_passport(self):
        super().print_passport()
        print(self.name, self.street)

    def set_name(self, new_name):  # сеттер для имени
        self.name = new_name

    def get_name(self):  # геттер для имени
        return self.name

    def set_street(self, new_street):  # сеттер для street
        self.street = new_street

    def get_street(self):  # геттер для street
        return self.street


bank1 = Bank(100, 230, 433, 'MainBankOfMinsk', 'MainStreet')
bank1.print_passport()
print(bank1.get_street(), bank1.get_name())
exit()


class School:

    def __init__(self, name, square, width, height, date_of_construction):
        self.name = name
        self.__square = square
        self.__width = width
        self.__height = height
        self.date_of_construction = date_of_construction
        print('object was created')

    def set_name(self, new_name):  # сеттер для имени
        self.name = new_name

    def get_name(self):  # геттер для имени
        return self.name

    def get_width(self):  # геттер для ширины
        return self.__width

    def set_width(self, new_width):  # сеттер для ширины
        self.__width = new_width

    def print_data(self):
        print(self.name, self.__square, self.__width, self.__height, self.date_of_construction)

    def print_welcome_message(self):
        print('Приглашаем в школу {}'.format(self.name))

school = School('HighSchool#3', 10000, 500, 200, '1980-01-01')
school.print_data()
school.set_name('sdf')
school.set_width(1000)
school.print_data()
school.print_welcome_message()
print(school.get_name())
