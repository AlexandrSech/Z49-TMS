def create_phone_number(n):
    for i in n:
        if i == n[0]:
            n.insert(0, '(')
        elif i == n[3]:
            n.insert(4, ')')
        elif i == n[7]:
            n.insert(8, '-')
    new = ''.join(map(str, n))
    print(new)


create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])


quit()

def number(n):
    x = 10
    while n > 1:
        result = n % x
        


quit()

def num(n, start):
    if start > n:
        return 0
    print(start)
    return num(n, start + 1)

print(num(10, 0))

exit()

def fib(a, limit):
    if len(a) > limit:
        return a
    a.append(a[-1] + a[-2])
    return fib(a, limit)

print(fib([0, 1], 100))