# Дан список целых чисел. Подсчитать сколько четных чисел в списке
# Примечание: Во всех задачах предоставить 2 решения. Одно с использованием цикла
# while, другое с использованием цикла for с параметром. Оба решения предоставить в
# одном файле.

my_list_of_numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Cicle for each
count_of_even = 0
for i in my_list_of_numbers:
    if i % 2 == 0:
        count_of_even += 1
print(count_of_even)

# Cicle for while
count_of_even_2 = 0
count = 0
while count < len(my_list_of_numbers):
    if my_list_of_numbers[count] % 2 == 0:
        count_of_even_2 += 1
        count += 1
    else:
        count += 1
print(count_of_even_2)
