import time
import asyncio

async def function1():
    await asyncio.sleep(1)
    print("func 1")
    return "Abhishek"

async def function2():
    await asyncio.sleep(1)
    print("Func 2")

async def function3():
    await asyncio.sleep(4)
    print("Func 3")

# async def main():
#     task = asyncio.create_task(function1())
#     await function1()
#     await function2()
#     await function3()

async def main():
    L = await asyncio.gather(
        function1(),
        function2(),
        function3(),
    )

    print(L)
asyncio.run(main())
