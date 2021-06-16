a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

max_value = max(a)

for i in a:
  if i % 2 == 0:
    a[i] = max_value
print(a)