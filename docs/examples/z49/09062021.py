





def reverse_args(func):
    def inner(*args):
        return func(*args[::-1])
    return inner

@reverse_args
def foo(*a):
    my_list = []
    for i in range(len(a)):
        my_list.append(a[i])
    return my_list

@reverse_args
def foo2(*a):
    return a[0] + a[1] * a[2]

print(foo2(1, 2, 3))


