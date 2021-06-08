def reverse_args(func):
    def inner(*args):
        return func(*args)[::-1]
    return inner

@reverse_args
def foo(*a):
    my_list = []
    for i in range(len(a)):
        my_list.append(a[i])
    return my_list

print(foo(1, 21, 21, 22, 1, 31, 31, 31))