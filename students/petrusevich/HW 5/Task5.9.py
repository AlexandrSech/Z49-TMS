m, n = int(input('Введите начало промежутка: ')), int(input('Введите конец промежутка: '))
for i in range(m, (n+1) ):
    print(f'{i}: ')
    for j in range(2, i):
        if i % j == 0:
            print(j)
