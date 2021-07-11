import asyncio
from time import sleep, time


async def print_nums():
    num = 1
    while True:
        print(num)
        num += 1
        await asyncio.sleep(0.1)


async def print_time():
    count = 0
    while True:
        if count % 3 == 0:
            print('count =', count)
        count += 1
        await asyncio.sleep(1)


async def event_manager():
    task1 = asyncio.create_task(print_nums())
    task2 = asyncio.create_task(print_time())

    await asyncio.gather(task1, task2)





    '''g1 = print_nums()
    g2 = print_time()
    event_list = [g1, g2]

    while True:
        g = event_list.pop(0)
        next(g)
        event_list.append(g)'''


if __name__ == '__main__':
    asyncio.run(event_manager())







