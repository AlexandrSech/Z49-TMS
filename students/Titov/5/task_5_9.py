'''Для каждого натурального числа в промежутке от m до n вывести все делители,
кроме единицы и самого числа. m и n вводятся с клавиатуры.'''
m = int(input('Введи'))
n = int(input("Введи"))

for el in range(m, n + 1):
    s = ''
    for al in range(2, el):
        if el % al == 0:
            s += ' ' + str(al)
    print(str(el) + ":" + s)
