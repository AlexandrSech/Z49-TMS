def decorator(func):
    def inner(*args):
        try:
            return func(*args)
        except ZeroDivisionError as zero:
            print("Divided by zero")
        except Exception as my_ex:
            print("Error: {}".format(my_ex))
    return inner

def logger(func):
    def inner(*args):
        with open('log.txt', 'w') as some_file:
            some_file.write('log')
    return inner

class Pi:
    k: int
    n: int

    def __init__(self, k, n):
        self.k = k
        self.n = n

    def root(self):
        x = 2 * (2 ** (0.5))
        return x

    def e(self, k):
        res = sum(x for x in range(0, k))
        return res

    def factorial(self, n):
        factorial = 1
        for i in range(2, n + 1):
            factorial *= i
        return factorial

    
    def log(func):
        def wrapper(self, root, e, factorial):
            pass

    @decorator
    def answer(self, root, e, factorial):
        multiple = root * e
        power = factorial**4
        summ = 1103 + 26390
        multiple2 = (4 * 99)**4
        return 9801 / (multiple * (factorial / power) * summ / multiple2)


x = Pi(5, 5)

a = x.factorial(10)
b = x.root()
c = x.e(5)

print(x.answer(b, c, a))