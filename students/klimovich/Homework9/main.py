import csv

#1

'''def foo(l:list):
    return ['{}-{}'.format(i, v) for i, v in enumerate(l)]


l_of_str = ['aaa', 'bbb', 'ccc', 'ddd', ]

print(foo(l_of_str))'''

'''#2

def foo2(**kwargs):
    d = {}
    for k, v in kwargs.items():
        result = lambda x: x*2
        d[k] = result(v)
    print(d)

foo2(name='alex', age='10')


#3
def my_dec(foo):
    def wrapper(lst):
        for i, v in enumerate(lst):
            if v % 2 == 0:
                lst.pop(i)
        return foo(lst)
    return wrapper


@my_dec
def our_foo(lst: list):
    return lst


@my_dec
def our_foo2(*args):
    return list(*args)


l = [1, 2, 3, 4, ]
print(our_foo(l))'''

#4

def my_dec(foo):
    def wrapper(*args):
        l = args[::-1]
        return  foo(l)
    return wrapper


@my_dec
def foo(*args):
    return list(*args)

print(foo(1,2,3))