# Дан словарь: {'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}
# Добавить каждому ключу число равное длине этого ключа (пример {‘key’: ‘value’} -> {‘key3’:‘value’}).
# Чтобы получить список ключей - использовать метод .keys()
# Примечание: Во всех задачах предоставить 2 решения. Одно с использованием цикла
# while, другое с использованием цикла for с параметром. Оба решения предоставить в одном файле.

test_dictionary = {
    'test': 'test_value',
    'europe': 'eur',
    'dollar': 'usd',
    'ruble': 'rub',
}
list_of_keys = []
list_of_values = []
new_dict = {}
for k, i in test_dictionary.items():
    list_of_keys.append(k)
    list_of_values.append(i)
for i in range(len(list_of_keys)):
    list_of_keys[i] = list_of_keys[i] + str(len(list_of_keys[i]))

for i in range(len(list_of_keys)):
    new_dict[list_of_keys[i]] = list_of_values[i]
print(new_dict)