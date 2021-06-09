'''
a=1
b=1
print(a)
print(b)
i=0
while i<13:
	c=a+b
	a=b
	b=c
	i+=1
	print(b)
'''
a=1
b=1
print(a)
print(b)
for i in range (13):
	c=a+b
	a=b
	b=c
	print(b)