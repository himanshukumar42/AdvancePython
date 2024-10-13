import asyncio


async def function1():
    await asyncio.sleep(3)
    print("Function 1")


async def function2():
    await asyncio.sleep(2)
    print("Function 2")


async def function3():
    await asyncio.sleep(3)
    print("Function 3")


async def main() -> None:
    L = await asyncio.gather(
        function1(),
        function2(),
        function3()
    )


if __name__ == '__main__':
    asyncio.run(main())
