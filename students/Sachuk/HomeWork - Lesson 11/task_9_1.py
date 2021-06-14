"""
Создать пять классов описывающие реальные объекты. Каждый класс
должен содержать минимум три приватных атрибута, конструктор, геттеры
и сеттеры для каждого атрибута, два метода.
"""
from time import sleep
import datetime
from abc import ABC, abstractmethod


class Animal(ABC):
    __weight = float  # Вес
    __height = float  # Рост
    __name = str  # тип животного
    __age = int  # Возраст
    __color = str  # Цвет
    __vertebrate = bool  # Позвоночное
    __male = str  # Пол

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, weight):
        self.__weight = weight

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        self.__height = height

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.__age = age

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, color):
        self.__color = color

    @property
    def vertebrate(self):
        return self.__vertebrate

    @vertebrate.setter
    def vertebrate(self, vertebrate):
        self.__vertebrate = vertebrate

    @property
    def male(self):
        return self.__male

    @male.setter
    def male(self, male):
        self.__male = male

    @abstractmethod
    def __init__(self, name, weight, height, age, color, vertebrate, male):
        self.name = name
        self.weight = weight
        self.height = height
        self.age = age
        self.color = color
        self.vertebrate = vertebrate
        self.male = male

    def sleep(self, time):
        print("я засыпаю")
        sleep(time)
        print('я проснулся')

    @abstractmethod
    def voice(self):
        pass

    @abstractmethod
    def move(self):
        pass

    @abstractmethod
    def eat(self):
        pass

    @abstractmethod
    def breathe(self):
        pass


class Bird(Animal):
    __wings = bool  # крылья

    @property
    def wings(self):
        return self.__wings

    @wings.setter
    def wings(self, wings):
        self.__wings = wings

    def __init__(self, name, weight, height, age, color, vertebrate, male, wings):
        self.name = name
        self.weight = weight
        self.height = height
        self.age = age
        self.color = color
        self.vertebrate = vertebrate
        self.male = male
        self.wings = wings

    def fly(self):
        print('Я умею летать')

    def move(self):
        print('Я умею ходить по земле')

    def eat(self):
        print('Ем жучков и паучков')

    def breathe(self):
        print('Дышу воздухом')

    def voice(self):
        print('Вообщем ЧИК-ЧИРИК')


class Fish(Animal):
    __gills = bool  # жабры
    __fish_fins = int  # количество

    @property
    def gills(self):
        return self.__gills

    @gills.setter
    def gills(self, gills):
        self.__gills = gills

    @property
    def fish_fins(self):
        return self.__fish_fins

    @fish_fins.setter
    def fish_fins(self, fish_fins):
        self.__fish_fins = fish_fins

    def __init__(self, name, gills, fish_fins, weight, height, age, color, vertebrate, male):
        self.name = name
        self.fish_fins = fish_fins
        self.gills = gills
        self.weight = weight
        self.height = height
        self.age = age
        self.color = color
        self.vertebrate = vertebrate
        self.male = male

    def swimm(self):
        print('Я умею плавать')

    def eat(self):
        print('Ем рыб меньше меня')

    def breathe(self):
        print("Дышу жабрами")

    def voice(self):
        print('')

    def move(self):
        pass


class Cat(Animal):
    __breed = str

    @property
    def breed(self):
        return self.__breed

    @breed.setter
    def breed(self, breed):
        self.__breed = breed

    def __init__(self, name, breed, weight, height, age, color, vertebrate, male):
        self.name = name
        self.breed = breed
        self.weight = weight
        self.height = height
        self.age = age
        self.color = color
        self.vertebrate = vertebrate
        self.male = male

    def night_vision(self):
        print('Я очень хорошо вижу ночью')

    def hunter(self, eat: object):
        print(f'{self.name} hunter on {eat.name}')

    def eat(self):
        print('ем мясо')

    def voice(self):
        print('МЯУУУУУУ')

    def move(self):
        print('хожу очень тихо на своих мягких лапках')

    def breathe(self):
        print('Дышу воздухом')


bird = Bird('Соловей', 3.0, 25.0, 1, 'black-white', True, True, True)
bird.eat()
bird.breathe()
bird.move()
bird.fly()
bird.voice()
bird.sleep(5)

fish = Fish('Сом', 3, True, 0.5, 10, 10, 'grey', True, False)
fish.eat()
fish.swimm()
fish.voice()
fish.breathe()
fish.move()
fish.sleep(2)

cat = Cat('Кот', 'персидский', 3, 5.0, 5, 'orange', True, True)
cat.eat()
cat.move()
cat.voice()
cat.breathe()
cat.night_vision()
cat.sleep(7)
cat.hunter(fish)
cat.hunter(bird)
