fib_list = [0, 1,]

# for _ in range(100):
while len(fib_list) < 10:
    fib_list.append(fib_list[-1] + fib_list[-2])

print(fib_list)