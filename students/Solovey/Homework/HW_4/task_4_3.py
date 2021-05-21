'''
3) Дан словарь: {'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}
Добавить каждому ключу число равное длине этого ключа (пример {‘key’: ‘value’} -> {‘key3’: ‘value’}).
Чтобы получить список ключей - использовать метод .keys()
'''


# example_1

dict_1 = {'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}

i = 0
list_of_keys = list(dict_1.keys())
list_of_values = list(dict_1.values())
new_keys = []

while i < len(dict_1):
    new_keys.append(list_of_keys[i] + str(len(list_of_values[i])))
    new_dict = dict(zip(new_keys, list_of_values))
    if len(new_dict) == len(dict_1):
        print(new_dict)
    i += 1



# example_2

dict_1 = {'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}
new_keys = {'test': 'test' + str(len(dict_1.get('test'))),
            'europe': 'europe' + str(len(dict_1.get('europe'))),
            'dollar': 'dollar' + str(len(dict_1.get('dollar'))),
            'ruble': 'ruble' + str(len(dict_1.get('ruble')))
            }

for i in list(dict_1):
    if i in new_keys:
        dict_1[new_keys[i]] = dict_1.pop(i)
print(dict_1)


