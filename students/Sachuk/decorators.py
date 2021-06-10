# Декораторы
from datetime import datetime
from functools import wraps

exit()
def decorator(another_decorator):

    def param_deco(func):
        @wraps(func)
        def res_deco(*args, **kwargs):
            return another_decorator(func, *args, **kwargs)

        return res_deco

    return param_deco


@decorator
def introduce(f, *args, **kwargs):
    print(f.__name__)
    return f(*args, **kwargs)


@introduce
def identity(x):
    return x


print(identity(31415))

exit()
def parametrized(init_deco):
    start = datetime.now()
    print(start)
    def param_deco(func):
        def res_deco(*args, **kwargs):
            return init_deco(func, *args, **kwargs)
        return res_deco
    finish = datetime.now()
    print(finish)
    print(finish - start)
    return param_deco


def memoized(maxsize=None):
    def make_decorator(func):
        d = {}
        @wraps(func)
        def wrapper(*args, **kwargs):
            key = (args, tuple(sorted(kwargs.items())))
            if key not in d:
                if len(d) < maxsize:
                    d[key] = func(*args, **kwargs)
                else:
                    d.popitem()
                    d[key] = func(*args, **kwargs)
            return d[key]
        return wrapper

    return make_decorator

@memoized(maxsize=2)
def sum_of_two(a, b):
    print(a, b, end='; ')
    return a + b


print(sum_of_two(2, 0), '\n')
print(sum_of_two(2, 0), '\n')

print(sum_of_two(4, 2), '\n')
print(sum_of_two(4, 2), '\n')

print(sum_of_two(5, 0), '\n')
print(sum_of_two(5, 0), '\n')

print(sum_of_two(4, 2))

exit()


def bucket(*arg, **kw):
    def make_decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print((arg, kw))
            return func(*args, **kwargs)

        return wrapper

    return make_decorator


@bucket(1, 2, 3, [1, 2, 3], 'one', 'two', 'three', one=1, two=2, three=3)
def identity(x):
    return x


print(identity(42))


@bucket()
def identity(x):
    return x


print(identity(42))

exit()


def optional_introduce(func):
    def wrapper(*args, introduce=False, **kwargs):
        if introduce:
            print(func.__name__)
        return func(*args, **kwargs)

    return wrapper


@optional_introduce
def identity(x):
    return x


print(identity(20))

print(identity(42, introduce=True))

exit()


def flip(func):
    def wrapper(*args, **kwargs):
        revers = reversed(args)
        return func(*revers, **kwargs)

    return wrapper


@flip
def div(x, y, show=False):
    res = x / y
    if show:
        print(res)
    return res


div(2, 4, show=True)

exit()
number_names = {
    0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine',
    10: 'ten', 11: 'eleven', 12: 'twelve',
    13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen'}

line = input().split()
result = sorted(line, key=lambda x: number_names[int(x)])
print(*result)

line = input().split()
for i in line:
    print(float(i))


def print_given(*args, **kwargs):
    for i in args:
        print(i, type(i))
    for i in kwargs:
        print(i, kwargs[i], type(kwargs[i]))


print_given(1, 2, 3, [1, 2, 3], 'one', 'two', 'three', two=2, one=1, three=3)

from datetime import datetime


def timeit(func):
    def wrapper(*args, **kwargs):
        start = datetime.now()
        result = func(*args, **kwargs)
        print(datetime.now() - start)
        return result

    return wrapper


# @timeit
def one(n):
    l = []
    for i in range(10 ** 4):
        if i % 2 == 0:
            l.append(i)

    return l


# @timeit
def two(n):
    l = [x for x in range(10 ** 4) if x % 2 == 0]
    return l


l1 = timeit(one)
