#Составить список чисел Фибоначчи содержащий 15 элементов.
# (Подсказка: Числа Фибоначчи - последовательность, в которой первые два числа равны
# либо 1 и 1, а каждое последующее число равно сумме двух предыдущих чисел.
# Пример: 1, 1, 2, 3, 5, 8, 13, 21, 34... )

my_list = [1,1]

for i in range(13):
    my_list.append(my_list[len(my_list) - 1] + my_list[len(my_list) - 2])
print(my_list)