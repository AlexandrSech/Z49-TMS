"""
Создать класс MyTime. Атрибуты: hours, minutes, seconds.
Методы:переопределить магические методы сравнения(==, !=, >=, <=, <, >),
сложения, вычитания, умножения на число, вывод на экран.
Перегрузить конструктор на обработку входных параметров вида:
одна строка, три числа, другой объект класса MyTime, и отсутствие входных параметров.
Реализовать нормальное отображение времени(12:65:83 - 13:06:23)
"""


class MyTime:
    __hours: int = 0  # Часы
    __minutes: int = 0  # Минуты
    __seconds: int = 0  # Секунды

    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    @property
    def hours(self):
        return self.__hours

    @hours.setter
    def hours(self, hours):
        if hours > 24:
            self.__hours = hours % 24
        elif hours < 0:

            self.__hours = 24 - abs(hours) % 24
        else:
            self.__hours = hours

    @property
    def minutes(self):
        return self.__minutes

    @minutes.setter
    def minutes(self, minutes):
        if 0 <= minutes < 60:
            self.__minutes = minutes
        else:
            self.__hours += minutes // 60
            self.__minutes = minutes % 60

    @property
    def seconds(self):
        return self.__seconds

    @seconds.setter
    def seconds(self, seconds):
        if 0 <= seconds < 60:
            self.__seconds = seconds
        else:
            self.__minutes += seconds // 60
            self.__seconds = seconds % 60

    def __add__(self, other):  # Сложение времени
        return MyTime(self.hours + other.hours, self.minutes + other.minutes, self.seconds + other.seconds)

    def __sub__(self, other):  # Вычитание времени
        return MyTime(self.hours - other.hours, self.minutes - other.minutes, self.seconds - other.seconds)

    def __mul__(self, other):  # Умножение времени на число
        return MyTime(self.hours * other, self.minutes * other, self.seconds * other)

    def __eq__(self, other):  # Сравнение времени ==
        return self.hours == other.hours and self.minutes == other.minutes and self.seconds == other.seconds

    def __ne__(self, other):  # Сравнение времени !=
        return self.hours != other.hours and self.minutes != other.minutes and self.seconds != other.seconds

    def __lt__(self, other):  # Сравнение времени <
        return self.hours * 3600 + self.minutes * 60 + self.seconds < other.hours * 3600 + other.minutes * 60 + other.seconds

    def __gt__(self, other):  # Сравнение времени >
        return self.hours * 3600 + self.minutes * 60 + self.seconds > other.hours * 3600 + other.minutes * 60 + other.seconds
        # return self.hours > other.hours and self.minutes > other.minutes and self.seconds > other.seconds

    def __le__(self, other):  # Сравнение времени <=
        return self.hours * 3600 + self.minutes * 60 + self.seconds <= other.hours * 3600 + other.minutes * 60 + other.seconds

    def __ge__(self, other):  # Сравнение времени >=
        return self.hours * 3600 + self.minutes * 60 + self.seconds >= other.hours * 3600 + other.minutes * 60 + other.seconds

    def __str__(self):  # Вывод времени на экран
        return f"{self.hours}:{self.minutes}:{self.seconds}"


print("ПРОВЕРКА РАБОТЫ!!!!")

t1 = MyTime(-50, 100, 0)
print(t1)
t2 = MyTime(11, 30, 15)
print(t2)
t3 = MyTime(15, 20, 30)
print(t3)
print(t2 - t3)
print(t2 * 6)
print(t2 < t3)
print(t2 >= t3)
t4 = MyTime(11, 30, 15)
print(t2 == t4)
print(t2 == t3)
