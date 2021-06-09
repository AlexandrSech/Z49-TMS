from bubble import bubble_sort

lis = [1, 21, 5, -10]

bubble_sort(lis)
print(lis)

quit()

def line_sum(row_number):
    col = sum([i for i in range(1, row_number + 1)])
    c = 1
    my_list = [c for i in range(1, col + 2) if i % 2 != 0]
    print(my_list)

line_sum(5)

quit()

def foo():
    l = [item for item in range(100) if item % 2 == 1] # list generator
    return l


def foo2(l1 = foo()):
    return {i: i**3 for i in l1}


print(foo2('\n'.join('{}: {}'.format(k, v) for k, v in foo2().items())))

exit()

def get_friendly_numbers():
    for n in range(200, 301):
        temp_list = []
        for delitel in range(1, n):
            if n % delitel == 0:
                temp_list.append(delitel)
        print(n, temp_list)

get_friendly_numbers()