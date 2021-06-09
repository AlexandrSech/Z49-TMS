'''
Создать универсальный декоратор, который меняет порядок аргументов в
функции на противоположный.
'''

def reverse_args(sample_func):
    def wrapper(args):
        args = args[::-1]
        return sample_func(args)
    return wrapper

@reverse_args
def sample_func(*args):
    return args

print(sample_func([1,2,3,4,5,]))