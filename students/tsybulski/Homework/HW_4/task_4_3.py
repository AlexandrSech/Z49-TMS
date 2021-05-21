# Дан словарь: {'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}
# Добавить каждому ключу число равное длине этого ключа
# (пример {‘key’: ‘value’} -> {‘key3’: ‘value’}).
# Чтобы получить список ключей - использовать метод .keys()
my_dict = {'test': 'test_value',
           'europe': 'eur',
           'dollar': 'usd',
           'ruble': 'rub'}
my_dict_2 = {'test'+ str(len('test')): 'test_value',
           'europe' + str(len('europe')): 'eur',
           'dollar' + str(len('dollar')): 'usd',
           'ruble' + str(len('ruble')): 'rub'}
print(my_dict_2)
print()