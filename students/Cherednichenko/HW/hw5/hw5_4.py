n = int(input('введите число: '))
a= 0
b= 0
for i in range (n):
	b+=1/(a+1)
	a+=1
print(b)