h = []


class ExceptionDecorator(object):
    def __init__(self, callback=None):
        self.callback = callback

    def __call__(self, f):
        def wrapper(instance, *args, **kwargs):
            try:
                return f(instance, *args, **kwargs)
            except Exception as e:
                if self.callback:
                    self.callback(e)
                raise
        return wrapper


class Foo(object):
    @ExceptionDecorator(lambda e: h.append(e))
    def bar(self):
        raise ZeroDivisionError


foo = Foo()
try:
    foo.bar()
except:
    pass
finally:
    assert len(h)

print(h)