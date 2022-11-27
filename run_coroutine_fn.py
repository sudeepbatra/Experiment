import asyncio


async def coroutine_add_one(number: int) -> int:
    return number + 1


# Put coroutine on the event loop and execute it
result = asyncio.run(coroutine_add_one(1))
print(result)
