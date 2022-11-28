import asyncio
from asyncio.exceptions import TimeoutError
from util import delay


async def async_main():
    task = asyncio.create_task(delay(10))
    try:
        result = await asyncio.wait_for(asyncio.shield(task), 5)
        print(result)
    except TimeoutError:
        print("Task took longer than five seconds to complete. It will finish soon.")
        result = await task
        print(result)

asyncio.run(async_main())
