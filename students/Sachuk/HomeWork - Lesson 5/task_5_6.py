# Задан целочисленный массив. Определить количество участков массива,
# на котором элементы монотонно возрастают (каждое следующее число
# больше предыдущего). [02-4.1-ML27]
from random import randint

my_list = []
result = {}
temp = []
count = 1
for i in range(20):
    my_list.append(randint(1, 100))

print(my_list)

for i in range(len(my_list) - 1):
    if my_list[i] <= my_list[i + 1]:
        if my_list[i] not in temp:
            temp.append(my_list[i])
        if my_list[i+1] not in temp:
            temp.append(my_list[i+1])
    else:
        if len(temp) > 0:
            result[count] = temp
            temp = []
            count +=1
        else:
            continue
print(result)