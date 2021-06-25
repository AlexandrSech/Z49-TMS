class Timer:
    import time

    def __init__(self, time: str):
        self.h, self.m, self.s = time.split(':')
        self.h = int(self.h)
        self.m = int(self.m)
        self.s = int(self.s)

    def t_gen(self, time_in_sec):
        for s in range(time_in_sec, -1, -1):
            yield s

    def start(self):
        for i in self.t_gen(
            self.h * 60 * 60 +
            self.m * 60 +
            self.s
        ):
            print('{:02}:{:02}:{:02}'.format(
                i // 3600,
                (i % 3600) // 60,
                (i % 3600) % 60
            ))
            self.time.sleep(1)


t1 = Timer('01:23:45')
t1.start()


exit()




def gf1(arg):
    for i in arg:
        yield i


l1 = [1,2,3,4,5,6,76,]

gen1 = gf1(l1)

for i in gen1:
    print(i)



exit()





def timer(max):
    for s in range(max, 0, -1):
        print(s)


# timer(10)
