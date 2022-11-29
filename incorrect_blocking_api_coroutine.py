import asyncio
import requests
from util import async_timed


# requests library is blocking.
# Since asyncio has only one thread, the request library blocks the event loop from doing anything concurrently.
@async_timed()
async def get_example_status() -> int:
    return requests.get('http://example.com').status_code


@async_timed()
async def main():
    task_1 = asyncio.create_task(get_example_status())
    task_2 = asyncio.create_task(get_example_status())
    task_3 = asyncio.create_task(get_example_status())

    await task_1
    await task_2
    await task_3


asyncio.run(main())
