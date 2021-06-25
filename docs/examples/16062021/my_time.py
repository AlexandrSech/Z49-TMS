


class MyTime:
    h: int
    m: int
    s: int
    t_string: str

    def __init__(self, time_string='', hour=0, minute=0, second=0, my_time_object=None):
        if time_string:
            self.t_string = time_string
        elif hour or minute or second:
            self.h = hour
            self.m = minute
            self.s = second
        elif my_time_object:
            self = my_time_object
        print(self.__dict__)



m1 = MyTime(time_string='01:00:00', hour=2)
print()
m2 = MyTime(hour=2, my_time_object=m1)
print()
m3 = MyTime(my_time_object=m1)

m4 = MyTime()




# t1 = MyTime('01:00:00')
# print(t1.__dict__)





