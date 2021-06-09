import datetime

"""
Создать пять классов описывающие реальные объекты.
Каждый класс должен содержать минимум три приватных атрибута,
конструктор, геттерыи сеттеры для каждого атрибута, два метода.
"""


class Dog:
    __weight: int  # Вес собаки
    __height: int  # Рост собаки
    __name: str  # Имя собаки

    def __init__(self, weigh, height, name):
        self.__weight = weigh
        self.__height = height
        self.__name = name

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, weight):
        if int(weight) < 0:
            print("Недопустимы вес для собаки!")
        else:
            self.__weight = int(weight)

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if int(height) < 10:
            print("Недопустимы рост для собаки")
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
            print("Некоректное имя!")

    def Jump(self):
        print("Собака прыгает!")

    def Run(self):
        print("Собака бегает! ")


class People:
    __name: str  # Имя
    __age: int  # Возраст
    __gender: str  # Пол

    def __init__(self, name, age, gender):
        self.__name = name
        self.__age = age
        self.__gender = gender

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if name.isalpha():
            self.__name = name
        else:
            print("Некоректное имя!")

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if 0 < int(age) < 125:
            self.__age = int(age)
        else:
            print("Недопустимы возраст для человека")

    @property
    def gender(self):
        return self.__gender

    @gender.setter
    def gender(self, gender):
        if gender.isalpha():
            self.__gender = gender
        else:
            print("Некоректно введён пол человека!")

    def Sleep(self, times: datetime.timedelta):
        print(times)
        if datetime.timedelta(hours=0, minutes=0) < times < datetime.timedelta(hours=6, minutes=0):
            print(f"{self.__name} спит!")
        else:
            print(f"{self.__name} бодрствует")

    def Work(self, times: datetime.timedelta):
        print(times)
        if datetime.timedelta(hours=8, minutes=0) < times < datetime.timedelta(hours=17, minutes=0):
            if datetime.timedelta(hours=12, minutes=0) < times < datetime.timedelta(hours=13, minutes=0):
                print(f"У {self.__name} сейчас обед!")
            else:
                print(f"{self.__name} работает!")
        else:
            print(f"{self.__name} отдыхает")


class Car:
    __mark: str  # Марка
    __engine_volume: float  # Объем двигателя
    __body_type: str  # Тип кузова
    __type_fuel: str  # Тип топлива
    __racing: float  # Разгон до 100 км/ч

    def __init__(self, mark, engine_volume, body_type, type_fuel, racing):
        self.__mark = mark
        self.__engine_volume = engine_volume
        self.__body_type = body_type
        self.__type_fuel = type_fuel
        self.__racing = racing

    @property
    def mark(self):
        return self.__mark

    @mark.setter
    def mark(self, mark):
        if mark.isalpha():
            self.__mark = mark
        else:
            print("Некоректно введена марка машнины!")

    @property
    def engine_volume(self):
        return self.__engine_volume

    @engine_volume.setter
    def engine_volume(self, eng):
        if 0.5 > eng > 12:
            self.__engine_volume = eng
        else:
            print("Введён объём двигателя который невозможен!")

    @property
    def body_type(self):
        return self.__body_type

    @body_type.setter
    def body_type(self, body):
        body_type_dict = ["купе", "седан", "хетчбэк",
                          "универсал", "минивен", "микроавтобус", "внедлрожник", "пикап", "кабриолет"]
        if body.lower() in body_type_dict:
            self.__body_type = body.lower()
        else:
            print("Такого кузова не суещтвует")

    @property
    def type_fuel(self):
        return self.__type_fuel

    @type_fuel.setter
    def type_fuel(self, fuel):
        fuel_list = ["бензин", "дизель", "электро", "гибрид"]
        if fuel.lower() in fuel_list:
            self.__type_fuel = fuel
        else:
            print("Некоректно введён тип топлива")

    @property
    def racing(self):
        return self.__racing

    @racing.setter
    def racing(self, racing):
        if 2 < racing < 25:
            self.__racing = racing
        else:
            print(f"Не верно указан разгон {self.__mark} до 100 км/ч")

    def Move(self, s: int):  # Автомобиль едет
        print(f"Автомобиль проехаал {s} киллометров")

    def Turn(self, t):  # Автомобль поворачивает
        if t.lower() == "right":
            print("Автомобиль повернул на право")
        elif t.lower() == "left":
            print("Автомобиль повернул на лево")
        else:
            print("Некоректно указано напрвлене поворота")


class EmployeBank:
    __first_name: str  # Имя владельца счета
    __last_name: str  # Фамилия владельца счета
    __position: str  # Должность
    __salary: int  # Зарплата

    def __init__(self, first_name, last_name, position, salary):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__position = position
        self.__salary = salary

    @property
    def first_name(self):
        return self.__first_name

    @first_name.setter
    def first_name(self, first_name):
        if first_name.isalpha():
            self.__first_name = first_name
        else:
            print("Некоректное имя!")

    @property
    def last_name(self):
        return self.__last_name

    @last_name.setter
    def last_name(self, last_name):
        if last_name.isalpha():
            self.__last_name = last_name
        else:
            print("Некоректная фамилия!")

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, position):
        if position.isalpha():
            self.__first_name = position
        else:
            print("Некоректное введена должность!")

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, salary):
        if salary > 0:
            self.__salary = salary
        else:
            print("Зарплата не может быть отрицательной)")

    def Work(self, times: datetime.timedelta):
        if datetime.timedelta(hours=8, minutes=0) < times < datetime.timedelta(hours=17, minutes=0):
            if datetime.timedelta(hours=12, minutes=0) < times < datetime.timedelta(hours=13, minutes=0):
                print(f"У {self.__first_name} {self.__last_name} сейчас обед!")
            else:
                print(f"{self.__first_name} {self.__last_name} работает!")
        else:
            print(f"{self.__first_name} {self.__last_name} отдыхает")

    def GetSalary(self, date: datetime.timedelta):
        if date == datetime.timedelta(days=20):
            print(f"{self.__first_name} {self.__last_name} получил зарплату {self.__salary}")
        else:
            print("Зарплата не скоро(")


class ClientBank:
    __first_name: str  # Имя владельца счета
    __last_name: str  # Фамилия владельца счета
    __id: int = 0  # Индефикатор счёта
    __account_sum: int  # Сумма на счёте

    def __init__(self, first_name, last_name, account_sum):
        self.__first_name = first_name
        self.__last_name = last_name
        ClientBank.__id += 1
        self.__id = ClientBank.__id
        self.__account_sum = account_sum

    @property
    def first_name(self):
        return self.__first_name

    @first_name.setter
    def first_name(self, first_name):
        if first_name.isalpha():
            self.__first_name = first_name
        else:
            print("Некоректное имя!")

    @property
    def last_name(self):
        return self.__last_name

    @last_name.setter
    def last_name(self, last_name):
        if last_name.isalpha():
            self.__last_name = last_name
        else:
            print("Некоректная фамилия!")

    @property
    def id(self):
        return self.__id

    @property
    def account_sum(self):
        return self.__account_sum

    @account_sum.setter
    def account_sum(self, sum):
        if sum > 0:
            self.__account_sum = sum
        else:
            print("Сумма на счёте не может быть отрицательной!")

    def Put(self, put_sum):  # Положить сумму на счёт
        self.__account_sum += put_sum
        print(f"На счёт {self.__id} положли {put_sum}")
        print(f"Сумма на счёте {self.__id} : {self.__account_sum}")

    def Withdrow(self, withdrow_sum):  # Снять сумму со счёта
        if self.__account_sum > withdrow_sum:
            self.__account_sum -= withdrow_sum
            print(f"Со счёта {self.__id} снято {withdrow_sum}")
            print(f"Сумма на счёте {self.__id} : {self.__account_sum}")
        else:
            print(f"Попытка снять {withdrow_sum} со счёта {self.__id} на котором {self.__account_sum}")
            print("Недостаточно средств")


# Тестируем класс Dog
print("Тестируем класс Dog!!!!!")
dog = Dog(5, 20, "Broono")
print(f"Имя собаки {dog.name}, вес собаки {dog.weight}, рост собаки {dog.height}")
print("." * 50)
dog.name = "Gr1f"
dog.weight = "23"
dog.height = "15"
print(f"Имя собаки {dog.name}, вес собаки {dog.weight}, рост собаки {dog.height}")
dog.Jump()
dog.Run()
print("=" * 50)

# Тестируем класс People
print("Тестируем класс People!!!!!")
p = People("Yura", 29, "Man")
print(f"Имя человека {p.name}, возраст  {p.age}, пол {p.gender}")
print("." * 50)
p.name = "Va2ya"
p.age = -21
p.gender = "2e311"
print(f"Имя человека {p.name}, возраст  {p.age}, пол {p.gender}")
p.Sleep(datetime.timedelta(hours=2, minutes=25))
p.Work(datetime.timedelta(hours=18, minutes=25))
p.Work(datetime.timedelta(hours=11, minutes=35))
p.Work(datetime.timedelta(hours=12, minutes=11))
print("=" * 50)

# Тестируем класс Car
print("Тестируем класс Car!!!!!")
c = Car("BMW", 3.0, "Cедан", "Бензин", 5.0)
print(f"Марка машны {c.mark}, объём двигателя  {c.engine_volume},"
      f" тип кузова {c.body_type}, тип топлива {c.type_fuel}, разгон до 100 км/ч - {c.racing} ")
print("." * 50)
c.mark = "w12"
c.engine_volume = 100
c.body_type = "11"
c.body_type = "куПе"
c.type_fuel = "Водород"
c.racing = 500
print(f"Марка машны {c.mark}, объём двигателя  {c.engine_volume},"
      f" тип кузова {c.body_type}, тип топлива {c.type_fuel}, разгон до 100 км/ч - {c.racing} ")
c.Move(10)
c.Turn("Right")
print("=" * 50)

# Тестируем класс ClientBank
print("Тестируем класс ClientBank!!!!!")
client = ClientBank("Иван", "Иванов", 500)
client2 = ClientBank("Андрей", "Петров", 200)
print(f"Имя клиента {client.first_name}, фамилия {client.last_name}, "
      f"сумма на счёте {client.account_sum}, id счёта: {client.id}")
print(f"Имя клиента {client2.first_name}, фамилия {client2.last_name}, "
      f"сумма на счёте {client2.account_sum}, id счёта: {client2.id}")
print("." * 50)
client.first_name = "T1m"
client.last_name = "Wil2on"
client.account_sum = -100
print(f"Имя клиента {client.first_name}, фамилия {client.last_name}, "
      f"сумма на счёте {client.account_sum}, id счёта: {client.id}")
print(f"Имя клиента {client2.first_name}, фамилия {client2.last_name}, "
      f"сумма на счёте {client2.account_sum}, id счёта: {client2.id}")

client.Put(200)
client2.Put(125)
client.Withdrow(250)
client2.Withdrow(700)
print("=" * 50)

# Тестируем класс EmployeBank
print("Тестируем класс EmployeBank!!!!!")
emp = EmployeBank("Bill", "Tompson", "Manager", 1000)
print(f"Имя cотрудника: {emp.first_name}, фамилия: {emp.last_name}, должность  {emp.position}, зарплата {emp.salary}")
print("." * 50)
emp.first_name = "123"
emp.last_name = "ttfl1"
emp.position = "dsp12"
emp.salary = -25
print(f"Имя cотрудника: {emp.first_name}, фамилия: {emp.last_name}, должность  {emp.position}, зарплата {emp.salary}")
emp.Work(datetime.timedelta(hours=16, minutes=23))
emp.GetSalary(datetime.timedelta(days=20))
emp.GetSalary(datetime.timedelta(days=25))
