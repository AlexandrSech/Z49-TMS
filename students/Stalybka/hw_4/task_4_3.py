''' Дан словарь: {'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}
Добавить каждому ключу число равное длине этого ключа (пример {‘key’: ‘value’} -> {‘key3’:
‘value’}). Чтобы получить список ключей - использовать метод .keys() '''

my_dict = {
    'test': 'test_value',
    'europe': 'eur',
    'dollar': 'usd',
    'ruble': 'rub'
}
values =list(my_dict.values())
keys_list = list(my_dict.keys())
new_dict = {}
end = len(keys_list)

for i in range(0,end):
    keys_list[i] += str(len(keys_list[i]))
    new_dict[keys_list[i]] = values[i]
print(new_dict)




