"""
Дан словарь:
{'test': 'test_value', 'europe': 'eur',
'dollar': 'usd', 'ruble': 'rub'}
Добавить каждому ключу число равное длине
этого ключа (пример {‘key’: ‘value’} ->
{‘key3’:‘value’}). Чтобы получить список ключей -
использовать метод .keys()
"""
my_dict = {'test': 'test_value', 'europe': 'eur',
'dollar': 'usd', 'ruble': 'rub'}

# Способ 1
my_dict2 = dict()

for key, velue in my_dict.items():
    key = key + str(len(key))
    my_dict2[key] = velue

print(my_dict2)

# Способ 2????
my_dict3 = {'test': 'test_value', 'europe': 'eur',
'dollar': 'usd', 'ruble': 'rub'}
my_dict4 = dict()
i = 0
while i < len(my_dict3):
    my_dict3[i] = my_dict3[i] + str(len(my_dict3[i]))
    print(my_dict3[i])
print(my_dict3)

