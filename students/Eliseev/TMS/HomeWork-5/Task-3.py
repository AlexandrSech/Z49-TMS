dict_all_number = {}
for number in range(200, 300):
    list_number = []
    #вычисляет делители числа
    for el in range(1, number + 1):
        if number % el == 0: list_number.append(el)
    #вычисляет сумму делителей без самого числа
    sum_number = sum(list_number, -number)
    dict_all_number[number] = sum_number
for k, v in dict_all_number.items():
    if v in range(200, 300): key_v = dict_all_number[v]
    for el in dict_all_number:
        if key_v == k:
            print(dict_all_number[k])
            break



