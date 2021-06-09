list = [73, 85, 78, 21, 25, 89, 7, 61, 80, 5, 3, 65, 40, 21, 35, 18, 39]
result = 0

for i in range(len(list)):
	if result < list[i]:
		result = list[i]
print (result)

for i in range(len(list)):
	if list[i]%2 ==0:
		list[i] = result
print('\n')
print(list)
