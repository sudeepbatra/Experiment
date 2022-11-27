import asyncio


async def add_one(number: int) -> int:
    return number + 1


# mimicking a normal call stack.
async def main() -> None:
    one_plus_one = await add_one(1)
    two_plus_one = await add_one(one_plus_one)

    print(one_plus_one)
    print(two_plus_one)


asyncio.run(main())
