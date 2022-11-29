from asyncio import Future

import asyncio


async def set_future_value(future) -> None:
    await asyncio.sleep(1)
    future.set_result(42)


def make_request() -> Future:
    future = Future()
    asyncio.create_task(set_future_value(future))
    return future


async def main():
    future = make_request()
    print(f"Is the future done? {future.done()}")
    result = await future
    print(f"Is the future done? {future.done()}")
    print(result)


asyncio.run(main())
