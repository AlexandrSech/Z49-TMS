a = 3
b = 1
a, b = b, a

print(a, b)

lst = [1,2,3,4,5]
lst[0], lst[len(lst) -1] = lst[len(lst) -1], lst[0]
print(lst)