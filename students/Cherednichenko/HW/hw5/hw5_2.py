n1=int(input('Введите число: '))
n2=n1
sum=0
pr=1
while n1 > 0:
	sum+=n1%10
	n1//=10
while n2 > 0:
	pr *=n2%10
	n2//=10
print ('сумма чисел - ', sum, 'произведение чисел - ', pr)
	