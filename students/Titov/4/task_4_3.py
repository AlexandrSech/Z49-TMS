a = {'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}
slov = {}
spis = []
i = 0
'''while i < len(a.keys()):
    spis = list(a)
    slov[str(spis[i]) + str(len(spis[i]))] = a[spis[i]]
    i += 1
print(slov)
exit()'''
for m, n in a.items():
    slov[m + str(len(m))] = n
print(slov)
