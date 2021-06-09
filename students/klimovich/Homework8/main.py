import math

#1

def fact2(n):
    result = 1
    result2 = 1
    if n % 2 == 0:
        for i in range(n+1):
            if i % 2 == 0 and i != 0:
                result *= i
        return result
    if n % 2 == 1:
        for i in range(n+1):
            if i % 2 == 1 and i != 0:
                result2 *= i
        return result2


print(fact2(9))
print(fact2(10))

#2


def palindrom(s: str) -> bool:
    rs = s[::-1]
    if rs == s:
        return True
    else:
        return False


print(palindrom('papap'))


#3


def sinus(x):
    return math.sin(x)


print(sinus(10))