m = int(input())
n = int(input())

dict_numbers_del = {}

for number in range(m, n + 1):
    list_numbers_del = []
    for el in range(1, number + 1):
        if el == 1 or el == number:
            continue
        elif number % el == 0:
           list_numbers_del.append(el)
    dict_numbers_del[number] = list_numbers_del


for k, v in dict_numbers_del.items():
    print(str(k) + ": ", str(v).replace("[", "").replace("]", ""))

