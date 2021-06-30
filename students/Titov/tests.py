class Dog:
    def __init__(self, height, weight, name, age, master):
        self.__name = name
        self._age = age
        self.height = height
        self.weight = weight
        self.__master = master
    def change_name(self, name):
        self.name = name
    def get_master(self):
        return self.__master
    def set_master(self, master):
        self.__master = master
dog_1 = Dog(100, 180, 'Bob', 12, 'of_carate')
print(dog_1.height)
print(dog_1.change_name('kraken'), dog_1._age)
print(dog_1.get_master())
dog_1.set_master('karakuli')
print(dog_1.get_master())