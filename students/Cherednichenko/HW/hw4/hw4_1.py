'''
list = [76, 54, -69, 36, 9]
new_list=[]

for i in list:
	new_list.append(i*-2)

print(new_list)
'''

list = [76, 54, -69, 36, 9]
new_list=[]
a=0
i=0
while i < len(list):
	new_list.append(list[a]*-2)
	i+=1
	a+=1
print(new_list)