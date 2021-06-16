"""
Создать пять классов описывающие реальные объекты. Каждый класс
должен содержать минимум три приватных атрибута, конструктор, геттеры
и сеттеры для каждого атрибута, два метода.
"""


class Pet:
    __weight: float  # Вес
    __height: int  # Рост
    __name: str  # Имя
    __age: float  # возраст

    def __init__(self, weight, height, name, age):
        self.__weight = weight
        self.__height = height
        self.__name = name
        self.__age = age

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, weight):
        if float(weight) <= 0:
            print("Wrong weight")
        else:
            self.__weight = float(weight)

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if int(height) < 0:
            print("Wrong height")
        else:
            self.__height = int(height)


    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if float(age) <= 0:
            print("Wrong age")
        else:
            self.__height = int(height)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if name.isalpha():
            self.__name = name
        else:
            print("Wrong Name")

    def Jump(self):
        print(self.__name, "прыгает!")

    def Alive(self):
        if self.__age < 20:
            print(self.__name, "жив!")
        else:
            print('Sorry, man, its dead. -_-')


class Dog(Pet):

    def __init__(self, weight, height, name, age):
        super().__init__(weight, height, name, age)
        self.__weight = weight
        self.__height = height
        self.__name = name
        self.__age = age

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if int(height) < 10:
            print("Wrong height")
        else:
            pet.__height = int(height)

    def Bark(self):
        print(self.__name, ': Brrr Raf raf Raf')


class Cat(Pet):

    def __init__(self, weight, height, name, age):
        super().__init__(weight, height, name, age)
        self.__weight = weight
        self.__height = height
        self.__name = name
        self.__age = age


    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if int(height) < 5:
            print("Wrong height")
        else:
            self.__height = int(height)

    def Meow(self):
        print(self.__name, ': meow meow')


class Parrot(Pet):

    def __init__(self, weight, height, name, age):
        super().__init__(weight, height, name, age)
        self.__weight = weight
        self.__height = height
        self.__name = name
        self.__age = age

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, weight):
        if float(weight) <= 0 or float(weight) > 2:
            print("Wrong weight")
        else:
            self.__weight = float(weight)

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if int(height) < 0 or int(height) > 15:
            print("Wrong height")
        else:
            self.__height = int(height)

    def Fly(self):
        print('Your', self.__name, 'flew away')


class Hamster(Pet):

    def __init__(self, weight, height, name, age):
        super().__init__(weight, height, name, age)
        self.__weight = weight
        self.__height = height
        self.__name = name
        self.__age = age

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, weight):
        if float(weight) <= 0 or float(weight) > 0.5:
            print("Wrong weight")
        else:
            self.__weight = float(weight)

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if int(height) < 0 or int(height) > 10:
            print("Wrong height")
        else:
            self.__height = int(height)

    def Voice(self):
        print('Your', self.__name, 'makes some weird noises')


class Turtle(Pet):

    def __init__(self, weight, height, name, age):
        super().__init__(weight, height, name, age)
        self.__weight = weight
        self.__height = height
        self.__name = name
        self.__age = age

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, weight):
        if float(weight) <= 0 or float(weight) > 50:
            print("Wrong weight")
        else:
            self.__weight = float(weight)

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if int(height) < 0 or int(height) > 60:
            print("Wrong height")
        else:
            self.__height = int(height)

    def Voice(self):
        print('Your', self.__name, 'is quiet like dead.')

    def Run(self):
        print('Your Turtle runs like a pro =)')

    def Alive(self):
        if self.__age < 200:
            print(self.__name, "жив!")
        else:
            print('Sorry, man, its dead. -_-')

    def Jump(self):
        print('Turtles cant jump -_-')


a = Turtle(20, 15, "Jack", 12)

print(a.name, a.weight, a.height, a.age)
a.Run()
a.Jump()
a.Voice()
a.Alive()
