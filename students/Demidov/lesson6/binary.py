

quit()

#    16  -->  1 + 6 = 7
#    942  -->  9 + 4 + 2 = 15  -->  1 + 5 = 6
#    132189  -->  1 + 3 + 2 + 1 + 8 + 9 = 24  -->  2 + 4 = 6
#    493193  -->  4 + 9 + 3 + 1 + 9 + 3 = 29  -->  2 + 9 = 11  -->  1 + 1 = 2

def digital_root(n):
    while n >= 10:
        n = sum(int(i) for i in str(n))
    return n

print(digital_root(13))

quit()

my_list = [1, 3, 5, 7, 9]

def binary_search(my_list, item):
    low = 0
    high = len(my_list) - 1
    while low <= high:
        mid = low + high
        guess = my_list[mid]
        if guess == item:
            return mid
        elif guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None

r = binary_search(my_list, 5)

print(r)