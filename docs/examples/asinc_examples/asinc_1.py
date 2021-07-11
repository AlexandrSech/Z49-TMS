def coroutine(foo):
    def inner(*args, **kwargs):
        g = foo(*args, **kwargs)
        print('0.', g.send(None))
        return g
    return inner


@coroutine
def gen1(_l: list):
    for i in _l:
        print('before')
        mess = yield i
        print('after')
        print(mess)


g = gen1([1,2,3,4,5,6,])


print(g.send(10))
print(g.send(10))
print(g.send(10))
print(g.send(10))
print(g.send(10))



exit()






print('_'*10)
print('next', next(g))
print(g.send(10))
print('_'*10)
print('next', next(g))
print('_'*10)
print('next', next(g))
print('_'*10)
print('next', next(g))
print('_'*10)
