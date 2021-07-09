import asyncio

my_list = [1, 2, 3, 4, 5, 6,]

async def counter():
    for i in my_list:
        if i % 2 == 0:
            print(f'{i} - even')
            await asyncio.sleep(1)
        else:
            print(f'{i} - odd')
            await asyncio.sleep(1)
    print('Has iterated all list values')

asyncio.run(counter())