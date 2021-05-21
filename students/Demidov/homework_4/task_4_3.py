my_dict = {
    'test': 'test_value', 
    'europe': 'eur', 
    'dollar': 'usd', 
    'ruble': 'rub',
}

for i in list(my_dict):
    width = str(len(i))
    my_dict[i + width] = my_dict.pop(i)
print(my_dict)