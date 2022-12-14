import asyncio
from util import delay


async def main():
    # Create task returns instantly and schedules it to run as soon as possible. await expression will extract the value once it is complete.
    sleep_for_three = asyncio.create_task(delay(3))
    print(type(sleep_for_three))
    result = await sleep_for_three
    print(result)


asyncio.run(main())
