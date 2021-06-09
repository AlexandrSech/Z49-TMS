a = {'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}
c = 0

while c <= len(a.keys()):
    a[a + str(len(a.keys()))] = a.pop.keys()
    c += 1
print(a)

exit()
b = list(a.keys())
for key in b:
    a[key + str(len(key))] = a.pop(key)
print(a)