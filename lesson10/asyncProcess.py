import asyncio


async def emulate_async_process():
    # წარმოვიდგინოთ რომ აქ მოგვავს ინფორმაცია ამინდის API-დან რომელსაც 5 წამი ჭირდება ჩასატვირთად
    print("Async function 1 started")
    await asyncio.sleep(5)
    print("Async function 1 finished")


async def another_async_process():
    # წარმოვიდგინოთ რომ აქ მოგვავს ინფორმაცია ამინდის API-დან რომელსაც 5 წამი ჭირდება ჩასატვირთად
    print("Async function 2 started")
    await asyncio.sleep(3)
    print("Async function 2 finished")


async def third_async_process():
    await asyncio.sleep(2)
    print("Async function 3 finished")


async def main():
    task1 = asyncio.create_task(emulate_async_process())
    task2 = asyncio.create_task(another_async_process())
    task3 = asyncio.create_task(third_async_process())
    await task1
    await task2
    await task3
    print("Main function finished")

asyncio.run(main())
