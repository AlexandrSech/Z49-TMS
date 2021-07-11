

def bc():
    summ = 0

    while True:
        data = yield summ
        summ += data
        print(summ, data)


g = bc()
print(next(g))
i = 10
for _ in range(5):
    i = g.send(i)
