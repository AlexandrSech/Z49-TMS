class Person:

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

a = Person("Sam", 20)
print(a.name, a.age)