import math

lis = [2, 8]

summ = sum(lis)


def product(numbers):
    res = 1
    for i in numbers:
        res *= i
    return res

res = product([4, 1, 4])

print(summ / len(lis))
print(math.sqrt(res))