queue = []

for i in range(1000):
    queue.append(i)

while queue: # пока есть очередь
    print(queue.pop(0))