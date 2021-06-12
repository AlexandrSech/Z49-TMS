
def dec(func):
    d = {}
    temp = []
    z = 0
    def inner(x, y):
        if (x, y) not in d:
            d[(x, y,)] = func(x, y)
            temp.append(x)
            temp.append(y)
            z += 1




@dec
def foo(x, y):
    return x + y


exit()

d = {i: i**5 for i in range(10)}
print(d)

print(d.popitem())
print(d)

print(d.pop(list(d.keys())[-1]))
print(d.keys(), type(d.keys()))
print(d)



exit()

def dec3(*dec3_args):
    def l1(func):
        def inner(*a, **k):
            t = a + dec3_args
            return func(*t, **k)
        return inner
    return l1


def dec1(func):
    def inner(*a, **kwa):
        print('dec1 start')
        t = a + (2,)
        r = func(*t, **kwa)
        print('dec1 end')
        return r
    return inner



def dec2(func):
    def inner(*a, **kwa):
        print('dec2 start')
        t = a + (3,)
        r = func(*t, **kwa)
        print('dec2 end')
        return r
    return inner


@dec3('one', 'two', 'bark')
def foo(*args):
    print('this is simple func')
    print(args)
    return False


foo(1)


