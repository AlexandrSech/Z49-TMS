'''Для заданного числа N составьте программу вычисления суммы
S=1+1/2+1/3+1/4+...+1/N, где N – натуральное число.'''
a = int(input("Введите число"))
n = 0
for el in range(1, a + 1):
    n += 1/el
print(n)