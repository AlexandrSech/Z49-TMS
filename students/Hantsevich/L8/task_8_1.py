def fact2(n: int):
    fact = 1
    if n % 2 == 0:
        for i in range(2,n+1, 2):
            fact *= i
        return fact
    else:
        for i in range(1, n+1, 2):
            fact *= i
        return fact
print(fact2(2),fact2(5), fact2(6), fact2(8),fact2(9))