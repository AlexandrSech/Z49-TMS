l1 =[1,2,3,4,5,]
l1.insert(0, 0)
print(l1)


exit()

from abc import ABC, abstractmethod
import time


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
        print('Animal init')

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


class A1():
    name: str

    def __init__(self, _name):
        self.name = _name
        print('a1')


class Dog(Animal):
    flea = False

    def __init__(self, flea, *animal): #, name, weight, height, age, color, vertebrate, male):
        super().__init__(*animal)
        # Animal.__init__(self, *animal)

        self.flea = flea
        print('dog')


    def breathe(self):
        pass

    def eat(self):
        pass

    def move(self):
        pass

    def voice(self):
        pass


d1 = Dog(True, 'dog', 1,2,3, 'red', False, True)


