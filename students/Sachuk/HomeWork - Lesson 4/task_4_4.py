# Дан список. Создать новый список, сдвинутый на 1 элемент влево
# Пример: 1 2 3 4 5 -> 2 3 4 5 1
# Примечание: Во всех задачах предоставить 2 решения. Одно с использованием цикла
# while, другое с использованием цикла for с параметром. Оба решения предоставить в
# одном файле.


# Cicle for each
list_of_numbers = [1, 2, 3, 4, 5]
print(list_of_numbers)
for i in range(5):
    list_of_numbers.append(list_of_numbers[0])
    del list_of_numbers[0]
    print(list_of_numbers)

# Cicle while
count = 0
list_of_num = [6, 7, 8, 9, 10]
print(list_of_num)
while count < 5:
    list_of_num.append(list_of_num[0])
    del list_of_num[0]
    count += 1
    print(list_of_num)
