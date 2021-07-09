class Timer:
    import time
    def __init__(self, time: str):
        self.h, self.m, self.s = time.split(';')
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
            print(f'{i // 3600}:{(i % 3600) // 60}:{(i % 3600) % 60}')
            self.time.sleep()

t1 = Timer({'01:12:34'})
t1.start()

quit()

def gf1(arg):
    for i in arg:
        yield i


l1 = [1, 2, 3, 4, 5, 6, 76,]

gen1 = gf1(l1)

for i in gf1(l1):
    print(i)




quit()

def foo1(arg):
    for i in arg:
        return i

def foo2(arg):
    for i in arg:
        yield i


l1 = [1, 2, 3, 4, 5]
print(foo1(l1))

gen1 = foo2(l1)

print(next(gen1))
print(next(gen1))
print(next(gen1))
print(next(gen1))
print(next(gen1))
print(next(gen1))

quit()


def timer(max):
    for s in range(max, 0, -1):
        print(s)


timer(10)