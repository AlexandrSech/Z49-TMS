# Для заданного числа N составьте программу вычисления суммы
# S=1+1/2+1/3+1/4+...+1/N, где N – натуральное число.

a = 5

for i in range(5):
  i = (i + 1) / a
  print(i)