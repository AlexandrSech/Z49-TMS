'''Для заданного числа N составьте программу вычисления суммы
S=1+1/2+1/3+1/4+...+1/N, где N – натуральное число.'''

n = 18
count = 1
result = 0
while count <= n:
    result += 1/count
    count += 1
print(result)