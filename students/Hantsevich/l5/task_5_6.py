my_list = [45,7546,45,468,7,45,6478,654,136,45]
a = 0
reserve = []
for i in range(len(my_list)-1):
     if my_list[i] < my_list[i+1]:
        reserve.append(my_list[i])
     else:
        if len(reserve) > 0:
            a+=1
        reserve = []
if len(reserve) > 0:
    a+=1

print(a)
