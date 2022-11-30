import asyncio
from asyncio.events import AbstractEventLoop
from concurrent.futures import ProcessPoolExecutor
from functools import partial
from typing import List


def count(count_to: int) -> int:
    counter = 0
    while counter < count_to:
        counter += 1
    return counter


async def main():
    with ProcessPoolExecutor() as process_pool:
        loop: AbstractEventLoop = asyncio.get_event_loop()
        nums = [5000000000, 1, 3, 5, 22, 100000000, 200000000, 500000000, 1000000000]
        calls: List[partial[int]] = [partial(count, nums) for nums in nums]

        call_coros = []
        for call in calls:
            call_coros.append(loop.run_in_executor(process_pool, call))
        results = await asyncio.gather(*call_coros)

        for result in results:
            print(result)


if __name__ == "__main__":
    asyncio.run(main())
