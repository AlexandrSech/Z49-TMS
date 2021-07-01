class MyValueErrorException(ValueError):
    def __init__(self):
        print('Ты ввел неправильные данные, придурок!')

class MyTime:
    def __init__(self, time_string='', hour=0, minute=0, second=0, my_time_object=None):
        if time_string:
            # self.t_string = time_string
            if len(time_string.split(':')) == 3:  # проверка, правильно ли заполнена строка времени
                self.h, self.m, self.s = map(int, time_string.split(':'))
            else:
                raise MyValueErrorException
        elif hour or minute or second:
            self.h = hour
            self.m = minute
            self.s = second
        elif my_time_object:
            if isinstance(my_time_object, MyTime):  # проверка что my_time_object это обьект класса MyTime
                self.__dict__ = my_time_object.__dict__
        else:
            raise MyValueErrorException

    def __lt__(self, other):
        if isinstance(other, MyTime):
            if self.h < other.h or \
                    self.h <= other.h and self.m < other.m or \
                    self.h < other.h and self.m < other.m and self.s < other.s:
                return True
        return False


m1 = MyTime(time_string='01:00:00', hour=2)
print('m1', m1.__dict__)
m2 = MyTime(hour=2, my_time_object=m1)
print('m2', m2.__dict__)
m3 = MyTime(my_time_object=m1)
print('m3', m3.__dict__)

print(m1 < m2)


# m4 = MyTime()

# print(m1 < m2)