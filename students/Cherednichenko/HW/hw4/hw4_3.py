'''
a={'test': 'test value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}
b={'test': 'test value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}
for i in b.keys():
	a[i+str(len(i))] = a.pop(i)
print(a)
'''

a={'test': 'test value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}
b={'test': 'test value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}
i=0
c=0
while i<len(b):
	for c in b.keys():
		a[c+str(len(c))]=a.pop(c)
		i+=1
print (a)