'''cоздать универсальный декоратор, который меняет порядок аргументов в
функции на противоположный.'''

def outer(arg):
    def inner(**kwargs):
        spis = []
        for i, j in kwargs.items():
            spis.append(j)
        for i, j in enumerate(kwargs):
            kwargs[j] = spis[-1]
            spis.pop()
        arg(kwargs)
    return inner

@outer
def foo(m):
    for i, j in m.items():
        print(i, '=', j)

a, b, c = 1, 3, 8
foo(a = 1, b = 3, c = 8)