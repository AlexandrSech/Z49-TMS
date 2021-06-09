# Составить список чисел Фибоначчи содержащий 15 элементов.
# (Подсказка: Числа Фибоначчи - последовательность, в которой первые два числа равны
# либо 1 и 1, а каждое последующее число равно сумме двух предыдущих чисел.
# Пример: 1, 1, 2, 3, 5, 8, 13, 21, 34... )
# Примечание: Во всех задачах предоставить 2 решения. Одно с использованием цикла
# while, другое с использованием цикла for с параметром. Оба решения предоставить в
# одном файле.

list_of_fibonacci = [1,1]
# Cicle for each
for i in range(13):
    list_of_fibonacci.append(list_of_fibonacci[len(list_of_fibonacci) - 1] +
                             list_of_fibonacci[len(list_of_fibonacci) - 2])

print(list_of_fibonacci)

list_of_fib = [1, 1]
# Cicle while
count = 0
while count < 13:
    list_of_fib.append(list_of_fib[len(list_of_fib) - 1] + list_of_fib[len(list_of_fib) - 2])
    count += 1
print(list_of_fib)