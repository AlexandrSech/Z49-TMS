a = lambda x: x**3

print(a(2))
print(a(3))


exit()

text = '''
123
asas
csd
sd
sd
dddd
'''
try:
    t1 = open('example.txt', 'r')
    try:
        print(t1.read())
        print(1/0)
    except:
        pass
    print(1/0)
except:
    pass
finally:
    print('close')
    t1.close()


with open('example.txt', 'r'):
    pass

exit()


import time


def my_decorator(f):
    start_time = time.time()

    def inner():
        return f()
    end_time = time.time()
    print(end_time - start_time)

    return inner


@my_decorator
def foo():
    r = 1
    for i in range(5):
        r += 1
        time.sleep(1)
    return r

@my_decorator
def foo2():
    return -1


print(foo())