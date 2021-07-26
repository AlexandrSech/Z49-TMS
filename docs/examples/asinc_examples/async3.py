import asyncio
import time


async def foo():
    print(time.time())
    await asyncio.sleep(1.2)
    return 123


async def event_manager():
    task1 = asyncio.create_task(foo())

    await asyncio.gather(task1)


if __name__ == '__main__':
    print(asyncio.run(event_manager()))

