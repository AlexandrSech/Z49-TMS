def my_iter(obj):
    for i in obj:
        yield i

l1 = [1, 2, 3, 4, 5, 6, 7,]

iterator_object = my_iter(l1)
print(type(iterator_object))