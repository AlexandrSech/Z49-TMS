'''
list = [76, 54, -69, 36, 9]
a=0
for i in list:
	if i%2==0:
	    a+=1
print(a)
'''

list = [76, 54, -69, 36, 9]
a=0
b=0
i=0
while i<len(list):
	if list[b]%2==0:
		a+=1
		b+=1
		i+=1
	else:
		i+=1
		b+=1
print(a)