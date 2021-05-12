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