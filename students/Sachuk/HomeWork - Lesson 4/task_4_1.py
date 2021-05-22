# Дан список целых чисел.
# Создать новый список, каждый элемент которого равен исходному элементу
# умноженному на -2
# Примечание: Во всех задачах предоставить 2 решения. Одно с использованием цикла
# while, другое с использованием цикла for с параметром. Оба решения предоставить в
# одном файле.

my_list_of_numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

my_list_of_numbers_2 = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

# cicle for each

for i in range(len(my_list_of_numbers)):
    my_list_of_numbers[i] *= -2

print(my_list_of_numbers)

# circle while

count = 0

while count < len(my_list_of_numbers_2):
    my_list_of_numbers_2[count] *= -2
    count += 1

print(my_list_of_numbers_2)
