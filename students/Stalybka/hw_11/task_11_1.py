"""
Создать пять классов описывающие реальные объекты. Каждый класс
должен содержать минимум три приватных атрибута, конструктор, геттеры
и сеттеры для каждого атрибута, два метода.
"""


class User:

    def __init__(self, login, password, age):
        self.__login = login
        self.password = password
        self.__age = age

    @property
    def login(self):
        return self.__login

    @login.setter
    def login(self, value):
        if not isinstance(value, str):
            raise ValueError('login must be string')
        self.__login = value

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value):
        if not isinstance(value, str) or len(value) < 6:
            raise ValueError('password must be string of 6 characters or more')
        self.__password = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if not isinstance(value, int):
            raise ValueError('age must be integer')
        if not 0 <= value <= 130:
            raise ValueError('incorrect age')
        self.__age = value

    def info(self):
        print(f'Login - {self.login}, age - {self.age}')


class Bike:

    def __init__(self, model, year, color, moving=False):
        self.__model = model
        self.__year = year
        self.__color = color
        self.moving = moving

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, value):
        if not isinstance(value, str):
            raise ValueError('model not found')
        self.__model = value

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, value):
        if not isinstance(value, int) or 2022 < value < 1818:
            raise ValueError('incorrect year')
        self.__year = value

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, value):
        self.__color = value
        print(f"you bike's color has been changed to {value}")

    def start_moving(self):
        self.moving = True

    def if_moving(self):
        if self.moving is True:
            return "you're still going"
        else:
            return 'better start moving'


class LordOfTheRings:
    health = 100
    sanity = 100

    def __init__(self, name, race, weapon, ring=False):
        self.__name = name
        self.__race = race
        self.__weapon = weapon
        self.ring = ring

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise ValueError('name must be string')
        if self.__name == 'sauron' or 'sauron'.capitalize():
            self.health = 1000
        self.__name = value.capitalize()

    @property
    def race(self):
        return self.__race

    @race.setter
    def race(self, value):
        if not isinstance(value, str):
            raise ValueError('race must be string')
        self.__race = value
        if value == 'orc' or 'orc'.capitalize():
            print('haha, sucks to suck')

    @property
    def weapon(self):
        return self.__weapon

    @weapon.setter
    def weapon(self, value):
        if not isinstance(value, str):
            raise ValueError('weapon cannot be recognised')

    def ring_found(self):
        self.ring = True
        self.sanity -= 50

    @staticmethod
    def fight(examp):
        LordOfTheRings.examp.health -= 20
        if LordOfTheRings.examp.health == 0:
            print('your opponent is already dead')

    def info(self):
        print(f"name - {self.name}, race - {self.race} \n"
              f"health - {self.health}, sanity - {self.sanity}")


class Paintball:

    def __init__(self, first_team, second_team, bullet_limit):
        self.__first_team = first_team
        self.__second_team = second_team
        self.__bullet_limit = bullet_limit
        self.compare_teams()

    def compare_teams(self):
        if abs(self.__first_team - self.__second_team) > 2:
            print('not fair team devision')

    @property
    def first_team(self):
        return self.__first_team

    @first_team.setter
    def first_team(self, value):
        if not isinstance(value, int):
            raise ValueError('must be integer')
        self.__first_team = value

    @property
    def second_team(self):
        return self.__second_team

    @second_team.setter
    def second_team(self, value):
        if not isinstance(value, int):
            raise ValueError('must be integer')
        self.__second_team = value

    @property
    def bullet_limit(self):
        return self.__bullet_limit

    @bullet_limit.setter
    def bullet_limit(self, value):
        if not isinstance(value, int):
            raise ValueError('must be integer')
        self.__bullet_limit = value

    def shoot(self):
        self.__bullet_limit -= 10
        return self.__bullet_limit


class Dog:

    def __init__(self, name, age, weight):
        self.__name = name
        self.__age = age
        self.__weight = weight

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError('name must be string')
        self.__name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if not isinstance(value, int):
            raise TypeError('name must be integer')
        if value < 0:
            raise ValueError("age can't be negative")
        self.__age = value

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError('weight must be integer or float')
        if value < 0:
            raise ValueError("weight can't be negative")
        self.__weight = value

    def feed(self, food: float or int):
        self.__weight += food

    def passport(self):
        print(f'Name - {self.__name}, age - {self.__age}, weight - {self.__weight}')
