list = [73, 85, 78, 21, 25, 89, 7, 65, 3, 65, 40]
a=0
reverse = []
for i in range (len(list)-1):
	if list[i]<list[i+1]:
		reverse.append(list[i])
	else:
		if len(reverse)>0:
			a+=1
		reverse =[]
if len(reverse)>0:
	a+=1
print(a)