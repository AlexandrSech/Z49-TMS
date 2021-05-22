# Составить список чисел Фибоначчи содержащий 15 элементов
fib = [1, 1]
while len(fib) < 15:
    fib.append(fib[-2] + fib [-1])
print(fib)


fib1 = [1, 1]
for i in range (13):
    fib1.append(fib1[len(fib1) - 1] + fib1[len(fib1) - 2])
print(fib1)
# решение через for я сам не смог сделать, подсмотрел


