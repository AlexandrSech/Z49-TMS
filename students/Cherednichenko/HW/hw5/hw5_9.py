a=int(input('введите а: '))
b=int(input('введите b: '))

for i in range (a, b+1):
	print(i, ': ', end=' ')
	for j in range(1, i):
		if j!=1 and j!=i and i%j==0:
			print(j, end=' ')
	print(end='\n')