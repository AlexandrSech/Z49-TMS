# matrix

my_list = []
for i in range(4):
    my_list.append([])
    
    for q in range(4):
        my_list[i].append(0)

for i in my_list:
    print(i)

for i, ii in enumerate(my_list):
    print(i, ii)

# enumerate

ll = [1, 2, 3, 4, 5]
for index, value in enumerate(ll):
    ll[index] += 0
    # print(index, value)

print(ll)