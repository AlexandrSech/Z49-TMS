class MyTime:
    n: int
    m: int
    s: int
    t_string: str

    '''
    def __init__(self, time_string= '', hour = 0, minute = 0, second = 0, my_time_object = None):
        if time_string:
    '''

    def __init__(self, t_str):
        self.t_string = t_str

    def __init__(self, h, m, s):
        self.h - h
        self.m = m
        self.s = s

t1 = MyTime('01:00:00')
print(t1.__dict__)