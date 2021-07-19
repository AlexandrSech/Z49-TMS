import time


some_list_for_test_decorator_work = []


def simple_deco(foo):
    def inner(*args, **kwargs):
        some_list_for_test_decorator_work.append(time.time())
        r = foo(*args, **kwargs)
        some_list_for_test_decorator_work.append(time.time())
        return r
    return inner


@simple_deco
def foo():
    print('some foo do things')


if __name__ == '__main__':
    foo()
