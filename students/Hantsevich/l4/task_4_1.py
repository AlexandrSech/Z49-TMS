'''
my_list = [12,43,6534,6423,6]
my_new_list = []

for i in my_list:
    my_new_list.append(i * -2)

print(my_new_list)
'''

my_list = [12,43,6534,6423,6]
my_new_list = []
a = 0
i = 0
while i < len(my_list):
    my_new_list.append(my_list[a] * -2)
    i += 1
    a += 1

print(my_new_list)
