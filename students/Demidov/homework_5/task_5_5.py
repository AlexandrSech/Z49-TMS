a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

a = list(map(lambda x:max(a) if x % 2 == 0 else x,a))

print(*a)