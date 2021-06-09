mtr = [[7, 5, 8], [1, 5, 9], [7, 6, 3]]

for i in mtr:
	print(i)
print('/n')

for item, value in enumerate (mtr):
	max_value=0
	r=0
	for j in range(len(mtr[item])):
		if mtr[item][j]>max_value:
			max_value = mtr [item][j]
			r=j
	mtr[item][r] = mtr [item][item]
	mtr[item][item]=max_value
	
for i in mtr:
	print(i)