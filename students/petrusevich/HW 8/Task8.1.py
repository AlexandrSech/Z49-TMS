def fact2():
    while True:
        n = int(input('Введите n или отрицательное число, чтобы прекратить работу: '))
        fact = 1
        if n > 0:
            if n % 2 == 0:
                for i in range(2, n+1, 2):
                    fact *= i
            else:
                for i in range(1, n+1, 2):
                    fact *= i
            print(f'{n}!! =', fact)
        elif n == 0:
            fact = 1
            print(f'{n}!! =', fact)
        else:
            print('Ввели не положительное число!')
            break

r = fact2()
print(r)