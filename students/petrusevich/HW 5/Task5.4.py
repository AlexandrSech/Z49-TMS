while True:
    numbers = input('Ввведите натуральное число: ')
    if numbers.isdigit():
        S = 0
        n = int(numbers)
        for i in range(1, n+1):
            S += 1/i
        print(S)
    else:
        print('Введите НАТУРАЛЬНОЕ число!')