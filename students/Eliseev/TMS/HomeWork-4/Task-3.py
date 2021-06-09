dict_1 = {'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}
dict_2 = {}
for k, v in dict_1.items():
    len_k = len(k)
    k_new = k + str(len_k)
    dict_2[k_new] = v
print(dict_2)