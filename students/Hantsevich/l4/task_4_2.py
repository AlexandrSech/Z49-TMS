
'''
my_list = [12,43,6534,6423,6,55,66,66,66]
a = 0
for i in my_list:
    if i % 2 == 0:
        #a += 1
print(a)
'''
my_list = [12,43,6534,6423,6,55,66,66,66]
a = 0
b = 0
i = 0
while i < len(my_list):
    if my_list[b] % 2 == 0:
        i += 1
        a += 1
        b += 1
    else:
        i += 1
        b += 1
print(a)