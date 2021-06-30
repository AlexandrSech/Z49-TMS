'''Создать пять классов описывающие реальные объекты. Каждый класс
должен содержать минимум три приватных атрибута, конструктор, геттеры
и сеттеры для каждого атрибута, два метода.'''

class dog():
    def __init__(self, weight, height, age):
        self.__weight = weight
        self.__height = height
        self.__age = age

    def getter(self):
        return self.__age
    def setter(self, age):
        self.__age = age

    def Burk(self):
        print("burk burk burk")

    def Eat(self):
        print("i'm eating")

class plain():
    def __init__(self, length, color, speed):
        self.__length = length
        self.__color = color
        self.__speed = speed

    def getter(self):
        return self.__age
    def setter(self, age):
        self.__age = age

    def Fly(self):
        print('just flying')

    def Land(self):
        print('getting lower')

class car():
    def __init__(self, age, color, horsepower):
        self.age = age
        self.color = color
        self.horsepower = horsepower

    def getter(self):
        return self.__age
    def setter(self, age):
        self.__age = age

    def ride(self):
        print('run Vasya run')

    def crack(self):
        print('i need to repair some things')


class cat():
    def __init__(self, gender, weight, age):
        self.age = age
        self.gender = gender
        self.weight = weight

    def getter(self):
        return self.__age
    def setter(self, age):
        self.__age = age

    def mau(self):
        print('maau')

    def jump(self):
        print('jump')

class tree():
    def __init__(self, name, height, size):
        self.size = size
        self.name = name
        self.height = height

    def getter(self):
        return self.__size
    def setter(self, size):
        self.__age = size

    def grow(self):
        print('10 years later')

    def fall(self):
        print("CRACKKKKKK")