# Для каждого натурального числа в промежутке от m до n вывести все делители,
# кроме единицы и самого числа. m и n вводятся с клавиатуры. Пример:m =100, n = 105
# 100: 2 4 5 10 20 25 50
# 101:
# 102: 2 3 6 17 34 51
# 103:
# 104: 2 4 8 13 26 52
# 105: 3 5 7 15 21 35

while True:
    dict = {}
    x = input('Please, enter the number_1: ')
    y = input('Please, enter the number_2: ')
    if x < y:
        x = int(x)
        y = int(y)
        for i in range(x,y+1):
            dict[i] = []
            for j in range(2, i//2 + 1):
                if i%j==0:
                    dict[i].append(j)
        print(dict)
    else:
        print('Your number_1 is more number_2. Number_2 must be more number_1')